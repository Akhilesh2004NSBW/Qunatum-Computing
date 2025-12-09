import numpy as np

def apply_kraus(rho, kraus_list):
    
    out = np.zeros_like(rho, dtype=complex)
    for E in kraus_list:
        out += E @ rho @ E.conj().T
    return out

def apply_amplitude_damping(rho, gamma):
  

    sqrt1mg = np.sqrt(max(0.0, 1.0 - gamma))
    sqrtg = np.sqrt(max(0.0, gamma))

    E0 = np.array([[1.0, 0.0],
                   [0.0, sqrt1mg]], dtype=complex)

    E1 = np.array([[0.0, sqrtg],
                   [0.0, 0.0]], dtype=complex)

    return apply_kraus(rho, [E0, E1])

def test_amplitude_damping():
    rho = np.array([[0.0, 0.0],
                    [0.0, 1.0]], dtype=complex)   # |1><1|

    gamma = 0.4   # 40% decay

    rho_new = apply_amplitude_damping(rho, gamma)

    print("Initial Density Matrix (rho):")
    print(rho)

    print("\nDensity Matrix after Amplitude Damping (gamma = {}):".format(gamma))
    print(rho_new)

# Run the test
test_amplitude_damping()