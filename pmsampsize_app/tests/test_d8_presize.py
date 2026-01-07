
import unittest
import sys
import os
import math
import numpy as np
from scipy.stats import norm

# Add project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from pmsampsize_app.core.d8_auc import prec_auc

class TestD8Presize(unittest.TestCase):
    
    def calculate_expected_width(self, auc, prev, n, conf_level=0.95):
        """Manual calculation of Hanley-McNeil width for verification"""
        n1 = n * prev
        n2 = n * (1 - prev)
        
        q0 = auc * (1 - auc)
        q1 = auc / (2 - auc) - auc**2
        q2 = 2 * auc**2 / (1 + auc) - auc**2
        
        se = math.sqrt((q0 + (n1 - 1) * q1 + (n2 - 1) * q2) / (n1 * n2))
        alpha = (1 - conf_level) / 2
        z = norm.ppf(1 - alpha)
        
        return 2 * z * se

    def test_scenario_1_precision(self):
        """Scenario 1: auc=0.65, prev=0.10, n=500, conf.level=0.95"""
        res = prec_auc(auc=0.65, prev=0.10, n=500, conf_level=0.95)
        
        expected_width = self.calculate_expected_width(0.65, 0.10, 500, 0.95)
        self.assertAlmostEqual(res["conf_width"], expected_width, places=4)
        self.assertEqual(res["n"], 500)
        
    def test_scenario_2_sample_size(self):
        """Scenario 2: auc=0.80, prev=0.10, conf.width=0.10, conf.level=0.95"""
        target_width = 0.10
        res = prec_auc(auc=0.80, prev=0.10, conf_width=target_width, conf_level=0.95)
        
        # Verify the achieved width matches target close enough
        self.assertAlmostEqual(res["conf_width"], target_width, places=4)
        
        # Verify the N found produces this width
        recalc_width = self.calculate_expected_width(0.80, 0.10, res["n"], 0.95)
        self.assertAlmostEqual(recalc_width, target_width, places=4)

    def test_scenario_3_low_conf(self):
        """Scenario 3: auc=0.75, prev=0.20, conf.width=0.08, conf.level=0.90"""
        target_width = 0.08
        res = prec_auc(auc=0.75, prev=0.20, conf_width=target_width, conf_level=0.90)
        
        self.assertAlmostEqual(res["conf_width"], target_width, places=4)
        
    def test_edge_case_max_variance(self):
        """AUC=0.5, Prev=0.5 -> Max variance scenario"""
        res = prec_auc(auc=0.5, prev=0.5, n=100)
        # q1 = 0.5/1.5 - 0.25 = 0.333 - 0.25 = 0.0833
        # q2 = 0.5/1.5 - 0.25 = 0.0833 (Symmetric)
        # q0 = 0.25
        # Matches manual check logic
        expected = self.calculate_expected_width(0.5, 0.5, 100)
        self.assertAlmostEqual(res["conf_width"], expected, places=4)

    def test_optimization_bounds(self):
        """Test finding N for very small width (requires large N)"""
        # width = 0.01 is strict
        res = prec_auc(auc=0.8, prev=0.5, conf_width=0.01)
        self.assertTrue(res["n"] > 1000)
        self.assertAlmostEqual(res["conf_width"], 0.01, places=4)

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            prec_auc(auc=1.5, prev=0.5, n=100) # Invalid AUC
        with self.assertRaises(ValueError):
            prec_auc(auc=0.5, prev=-0.1, n=100) # Invalid Prev
        with self.assertRaises(ValueError):
            prec_auc(auc=0.5, prev=0.5, n=None, conf_width=None) # Both None

if __name__ == "__main__":
    unittest.main()
