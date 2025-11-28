
# Day: 1

# Quantum State Simulation & Decoherence Effect

## Overview

This project simulates quantum states and explores the effect of decoherence on qubits. It allows users to:

* Create and normalize qubits
* Compute probabilities of measurement outcomes
* Simulate quantum behavior interactively

This repository is designed for learning and experimentation with quantum computing concepts using Python.

## Features

* **Manual Qubit Creation:** Users can create a qubit with complex amplitudes (\alpha) and (\beta).
* **Normalization:** Qubits are automatically normalized to ensure valid quantum states.
* **Probability Calculation:** Calculate the probabilities of measuring `0` or `1` for a given qubit.
* **Interactive Notebook:** Fully interactive Jupyter notebook for experimentation and visualization.
* **Version Control Ready:** Compatible with Git and GitHub for project tracking and sharing.

## Getting Started

### Prerequisites

* Python 3.x
* Libraries: `numpy`, `matplotlib`, `qutip`, `ipywidgets`, `pandas`

You can install required libraries using:

```bash
pip install numpy matplotlib qutip ipywidgets pandas
```

### Usage

1. Clone the repository:

```bash
git clone <repository-link>
```

2. Navigate to the project directory:

```bash
cd quantum-state-simulation
```

3. Open the Jupyter notebook:

```bash
jupyter notebook Quantum_Simulation.ipynb
```

4. Explore the notebook to create qubits, normalize them, and simulate measurement probabilities.

## Example

```python
import numpy as np

def manual_qubit(alpha, beta):
    vec = np.array([alpha, beta], dtype=complex)
    return vec / np.linalg.norm(vec)

# Example
alpha = 1 + 0j
beta = 1 + 0j
qubit = manual_qubit(alpha, beta)
print("Normalized Qubit:", qubit)
```

Output:

```
Normalized Qubit: [0.70710678+0.j 0.70710678+0.j]
```

## Contributing

Feel free to fork this repository, add new features, improve code, or fix bugs. Pull requests are welcome!

## License

This project is open source and available under the MIT License.

---

