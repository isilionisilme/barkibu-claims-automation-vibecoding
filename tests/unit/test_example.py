"""
Example unit test demonstrating the testing approach.

This test verifies basic functionality and demonstrates:
- Fail-fast configuration
- Proper test structure
- Timeout handling
"""

import pytest


def test_example_basic():
    """Test basic assertion."""
    result = 2 + 2
    assert result == 4, "Basic math should work"


def test_example_with_fixture(tmp_path):
    """Test using pytest fixture."""
    # Create a temporary file
    test_file = tmp_path / "test.txt"
    test_file.write_text("test content")
    
    # Verify it exists and has correct content
    assert test_file.exists()
    assert test_file.read_text() == "test content"


@pytest.mark.timeout(5)
def test_example_with_timeout():
    """Test with explicit timeout (5 seconds)."""
    # This test will fail if it takes longer than 5 seconds
    result = sum(range(1000))
    assert result == 499500


def test_example_exception_handling():
    """Test that exceptions are handled correctly."""
    with pytest.raises(ValueError):
        raise ValueError("Expected error")


class TestExampleClass:
    """Example test class grouping related tests."""
    
    def test_method_one(self):
        """Test method one."""
        assert True
    
    def test_method_two(self):
        """Test method two."""
        assert 1 + 1 == 2
