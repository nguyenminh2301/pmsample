
import unittest
import numpy as np
import sys
import os

# Add project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from pmsampsize_app.core.riley import calculate_r2_max, auc_to_r2_simulation, calculate_sample_size

class TestCoreRiley(unittest.TestCase):
    
    # Test R2 Max
    def test_r2_max(self):
        # p = 0.5 -> max R2 = 0.75
        r2 = calculate_r2_max(0.5)
        self.assertAlmostEqual(r2, 0.75, delta=0.01)
    
        # p = 0.1
        r2_p01 = calculate_r2_max(0.1)
        self.assertAlmostEqual(r2_p01, 0.478, delta=0.01)
    
    # Test AUC to R2
    def test_auc_to_r2(self):
        # AUC = 0.5 -> R2 should be ~0
        r2 = auc_to_r2_simulation(0.5, 0.1, n_sim=10000)
        self.assertLess(r2, 0.01)
        
        # AUC = 0.8, p = 0.1
        # Check consistency (determinism via seed)
        r2_a = auc_to_r2_simulation(0.8, 0.1, n_sim=10000, seed=42)
        r2_b = auc_to_r2_simulation(0.8, 0.1, n_sim=10000, seed=42)
        self.assertEqual(r2_a, r2_b)
        self.assertGreater(r2_a, 0.1) # Should be significant
    
    # Test Sample Size Calculation
    def test_sample_size_basic(self):
        # Example: 10 parameters, p=0.1, R2=0.2, Shrinkage=0.9
        res = calculate_sample_size(p=0.1, parameters=10, r2=0.2, shrinkage=0.9)
        # Check if keys exist
        self.assertIn("n_total", res)
        self.assertGreater(res['n_total'], 0)
        self.assertIn(res['binding_criterion'], [1, 2, 3])
    
    def test_sample_size_precision_dominates(self):
        # If p is very small, precision (criterion 3) might dominate
        res = calculate_sample_size(p=0.5, parameters=1, r2=0.4)
        # C3 should be around 385
        self.assertEqual(res['binding_criterion'], 3)
        self.assertTrue(abs(res['n_total'] - 385) < 5)
    
    def test_sanity_check_values(self):
        # Common rule of thumb EPV 10 or 20
        # p=0.1, P=10 -> EPV 10 -> Events=100 -> N=1000
        res = calculate_sample_size(p=0.1, parameters=10, auc=0.8)
        # Usually around 400-800 depending on R2.
        self.assertGreater(res['n_total'], 100)

if __name__ == "__main__":
    unittest.main()
