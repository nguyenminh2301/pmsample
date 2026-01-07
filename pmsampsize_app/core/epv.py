
import pandas as pd
import numpy as np

def calculate_epv_size(p, params, target_epv):
    """
    Calculates sample size based on Events Per Variable (EPV/EPP).
    N = ceil( (Target * P) / p )
    
    Args:
        p (float or list): Prevalence (0 < p < 1)
        params (int or list): Number of parameters (P)
        target_epv (float or list): Target Events Per Parameter (e.g. 10, 15, 20)
        
    Returns:
        pd.DataFrame: Scenario table
    """
    # Normalize inputs to lists
    if not isinstance(p, list): p = [p]
    if not isinstance(params, list): params = [params]
    if not isinstance(target_epv, list): target_epv = [target_epv]
    
    scenarios = []
    
    for pp in p:
        for P in params:
            for t in target_epv:
                req_events = np.ceil(t * P)
                req_n = np.ceil(req_events / pp)
                
                scenarios.append({
                    "Prevalence": pp,
                    "Parameters": P,
                    "Target_EPP": t,
                    "Required_Events": int(req_events),
                    "Required_N": int(req_n),
                    "Actual_EPP": round(req_events / P, 2)
                })
                
    return pd.DataFrame(scenarios)
