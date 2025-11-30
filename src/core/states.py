import cmath
import numpy as np

class Qubit:
    def __init__(self, alpha, beta):
        self.alpha = complex(alpha)
        self.beta = complex(beta)
        self.normalize()

    def normalize(self):
        magnitude_alpha = abs(self.alpha)
        magnitude_beta = abs(self.beta)
        norm = cmath.sqrt(magnitude_alpha**2 + magnitude_beta**2)

        self.alpha = self.alpha / norm
        self.beta = self.beta / norm

    def probabilities(self):
        return abs(self.alpha)**2, abs(self.beta)**2

    # -------------------------
    # DAY 2: Measurement
    # -------------------------
    def measure(self):
        p0, p1 = self.probabilities()
        rand = np.random.random()

        if rand < p0:
            self.alpha, self.beta = 1, 0
            return 0
        else:
            self.alpha, self.beta = 0, 1
            return 1

    # -------------------------
    # DAY 2: Apply quantum gate
    # -------------------------
    def apply_gate(self, gate_matrix):
        vector = np.array([self.alpha, self.beta])
        new_vector = np.dot(gate_matrix, vector)

        self.alpha = new_vector[0]
        self.beta = new_vector[1]

        self.normalize()

    # -------------------------
    # Tensor Product
    # -------------------------
    def tensor(self, other):
        vec1 = np.array([self.alpha, self.beta])
        vec2 = np.array([other.alpha, other.beta])
        return np.kron(vec1, vec2)
