import numpy as np
from src.core.states import Qubit
from src.gates.gates import H, CNOT

def create_bell_pair():
    
    # Step 1: Initialize |0> Qubits
    q0 = Qubit(1, 0)
    q1 = Qubit(0, 1)
    
    # Step 2: Apply Hadamard to q0
    q0.apply_gate(H)
    
    # Step 3: Tensor Product -> Combined State
    combined = q0.tensor(q1)
    
    # Step 4: Apply CNOT -> Entangled Bell State
    entangled_state = np.dot(CNOT, combined)
    
    return entangled_state

def create_custom_entangled_state(alpha, beta):
    """create entanglement starting from any custom 1st Qubit (Superposition)."""
    q0 = Qubit(alpha, beta) # Custom Qubit
    q1 = Qubit(1, 0) # 2nd in |0>
    
    # Apply H only if interviewer asks for Bell type
    q0.apply_gate(H)
    combined = q0.tensor(q1)
    entangled_state = np.dot(CNOT, combined)
    
    return entangled_state