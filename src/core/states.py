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
        
