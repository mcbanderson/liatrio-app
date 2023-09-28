"""Smoke test running instance of app.py."""
import sys

import requests

# Ideally we'd use pytest here, but for now we're not for simplicity
def test_hello_world_endpoint(endpoint):
    """Test the hello world endpoint returns a 200 status code."""
    assert requests.get(endpoint).status_code == 200

if __name__ == '__main__':
    test_hello_world_endpoint(sys.argv[1])
