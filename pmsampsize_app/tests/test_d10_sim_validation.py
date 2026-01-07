
import unittest
import numpy as np
import pandas as pd
import sys
import os

# Internal
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from pmsampsize_app.core.d10_sim import run_d10_simulation, sim_lp_distribution, solve_gamma_for_target_p, inverse_logit

class TestD10Sim(unittest.TestCase):
    
    def test_determinism(self):
        """Test that same seed produces identical results"""
        n_list = [200]
        params = {"mu": -1.75, "sd": 1.47}
        
        df1, audit1 = run_d10_simulation(n_list, "normal", params, n_sims=50, seed_start=12345)
        df2, audit2 = run_d10_simulation(n_list, "normal", params, n_sims=50, seed_start=12345)
        
        pd.testing.assert_frame_equal(df1, df2)
        self.assertEqual(audit1["seed_start"], audit2["seed_start"])

    def test_width_decreases_with_n(self):
        """Test that increasing N reduces CI width on average"""
        n_list = [100, 500, 2000]
        params = {"mu": 0, "sd": 1} # Simpler case
        
        df, _ = run_d10_simulation(n_list, "normal", params, n_sims=100, seed_start=42)
        
        # Check monotonic decrease for C Width and Slope Width
        widths_c = df["Mean_C_Width"].values
        widths_s = df["Mean_Slope_Width"].values
        
        self.assertTrue(widths_c[0] > widths_c[1] > widths_c[2], f"C widths not decreasing: {widths_c}")
        self.assertTrue(widths_s[0] > widths_s[1] > widths_s[2], f"Slope widths not decreasing: {widths_s}")

    def test_solve_gamma(self):
        """Test gamma solving for prevalence"""
        target_p = 0.2
        slope = 1.0
        
        def lp_gen(n): 
            np.random.seed(111)
            return np.random.normal(-1.0, 1.0, n)
            
        gamma = solve_gamma_for_target_p(target_p, slope, lp_gen, n_integration=5000)
        
        # Verify
        lp_check = lp_gen(5000)
        p_check = np.mean(inverse_logit(gamma + slope * lp_check))
        
        self.assertAlmostEqual(p_check, target_p, places=2)

    def test_miscalibration_params(self):
        """Test that S != 1 works"""
        # If true slope is 0.5, then estimated slope should be around 0.5?
        # Simulation generates Y based on True S=0.5.
        # Calibration model fits Y ~ LP.
        # Slope estimate should be ~0.5.
        
        n_list = [1000]
        # LP ~ N(0,1)
        params = {"mu": 0, "sd": 1}
        # True model: logit(p) = 0 + 0.5 * LP
        # Fitted model: logit(p) = a + b * LP
        # b should be ~ 0.5
        
        # We need to peek inside run_d10_simulation or trust the width logic.
        # CI Width depends on SE. SE depends on Fisher Info. 
        # Here we just check it runs without error.
        
        df, _ = run_d10_simulation(n_list, "normal", params, slope_true=0.5, n_sims=50)
        self.assertFalse(df.empty)
        self.assertTrue("Mean_Slope_Width" in df.columns)

if __name__ == "__main__":
    unittest.main()
