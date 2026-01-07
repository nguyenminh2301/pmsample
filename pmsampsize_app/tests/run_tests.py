import unittest
import sys
import os

# Add project root to path (3 levels up from this file: tests -> pmsampsize_app -> root)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from pmsampsize_app.core_riley import calculate_r2_max, auc_to_r2_simulation, calculate_sample_size

class TestPmsampsize(unittest.TestCase):
    
    def test_r2_max(self):
        # p=0.5 -> max=0.75
        r2 = calculate_r2_max(0.5)
        self.assertAlmostEqual(r2, 0.75, places=2)
        
        # p=0.1
        # Formula check: 1 - exp(2*(0.1ln0.1 + 0.9ln0.9)) -> ~0.478
        r2_p01 = calculate_r2_max(0.1)
        self.assertAlmostEqual(r2_p01, 0.478, places=3)
        
    def test_auc_to_r2(self):
        # AUC=0.5 -> R2~0
        r2 = auc_to_r2_simulation(0.5, 0.1, n_sim=10000)
        self.assertTrue(r2 < 0.01)
        
        # AUC=0.8, p=0.1 -> R2 > 0
        r2_real = auc_to_r2_simulation(0.8, 0.1, n_sim=10000, seed=42)
        self.assertTrue(r2_real > 0.05) 

    def test_sample_size_calculation(self):
        # Scenario: p=0.1, params=10, AUC=0.8, S=0.9
        # 1. R2 max = 0.478
        # 2. AUC 0.8 -> R2 ~?
        #    mu = sqrt(2)*0.84 = 1.19
        #    R2 approx 0.2?
        # 3. Calc N
        res = calculate_sample_size(p=0.1, parameters=10, auc=0.8)
        
        n_total = res['n_total']
        self.assertGreater(n_total, 100)
        self.assertLess(n_total, 2000)
        self.assertTrue(res['binding_criterion'] in [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
