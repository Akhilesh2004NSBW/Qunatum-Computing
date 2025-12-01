
---

⚛️ Quantum State Simulation & Decoherence Engine

A Mathematical, Physics-Driven Quantum Computing Simulator Built Entirely From Scratch


---

🚀 Project Overview

This repository contains a pure Python, mathematics-driven quantum simulator, built from first principles without relying on high-level quantum toolkits such as Qiskit, QuTiP, or Cirq.

The goal is to deeply understand:

How qubits behave mathematically

How quantum gates transform states

How superposition and entanglement are formed

How tensor products expand Hilbert space

How measurement collapses a quantum state

How a full quantum circuit simulator can be built manually


This project is being developed as a research-grade foundation for advanced quantum simulation, decoherence modeling, and quantum-enhanced machine learning.


---

🎯 Project Goals

✔ Build a fully functional low-level quantum simulator

Using only NumPy, complex numbers, and linear algebra.

✔ Implement quantum behavior mathematically

Not using shortcuts, not importing pre-built libraries.

✔ Create a modular, extensible engine

Where new gates, circuits, and algorithms can be added easily.

✔ Enable deep learning of quantum mechanics

By coding the physics manually, line by line.

✔ Prepare for advanced capabilities

Future stages will include:

Decoherence & noise channels

Density matrix simulation

Bloch sphere visualization

Quantum circuits

Bell state generation

Quantum teleportation

Grover’s algorithm

QML-based analysis



---

⚙️ Core Features

🔹 1. Qubit Engine (states.py)

Implements the fundamental mathematical behavior of a qubit:

Complex amplitude representation

Automatic normalization

Measurement collapse using genuine quantum probability

Unitary gate application (2×2 matrices)

Tensor (Kronecker) product for multi-qubit systems


Mathematically, a qubit is represented as:

|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1

You implement this manually using NumPy.


---

🔹 2. Quantum Gates (gates.py)

Implemented:

Hadamard (H) – Creates superposition

Pauli-X (NOT)

Pauli-Y

Pauli-Z

Identity (I)

CNOT Gate (for entanglement)


Each gate is represented as a unitary matrix, implemented directly using linear algebra—not pre-built functions.


---

🔹 3. Superposition Module (superposition.py)

Creates:

|+⟩ = (|0⟩ + |1⟩)/√2

|−⟩ = (|0⟩ − |1⟩)/√2


Using the Hadamard transform on |0⟩ or |1⟩.

This demonstrates how quantum amplitudes work mathematically.


---

🔹 4. Entanglement Module (entangle.py)

(Added Recently — Day 3 Update)

Implements true Bell State generation using:

1. Superposition on the first qubit


2. Tensor product


3. CNOT application



Generates states such as:

|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}

|\Psi^+\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}}

Depending on the control and target configuration.

This is the strongest form of entanglement in quantum mechanics.


---

📁 Project Structure

Quantum_Simulator/
│
├── example.py                 # Demonstrates usage of all modules
├── README.md
│
├── src/
│   ├── core/
│   │   └── states.py          # Qubit: normalization, measurement, gates
│   │
│   ├── gates/
│   │   └── gates.py           # Hadamard, Pauli gates, CNOT (unitary logic)
│   │
│   ├── superposition/
│   │   └── superposition.py   # |+> and |-> generation
│   │
│   ├── entanglement/
│   │   └── entangle.py        # Bell state generation (Day 3)
│
└── requirements.txt


---

🛠️ Installation

pip install numpy


---

▶️ How to Use

1. Create and normalize a qubit

from src.core.states import Qubit

q = Qubit(3, 4)
print(q.alpha, q.beta)
print(q.probabilities())


---

2. Superposition

from src.superposition.superposition import create_superposition

q0 = create_superposition('0')
q1 = create_superposition('1')


---

3. Apply quantum gates

from src.gates.gates import H, X

q.apply_gate(H)


---

4. Measure a qubit

result = q.measure()
print(result)


---

5. Tensor product

q1 = Qubit(1, 0)
q2 = Qubit(0, 1)

multi = q1.tensor(q2)
print(multi)


---

6. Entanglement (Bell State)

from src.entanglement.entangle import create_bell_pair

state = create_bell_pair()
print(state)


---

🧠 Mathematical Foundations

✔ Linear algebra

✔ Complex numbers

✔ 2D → 4D Hilbert space expansion

✔ Unitary transformations

✔ Measurement postulates

✔ Tensor product

✔ Bell state generation

This simulator is built on pure quantum mechanics, not shortcuts.


---

🌌 Future Scope

The long-term vision:

Quantum circuits

Multi-qubit gate pipelines

Phase damping & decoherence

Density matrices

Bloch sphere visualization

Quantum Fourier Transform

Quantum Teleportation

Grover’s Algorithm

Variational Quantum Machine Learning (VQML)



---

🤝 Contributing

Contributions are welcome!
Feel free to submit pull requests for:

New gates

Optimization

Circuit implementation

Noise models

Visualizations



---

📜 License

MIT License — free for research, education, and development.


---

