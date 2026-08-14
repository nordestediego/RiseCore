# test_risecore.py
"""
Tests for RiseCore module.
"""

import unittest
from risecore import RiseCore

class TestRiseCore(unittest.TestCase):
    """Test cases for RiseCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RiseCore()
        self.assertIsInstance(instance, RiseCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RiseCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
