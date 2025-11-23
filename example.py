from src.core.states import Qubit

# Real coefficientts

q1 = Qubit(3, 4)

print("Qubit 1 after normalization: ")

print("alpha:", q1.alpha) # Prints normalized alpha value
print("beta:", q1.beta) # Prints normalized beta value

print("Probabilities:", q1.probabilities())