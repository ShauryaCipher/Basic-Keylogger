"""
Basic tests for the keylogger educational demonstration.
"""

import os
import unittest
import tempfile
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the keylogger module (without activating the keyboard listener)
from keylogger import EducationalKeylogger

class TestKeyloggerBasics(unittest.TestCase):
    """Test basic functionality of the keylogger class without activating listeners."""
    
    def setUp(self):
        """Set up a temporary directory for log files."""
        self.test_dir = tempfile.mkdtemp()
        
    def test_initialization(self):
        """Test that the keylogger initializes properly."""
        keylogger = EducationalKeylogger(log_dir=self.test_dir, collect_system_info=False)
        
        # Check that the log directory was created
        self.assertTrue(os.path.exists(self.test_dir))
        
        # Check that a log file was created
        self.assertIsNotNone(keylogger.log_file)
        self.assertTrue(os.path.exists(keylogger.log_file))
        
    def test_log_file_creation(self):
        """Test that the log file contains the expected headers."""
        keylogger = EducationalKeylogger(log_dir=self.test_dir, collect_system_info=False)
        
        # Read the log file
        with open(keylogger.log_file, 'r') as f:
            content = f.read()
        
        # Check for expected header content
        self.assertIn("=== EDUCATIONAL KEYLOGGER DEMONSTRATION ===", content)
        self.assertIn("Log started at:", content)
        
    def test_special_keys_mapping(self):
        """Test that the special keys mapping is properly initialized."""
        keylogger = EducationalKeylogger(log_dir=self.test_dir)
        
        # Check that common special keys are mapped
        self.assertTrue(len(keylogger.special_keys) > 10)  # Should have multiple mappings
        
        # Check a few specific mappings that should exist
        from pynput.keyboard import Key
        self.assertEqual(keylogger.special_keys[Key.space], " ")
        self.assertEqual(keylogger.special_keys[Key.enter], "[ENTER]\n")
        
    def tearDown(self):
        """Clean up test files and directories."""
        # Remove the temporary directory and its contents
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

if __name__ == '__main__':
    unittest.main()