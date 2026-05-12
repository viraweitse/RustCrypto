# test_rustcrypto.py
"""
Tests for RustCrypto module.
"""

import unittest
from rustcrypto import RustCrypto

class TestRustCrypto(unittest.TestCase):
    """Test cases for RustCrypto class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RustCrypto()
        self.assertIsInstance(instance, RustCrypto)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RustCrypto()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
