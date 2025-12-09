import numpy as np 

def apply_kraus(rho, kraus_list):
    out = np.zeros_like(rho, dtype=complex)  # FIXED dtype
    
    for E in kraus_list:
        out += E @ rho @ E.conj().T
    return out

def apply_phase_damping(rho, gamma):
    sqrt1mg = np.sqrt(max(0.0, 1.0 - gamma))
    sqrtg = np.sqrt(max(0.0, gamma))

    E0 = np.array([[1.0, 0.0],
                   [0.0, sqrt1mg]], dtype=complex)

    E1 = np.array([[0.0, 0.0],
                   [0.0, sqrtg]], dtype=complex)

    return apply_kraus(rho, [E0, E1])

# Test Phase Damping Noise by Akhileesh Pant (APX)

def test_phase_damping():
    rho = np.array([[0.5, 0.5],
                    [0.5, 0.5]], dtype=complex)

    gamma = 0.6  # 60% loss of coherence

    new_rho = apply_phase_damping(rho, gamma)

    print("Initial Density Matrix (rho):")
    print(rho)

    print("\nDensity Matrix after Phase Damping with gamma =", gamma)
    print(new_rho)

# Run the test
test_phase_damping()
