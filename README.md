
---

# ⚛️ Quantum State Simulation & Decoherence Engine

### A Python-Based Quantum Computing Simulator for Research & Learning

---

## 🚀 **Project Overview**

This project is a custom-built **Quantum State Simulation Engine** designed to model the fundamental behavior of qubits, quantum gates, superposition, measurement, and multi-qubit systems.

The simulator focuses on:

* Mathematical accuracy
* Clean modular design
* Ease of extension
* Realistic quantum-mechanical behavior
* Future integration of decoherence and noise models

This repository aims to serve as a learning tool, a research foundation, and a stepping stone toward building a **full quantum computing framework**.

---

## 🎯 **Project Goals**

### ✔ Build a fully functional Python quantum simulator

Capable of creating and manipulating quantum states using linear algebra and complex vector math.

### ✔ Simulate real quantum behavior

Including normalization, probability distributions, collapse, unitary gates, and tensor products.

### ✔ Provide a modular framework

Allowing new gates, algorithms, and decoherence models to be added easily.

### ✔ Enable students & developers to experiment

By offering clean, understandable examples and expanding code structure.

### ✔ Lay the groundwork for advanced features

Such as:

* Quantum circuits
* Decoherence
* Noise models (Depolarizing channel, Phase damping)
* Entanglement operations
* Quantum teleportation
* Grover’s algorithm
* Machine-learning-based quantum state analysis

---

## ⚙️ **Features**

### 🔹 **Qubit Class (Core Engine)**

* Supports complex amplitudes
* Automatically normalizes state vectors
* Calculates measurement probabilities
* Performs state collapse based on true quantum randomness
* Applies any 2×2 unitary quantum gate
* Supports tensor (Kronecker) product for multi-qubit systems

### 🔹 **Quantum Gates Implemented**

* **Hadamard Gate (H)** – Creates superposition
* **Pauli-X Gate (NOT Gate)** – Bit flip
* **Pauli-Y Gate** – Flip + Phase shift
* **Pauli-Z Gate** – Phase flip

Designed for future expansion into:

* Controlled gates (CNOT, CZ)
* Rotation gates (Rx, Ry, Rz)
* Custom unitary operations

### 🔹 **Superposition Module**

Easily generate:

* |+⟩ state
* |−⟩ state

Using the Hadamard transformation on |0⟩ or |1⟩.

### 🔹 **Measurement Engine**

Simulates real quantum measurement:

* Random number generation
* Collapse based on amplitude probabilities
* Irreversible state reduction

### 🔹 **Tensor Product Engine**

Constructs multi-qubit state vectors for entanglement and circuit building.

---

## 📁 **Project Structure**

```
Quantum_Simulator/
│
├── example.py
├── README.md
│
├── src/
│   ├── core/
│   │   └── states.py          # Qubit class: normalization, measurement, gates
│   │
│   ├── gates/
│   │   └── gates.py           # Pauli, Hadamard, and future gates
│   │
│   ├── superposition/
│   │   └── superposition.py   # Superposition generation utilities
│
└── requirements.txt           # Dependencies (optional)
```

---

## 🛠️ **Installation**

```
pip install numpy
```

---

## ▶️ **How to Use**

### **1. Creating and normalizing a qubit**

```python
from src.core.states import Qubit

q = Qubit(3, 4)
print(q.alpha, q.beta)
print(q.probabilities())
```

---

### **2. Creating superposition**

```python
from src.superposition.superposition import create_superposition

q0 = create_superposition('0')
q1 = create_superposition('1')

print(q0.alpha, q0.beta)
print(q1.alpha, q1.beta)
```

---

### **3. Applying quantum gates**

```python
from src.gates.gates import H, X, Y, Z

q.apply_gate(H)
print(q.alpha, q.beta)
```

---

### **4. Measurement (Quantum Collapse)**

```python
result = q.measure()
print("Measured:", result)
print("State:", q.alpha, q.beta)
```

---

### **5. Tensor product (Multi-Qubit States)**

```python
q1 = Qubit(1, 0)
q2 = Qubit(0, 1)

system = q1.tensor(q2)
print(system)
```

---

## 🧠 **Mathematical Foundations**

### ✔ Qubit Representation

[
|\psi⟩ = \alpha |0⟩ + \beta |1⟩,\quad |\alpha|^2 + |\beta|^2 = 1
]

### ✔ Normalization

[
(\alpha, \beta) \rightarrow
\left( \frac{\alpha}{\sqrt{|\alpha|^2 + |\beta|^2}},;
\frac{\beta}{\sqrt{|\alpha|^2 + |\beta|^2}} \right)
]

### ✔ Quantum Gates

All gates are implemented as unitary matrices:

[
|\psi'⟩ = U |\psi⟩
]

### ✔ Measurement & Collapse

[
P(0) = |\alpha|^2,\quad P(1) = |\beta|^2
]

State collapses to basis vector depending on probability.

### ✔ Tensor Product

[
|\psi⟩ \otimes |\phi⟩ = \text{kron}([\alpha,\beta], [\gamma,\delta])
]

---

## 🌌 **Future Scope**

This simulator is being developed toward a full educational quantum engine, including:

* Quantum Circuits
* Multi-Gate Pipelines
* Decoherence Models
* Quantum Entanglement
* Visualization (Bloch Sphere)
* Quantum Fourier Transform
* Grover’s Algorithm
* Machine-Learning-driven quantum state prediction

---

## 🤝 **Contributing**

Contributions, optimizations, gate implementations, and new modules are welcome!
Feel free to open pull requests or issues.

---

## 📜 License

MIT License — open and free for educational and research use.

---

