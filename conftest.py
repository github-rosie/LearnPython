# tests/conftest.py
import sys
import os

# Add the src directory to the PYTHONPATH
# Using conftest.py to update sys.path affects only the current test session. 
# Non-Intrusive: This approach is safe and doesn't affect the global or system-wide PYTHONPATH.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

