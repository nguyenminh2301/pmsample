
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import sys
import os

# Add project root to path (parent of pmsampsize_app)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

try:
    from pmsampsize_app import reporting
except ImportError:
    # Fallback if running from within module
    import reporting

class TestReporting(unittest.TestCase):
    
    def setUp(self):
        self.context = {
            "method_title": "Test Method",
            "inputs": {"Prevalence": 0.1, "Params": 10},
            "timestamp": "2023-01-01"
        }
        self.df = pd.DataFrame({"Col1": [1, 2], "Col2": [3, 4]})
        self.T = {
            "report_header": "Report",
            "title": "Title",
            "results": "Results",
            "riley_inputs": "Inputs"
        }

    def test_generate_report_markdown(self):
        md = reporting.generate_report_markdown(self.context, self.df, self.T)
        self.assertIn("# Report", md)
        self.assertIn("Test Method", md)
        self.assertIn("Prevalence", md)
        self.assertIn("|   Col1 |   Col2 |", md) # Table check in markdown

    def test_generate_report_empty(self):
        md = reporting.generate_report_markdown(self.context, None, self.T)
        self.assertEqual(md, "No results to report.")

    @patch("smtplib.SMTP")
    def test_send_email_success(self, mock_smtp):
        # Mock server instance
        server_instance = MagicMock()
        mock_smtp.return_value = server_instance
        
        success, msg = reporting.send_email(
            "to@example.com", 
            "Subject", 
            "**Body**", 
            self.df, 
            "from@example.com", 
            "password"
        )
        
        self.assertTrue(success)
        self.assertEqual(msg, "Success")
        
        # Verify calls
        mock_smtp.assert_called_with('smtp.gmail.com', 587)
        server_instance.starttls.assert_called_once()
        server_instance.login.assert_called_with("from@example.com", "password")
        server_instance.sendmail.assert_called_once()

    def test_send_email_no_creds(self):
        success, msg = reporting.send_email("to@example.com", "Subj", "Body")
        self.assertFalse(success)
        self.assertIn("credentials missing", msg)

if __name__ == "__main__":
    unittest.main()
