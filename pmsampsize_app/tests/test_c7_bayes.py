
import unittest
import sys
import os
import pandas as pd
import numpy as np

# Add project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from pmsampsize_app.core.bayes import BayesianAssuranceSimulation, HAS_PYMC

@unittest.skipUnless(HAS_PYMC, "PyMC not installed")
class TestC7Bayes(unittest.TestCase):
    
    def test_run_joblib(self):
        """Test that joblib parallelization works"""
        # Small run
        sim = BayesianAssuranceSimulation(
            p_true=0.3,
            P=3,
            n_continuous=2,
            n_binary=1,
            rho=0.1,
            n_candidates=[500],
            n_sims=4, # Small for speed
            start_seed=42
        )
        df, audit = sim.run()
        
        self.assertFalse(df.empty)
        self.assertEqual(len(df), 1)
        self.assertIn("assurance", df.columns)
        self.assertEqual(len(audit["replicates"]), 4)
        
    def test_determinism(self):
        """Test that same seed produces same result even with parallel execution"""
        params = {
            "p_true": 0.3, "P": 3, "n_continuous": 2, "n_binary": 1, "rho": 0.1,
            "n_candidates": [500], "n_sims": 4, "start_seed": 12345
        }
        
        # Run 1
        sim1 = BayesianAssuranceSimulation(**params)
        df1, _ = sim1.run()
        
        # Run 2
        sim2 = BayesianAssuranceSimulation(**params)
        df2, _ = sim2.run()
        
        pd.testing.assert_frame_equal(df1, df2)

if __name__ == "__main__":
    unittest.main()
