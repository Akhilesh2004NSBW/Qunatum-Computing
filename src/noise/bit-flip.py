import numpy as np 

def apply_kraus(rho, kraus_list):
    out = np.zeros_like(rho, dtype=complex)
    for E in kraus_list:
        out += E @ rho @ E.conj().T
    return out

def apply_bit_flip(rho, p):
    I = np.eye(2, dtype=complex)
    X = np.array([[0.0, 1.0],
                  [1.0, 0.0]], dtype=complex)

    E0 = np.sqrt(max(0.0, 1.0 - p)) * I
    E1 = np.sqrt(max(0.0, p)) * X

    return apply_kraus(rho, [E0, E1])


# -------------------------
# Missing functions added:
# -------------------------

def purity(rho):
    val = np.trace(rho @ rho)
    return float(np.real_if_close(val))

def probabilities_from_density(rho):
    p0 = np.real_if_close(rho[0, 0])
    p1 = np.real_if_close(rho[1, 1])
    return float(p0), float(p1)


# -------------------------
# Test Bit Flip Noise
# -------------------------

def test_bit_flip():
    rho = np.array([[1.0, 0.0],
                    [0.0, 0.0]], dtype=complex)

    p = 0.3

    rho_new = apply_bit_flip(rho, p)

    print("Initial Density Matrix (rho):")
    print(rho)

    print("\nDensity Matrix after Bit-Flip Noise with p = {}:".format(p))
    print(rho_new)

    # Probabilities
    p0_before, p1_before = probabilities_from_density(rho)
    p0_after, p1_after = probabilities_from_density(rho_new)

    print("\nProbabilities BEFORE noise:", p0_before, p1_before)
    print("Probabilities AFTER noise:", p0_after, p1_after)

    print("\nPurity BEFORE noise:", purity(rho))
    print("Purity AFTER noise:", purity(rho_new))


# Run test
test_bit_flip()
