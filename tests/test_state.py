import sys
import os

# Add project root to sys.path 

# sys.path.append(...) -> (Adds the project root folder to Python’s module search path.)
# Python will now be able to find modules inside src even if the script is run from tests.
# Without this, Python would throw: ModuleNotFoundError: No module named 'src'
# Python does not automatically know about C:\Quantum_Simulator when you run test_state.py inside the tests folder.
# By adding the project root to sys.path, you make from src.core.states import Qubit work correctly.

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

from src.core.states import Qubit  # Only once

# Test case 1: Real Numbers
def test_normalization():
    q = Qubit(3, 4)
    q.normalize()
    pa, pb = q.probabilities()
    assert round(pa + pb, 5) == 1.0
    print("Test 1 passed: Real qubit normalized correctly.")

# Test case 2: Complex Numbers
def test_complex_normalization():
    q = Qubit(3+4j, 1-2j)
    q.normalize()
    pa, pb = q.probabilities()
    assert round(pa + pb, 5) == 1.0
    print("Test 2 passed: Complex qubit normalized correctly.")

# Part 2: The if __name__ == "__main__": block
# __name__ is a special Python variable.
# When a Python file is run directly, __name__ is set to "__main__".
# When a Python file is imported as a module, __name__ is set to the module name, e.g., "test_state" or "states".

if __name__ == "__main__":
    test_normalization()
    test_complex_normalization()
    
# if __name__ == "__main__":

# This checks if the script is being run directly, not imported.
# Only if it’s run directly, the code inside this block will execute.


# test_normalization() and test_complex_normalization()

# These are function calls to your test cases.
# They execute the tests when the script is run.
# If the script is imported elsewhere, these tests won’t run automatically, preventing unwanted execution.