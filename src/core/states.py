import cmath 

class Qubit:
    def __init__(self, alpha, beta):
        self.alpha = complex(alpha)
        self.beta = complex(beta)
        self.normalize() # abs(self.alpha) / norm and abs(self.beta) / norm
        
    # Define normalization function
    
    def normalize(self):
        magnitude_alpha = abs(self.alpha)
        magnitude_beta = abs(self.beta)
        norm = cmath.sqrt(magnitude_alpha**2 + magnitude_beta**2)
        
        self.alpha = self.alpha / norm
        self.beta = self.beta / norm
        
    # Add a method to set probabilities
    
    def probabilities(self):
        return abs(self.alpha)**2, abs(self.beta)**2
    
    
        
   # MEASUREMENT (DAY 2)

# --------------------------------------------------  
def measure(self):  
    """  
    Collapses the qubit to |0⟩ or |1⟩ based on probabilities.  
    """  
    p0, p1 = self.probabilities()  
    rand = np.random.random()  

    if rand < p0:  
        # Collapse to |0⟩  
        self.alpha, self.beta = 1, 0  
        return 0  
    else:  
        # Collapse to |1⟩  
        self.alpha, self.beta = 0, 1  
        return 1  

# --------------------------------------------------  
# APPLY A QUANTUM GATE (DAY 2)  
# --------------------------------------------------  
def apply_gate(self, gate_matrix):  
    """  
    Applies a 2×2 quantum gate to the qubit.  
    """  
    vector = np.array([self.alpha, self.beta])  
    new_vector = np.dot(gate_matrix, vector)  

    self.alpha = new_vector[0]  
    self.beta = new_vector[1]  

    # Re-normalize (very important)  
    self.normalize()  

# --------------------------------------------------  
# TENSOR PRODUCT (DAY 2 → used in entangle.py)  
# --------------------------------------------------  
def tensor(self, other):  
    """  
    Returns the 4D state vector of 2 qubits using tensor/Kronecker product.  
    """  
    vec1 = np.array([self.alpha, self.beta])  
    vec2 = np.array([other.alpha, other.beta])  

    return np.kron(vec1, vec2)