# tests/test_utils.py
import sys
import os

# --- CRITICAL MANUAL FIX ---
# This forces the project root (NIU_PREP) onto the Python path so pytest can find 'src'
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
# ---------------------------

# Now the import will work regardless of environment configuration
from src.utils import greet

def test_greet_standard_name():
    """Test the basic greeting function with standard input."""
    expected_output = "Hello, Contributor! Welcome to the Neuroinformatics Kit."
    assert greet("Contributor") == expected_output

def test_greet_empty_name():
    """Test the basic greeting function with an empty string."""
    expected_output = "Hello, ! Welcome to the Neuroinformatics Kit."
    assert greet("") == expected_output

def test_greet_invalid_input():
    """Test that the greet function handles a non-string input gracefully."""
    # The function should return the specific error message, not raise an error
    expected_fallback = "Hello! I received bad input and cannot greet you properly."
    assert greet(12345) == expected_fallback
    assert greet(True) == expected_fallback