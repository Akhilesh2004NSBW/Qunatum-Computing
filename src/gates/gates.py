import math
import numpy as np

# Hadmard Gate (H) - Creates Superposition

H = (1/math.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])

# Pauli - X Gate - Bit Flip - |0> <-> |1>

X = np.array([
    [0, 1],
    [1, 0]
])

# Pauli -Y Gate - Adds Phase & Flips bits

Y = np.array([
    [0, -1j],
    [1j, 0]
])

# Pauli - Z Gate - Phase flip: |1> gets a minus sign.

Z = np.array([
    [1, 0],
    [0, -1]
])

# Identity Gate (I) - Does nothing, useful in larger circuit

I  = np.array([
    [1, 0],
    [0, 1]
])

# CNOT (Controlled - NOT) Gate - 2 Qubit Gate

CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

