# tests/test_utils.py

import sys
import os

# 1. Add the project root to the system path so Python can find 'src'
# The directory of the test file is 'tests'. We go up one level (..) to get to NIU-PREP root.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 2. Now the import should work without the system environment being configured
from src.utilis import greet

def test_greet_standard_name():
    expected_output = "Hello, Contributor! Welcome to the Neuroinformatics Kit."
    assert greet("Contributor") == expected_output

# ... (Keep your other two test functions here)
# ... test_greet_empty_name()
# ... test_greet_contains_welcome_phrase()