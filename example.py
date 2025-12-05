from src.core.states import Qubit
from src.superposition.superposition import create_superposition
from src.entanglement.entangle import create_bell_pair
from src.visualization.bloch import plot_bloch_vector

# Real coefficientts

q1 = Qubit(3, 4)

print("Qubit 1 after normalization: ")

print("alpha:", q1.alpha) # Prints normalized alpha value
print("beta:", q1.beta) # Prints normalized beta value

print("Probabilities:", q1.probabilities())

# Check the output of superposition.py file


q1 = create_superposition('0')
print("Superposition from |0>:", q1.alpha, q1.beta)

q2 = create_superposition('1')
print("Superposition from |1>:", q2.alpha, q2.beta)

# Entanglement

State = create_bell_pair()
print("Bell State: ", State)

# Density materix

q = Qubit(3+4j, 1-2j)

rho = q.to_density_matrix()

print(rho)

# Visualization

print("\nPlotting Bloch Sphere for Superposition State |+>: ")
plot_bloch_vector(q1.alpha, q1.beta)