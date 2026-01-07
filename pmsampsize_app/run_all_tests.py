
import unittest
import sys
import os

# Add project root to path (parent of this script's dir)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_tests():
    print("Running Global Test Suite for Prognostic Research Sample Size Tool...")
    loader = unittest.TestLoader()
    start_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests')
    
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\nSUCCESS: All tests passed!")
        return 0
    else:
        print(f"\nFAILURE: {len(result.errors)} errors, {len(result.failures)} failures.")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())
