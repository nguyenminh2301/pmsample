
import unittest
import sys
import os
import numpy as np

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from pmsampsize_app.core import epv as core_quick_epv
from pmsampsize_app.core import precision as core_quick_binom_precision

class TestQuickTools(unittest.TestCase):
    
    def test_epv_calculation(self):
        """Test A1 EPV Logic"""
        # p=0.1, P=10, EPV=10 -> Events=100, N=1000
        df = core_quick_epv.calculate_epv_size(0.1, 10, 10)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["Required_Events"], 100)
        self.assertEqual(df.iloc[0]["Required_N"], 1000)
        
        # Ranges
        df2 = core_quick_epv.calculate_epv_size([0.1, 0.2], 10, 10)
        self.assertEqual(len(df2), 2)
        
    def test_binom_precision_wald(self):
        """Test A2 Wald Logic (Closed Form)"""
        # p=0.5, d=0.05, conf=0.95 (z~1.96)
        # N = 1.96^2 * 0.25 / 0.0025 = 3.84*100 = 384 approx
        res = core_quick_binom_precision.calculate_binom_size(0.5, 0.05, 0.95, "wald")
        self.assertTrue(380 < res["N"] < 390)
        self.assertEqual(res["Method"], "Wald")
        
    def test_binom_precision_monotone(self):
        """Test A2 Wilson Monotone Search"""
        # p=0.1, d=0.02
        res = core_quick_binom_precision.calculate_binom_size(0.1, 0.02, 0.95, "wilson")
        n = res["N"]
        self.assertTrue(n > 0)
        self.assertLess(res["Actual_Half_Width"], 0.02 + 1e-9)
        
        # Verify N-1 fails (or at least N is tight)
        # This is strictly hard to test perfectly due to integer granularity but check reasonableness
        # Approx n ~ 1.96^2 * 0.09 / 0.0004 = 3.84 * 225 = 864
        self.assertTrue(800 < n < 950)

if __name__ == '__main__':
    unittest.main()
