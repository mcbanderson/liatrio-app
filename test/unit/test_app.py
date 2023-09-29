import unittest

from app.app import hello_world, about_me, ralph


class AppTestCase(unittest.TestCase):
    """Test app.py."""

    def test_hello_world_endpoint(self):
        """Test the hello world endpoint returns a string."""
        assert isinstance(hello_world(), str)

    def test_ralph_endpoint(self):
        """Test the ralph endpoint returns a string."""
        assert isinstance(ralph(), str)

    def test_ralph_endpoint_contains_last_name(self):
        """Test the ralph endpoint returns the correct string."""
        assert "Mechrek" in ralph()
