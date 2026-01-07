
import unittest
import sys
import os
import numpy as np

# Add project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from pmsampsize_app.methods.d9_extval import calculate_pmvalsampsize, calculate_sampsizeval, find_lp_params_from_c_and_p

class TestD9ExternalValidation(unittest.TestCase):
    
    def test_lp_params_search(self):
        """Test finding normal parameters for C and P."""
        c = 0.8
        p = 0.1
        mu, sigma = find_lp_params_from_c_and_p(c, p)
        
        # Sigma should be driven by C. C=0.8 -> sigma ~ 1.19
        # sigma = norm.ppf(0.8)*sqrt(2) = 0.84 * 1.41 = 1.18
        self.assertAlmostEqual(sigma, 1.19, delta=0.1)
        
        # If simulation with these params roughly gives back C and P
        np.random.seed(42)
        lp = np.random.normal(mu, sigma, 100000)
        probs = 1 / (1 + np.exp(-lp))
        p_est = np.mean(probs)
        self.assertAlmostEqual(p_est, p, delta=0.01)
        
    def test_pmvalsampsize_determinism(self):
        """Test that pmvalsampsize is deterministic with seed."""
        res1 = calculate_pmvalsampsize(0.1, 0.8, 0.2, 0.2, 0.1, n_sim=10000, seed=123)
        res2 = calculate_pmvalsampsize(0.1, 0.8, 0.2, 0.2, 0.1, n_sim=10000, seed=123)
        
        self.assertEqual(res1['n_recom'], res2['n_recom'])
        self.assertEqual(res1['events_recom'], res2['events_recom'])
        self.assertEqual(res1['lp_mu'], res2['lp_mu'])
        
    def test_pmvalsampsize_logic(self):
        """Test basic logic directions."""
        # Tighter O/E width -> Larger N
        res_loose = calculate_pmvalsampsize(0.1, 0.8, 0.2, 1.0, 1.0, n_sim=10000) # Only O/E matters
        res_strict = calculate_pmvalsampsize(0.1, 0.8, 0.1, 1.0, 1.0, n_sim=10000)
        
        self.assertGreater(res_strict['n_oe'], res_loose['n_oe'])
        
    def test_sampsizeval_logic(self):
        """Test sampsizeval (Pavlou) logic."""
        # C-stat sizing
        # SE(C) reduced -> N increased
        res1 = calculate_sampsizeval(0.1, 0.8, 0.025, 1.0, 1.0)
        res2 = calculate_sampsizeval(0.1, 0.8, 0.01, 1.0, 1.0)
        
        self.assertGreater(res2['n_c'], res1['n_c'])
        
        # Slope sizing
        res_slope1 = calculate_sampsizeval(0.1, 0.8, 1.0, 0.05, 1.0)
        res_slope2 = calculate_sampsizeval(0.1, 0.8, 1.0, 0.025, 1.0)
        
        self.assertGreater(res_slope2['n_slope'], res_slope1['n_slope'])

if __name__ == "__main__":
    unittest.main()
