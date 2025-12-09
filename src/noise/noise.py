# src/noise/noise.py
import numpy as np

def apply_kraus(rho, kraus_list):
    """
    Generic Kraus map:
        rho' = sum_i E_i rho E_i^dagger
    where each E_i is a Kraus operator (matrix).
    """
    out = np.zeros_like(rho, dtype=complex)
    for E in kraus_list:
        out += E @ rho @ E.conj().T
    return out


def apply_phase_damping(rho, gamma):
    """
    Phase damping (pure dephasing) channel with strength gamma in [0,1].
    Kraus operators (single qubit):
        E0 = [[1, 0],
              [0, sqrt(1-gamma)]]
        E1 = [[0, 0],
              [0, sqrt(gamma)]]
    This preserves populations (diagonals) and damps off-diagonals.
    """
    sqrt1mg = np.sqrt(max(0.0, 1.0 - gamma))
    sqrtg = np.sqrt(max(0.0, gamma))

    E0 = np.array([[1.0, 0.0],
                   [0.0, sqrt1mg]], dtype=complex)
    E1 = np.array([[0.0, 0.0],
                   [0.0, sqrtg]], dtype=complex)

    return apply_kraus(rho, [E0, E1])


def apply_bit_flip(rho, p):
    """
    Bit-flip channel with probability p:
        E0 = sqrt(1-p) * I
        E1 = sqrt(p) * X
    X = Pauli-X = [[0,1],[1,0]]
    This flips population between |0> and |1> with prob p.
    """
    I = np.eye(2, dtype=complex)
    X = np.array([[0.0, 1.0],
                  [1.0, 0.0]], dtype=complex)

    E0 = np.sqrt(max(0.0, 1.0 - p)) * I
    E1 = np.sqrt(max(0.0, p)) * X

    return apply_kraus(rho, [E0, E1])

def apply_amplitude_damping(rho, gamma):
    """
    Amplitude damping noise with parameter gamma in [0,1].
    Models energy loss: |1> → |0>.
    
    Kraus operators:
        E0 = [[1, 0],
              [0, sqrt(1-gamma)]]

        E1 = [[0, sqrt(gamma)],
              [0, 0]]
    """

    sqrt1mg = np.sqrt(max(0.0, 1.0 - gamma))
    sqrtg = np.sqrt(max(0.0, gamma))

    E0 = np.array([[1.0, 0.0],
                   [0.0, sqrt1mg]], dtype=complex)

    E1 = np.array([[0.0, sqrtg],
                   [0.0, 0.0]], dtype=complex)

    return apply_kraus(rho, [E0, E1])



def purity(rho):
    """
    Purity = Tr(rho^2). For pure states purity==1. For mixed states purity<1.
    Real number returned.
    """
    val = np.trace(rho @ rho)
    return float(np.real_if_close(val))


def probabilities_from_density(rho):
    """
    Read probabilities of measuring |0> and |1> from density matrix:
      P(0) = rho[0,0], P(1) = rho[1,1]
    Return as two python floats.
    """
    p0 = np.real_if_close(rho[0, 0])
    p1 = np.real_if_close(rho[1, 1])
    return float(p0), float(p1)
