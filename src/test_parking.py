"""
Automated Test Suite for Parking Compliance Engine
Author: Michael Stephen Curbeam Jr. 
Description: Unit tests verifying deterministic logical constraints and 
             edge-case validation matrices for the parking system.
"""

import unittest
# Import the specific functions we want to test from main.py
from .main import parse_time, check_overnight_restriction

class TestParkingCompliance(unittest.TestCase):

    def test_valid_time_parsing(self):
        """Verify that valid time strings are correctly tokenized."""
        hour, minutes, period = parse_time("10:30 AM")
        self.assertEqual(hour, 10)
        self.assertEqual(minutes, 30)
        self.assertEqual(period, "AM")

    def test_invalid_time_parsing(self):
        """Verify that malformed time strings return safe None values."""
        hour, minutes, period = parse_time("invalid_time_string")
        self.assertIsNone(hour)
        self.assertIsNone(minutes)
        self.assertIsNone(period)

    def test_overnight_restriction_active(self):
        """Verify 12:00 AM to 3:00 AM restriction accurately triggers violation state."""
        # 1:30 AM is strictly inside the restricted window
        is_restricted = check_overnight_restriction(1, 30, "AM")
        self.assertTrue(is_restricted)

    def test_overnight_restriction_inactive(self):
        """Verify times outside 12:00 AM to 3:00 AM are allowed by default."""
        # 4:15 AM is safely past the restricted window
        is_restricted = check_overnight_restriction(4, 15, "AM")
        self.assertFalse(is_restricted)

    def test_overnight_grace_period(self):
        """Verify the 3:00 AM grace period logic allows parking past 3:00 AM."""
        # 3:05 AM should pass because it is past the 3:00 AM threshold
        is_restricted = check_overnight_restriction(3, 5, "AM")
        self.assertFalse(is_restricted)

if __name__ == "__main__":
    unittest.main()