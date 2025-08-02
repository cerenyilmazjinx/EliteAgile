# test_eliteagile.py
"""
Tests for EliteAgile module.
"""

import unittest
from eliteagile import EliteAgile

class TestEliteAgile(unittest.TestCase):
    """Test cases for EliteAgile class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EliteAgile()
        self.assertIsInstance(instance, EliteAgile)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EliteAgile()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
