# demo_noise.py (or append to example.py)
import numpy as np
from src.core.states import Qubit
from src.gates.gates import H
from src.noise.noise import apply_phase_damping, apply_bit_flip, purity, probabilities_from_density

def demo_noise():
    print("=== Noise demo ===\n")

    # Create |+> state by applying H to |0>
    q = Qubit(1, 0)      # |0>
    q.apply_gate(H)      # |+> = (|0> + |1>)/sqrt(2)

    rho = q.to_density_matrix()
    print("Initial density matrix (|+>):")
    print(np.round(rho, 4))
    print("Purity:", purity(rho))
    print("Probabilities:", probabilities_from_density(rho))

    # Phase damping (dephasing)
    gamma = 0.4
    rho_deph = apply_phase_damping(rho, gamma)
    print(f"\nAfter phase damping (gamma={gamma}):")
    print(np.round(rho_deph, 4))
    print("Purity:", purity(rho_deph))
    print("Probabilities:", probabilities_from_density(rho_deph))

    # Bit-flip channel
    p = 0.3
    rho_bit = apply_bit_flip(rho, p)
    print(f"\nAfter bit-flip (p={p}):")
    print(np.round(rho_bit, 4))
    print("Purity:", purity(rho_bit))
    print("Probabilities:", probabilities_from_density(rho_bit))

if __name__ == "__main__":
    demo_noise()
