from src.core.states import Qubit
from src.gates.gates import H

def create_superposition(initial='0'):
    """Returns a qubit in superposition using the Hadamard gate."""

    initial = initial.strip().lower()

    if initial not in ('0', '1'):
        raise ValueError("Initial state must be '0' or '1'")

    q = Qubit(1, 0) if initial == '0' else Qubit(0, 1)
    q.apply_gate(H)
    return q
