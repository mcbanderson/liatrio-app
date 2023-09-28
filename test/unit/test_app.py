import unittest

from app.app import hello_world, about_me


class AppTestCase(unittest.TestCase):
    """Test app.py."""

    def test_hello_world_endpoint(self):
        """Test the hello world endpoint returns a string."""
        assert isinstance(hello_world(), str)
