
import unittest
import sys
import os
import pandas as pd
import numpy as np

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from pmsampsize_app.core.dev_sim import SampleSizeDevSimulation

class TestMethod6(unittest.TestCase):
    
    def test_simple_mode(self):
        """Test Simple Mode runs and produces reasonable output"""
        # Small run
        sim = SampleSizeDevSimulation(
            mode="simple", 
            p_true=0.1, 
            P=5, 
            target_auc=0.75,
            n_candidates=[500, 1000],
            n_sims=50, # Fast but robust enough
            start_seed=123
        )
        df, audit = sim.run()
        
        self.assertEqual(len(df), 2)
        self.assertIn("Slope_mean", df.columns)
        self.assertIn("AUC_mean", df.columns)
        
        # Check AUC roughly matches target (0.75) within loose bounds from small N
        auc_500 = df.loc[0, "AUC_mean"]
        self.assertTrue(0.6 < auc_500 < 0.9, f"AUC {auc_500} should be near 0.75")
        
        # Check monotonic trend: Slope SD should decrease as N increases
        sd_500 = df.loc[0, "Slope_sd"]
        sd_1000 = df.loc[1, "Slope_sd"]
        self.assertTrue(sd_1000 <= sd_500, f"Slope SD should decrease with N (500:{sd_500} vs 1000:{sd_1000})")

    def test_audit_trail(self):
        """Ensure RNG audit is populated"""
        sim = SampleSizeDevSimulation(n_sims=5, n_candidates=[500])
        df, audit = sim.run()
        self.assertEqual(audit["global_seed"], 20260107)
        self.assertTrue(len(audit["replicates"]) > 0)
        
    def test_custom_mode_runs(self):
        """Test Custom DGM logic path"""
        sim = SampleSizeDevSimulation(mode="custom", rho=0.5, P=5, n_sims=5, n_candidates=[1000])
        df, audit = sim.run()
        self.assertEqual(len(df), 1)
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()
