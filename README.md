
---

# **Quantum State Simulation & Decoherence Engine**

### *A Physics-Driven, Mathematics-First Quantum Computing Simulator Built Entirely From Scratch*

---

## 🚀 **Project Overview**

This project is a **fully custom quantum simulation engine**, implemented **from first principles** using only:

* Complex numbers
* Linear algebra
* Quantum mechanics equations
* NumPy for raw matrix math

No Qiskit.
No QuTiP.
No shortcuts.

Every part of the quantum behavior — superposition, measurement, entanglement, density matrices, noise, and Bloch sphere visualization — is manually derived and implemented.

The goal is to gain **true mastery** of quantum information science by coding the physics itself.

---

# 🎯 **What This Simulator Can Do**

### ✔ Build and manipulate qubits using raw mathematics

### ✔ Apply real quantum gates (Hadamard, Pauli, CNOT)

### ✔ Generate superposition states manually

### ✔ Create Bell-pair entanglement using tensor products

### ✔ Convert state vectors to density matrices

### ✔ Apply Kraus-operator based noise (decoherence)

### ✔ Visualize qubit states on a Bloch sphere

### ✔ Track purity and coherence loss during noise

This framework is designed as a foundation for advanced quantum algorithms and research in decoherence.

---

# ⚙️ **Core Components**

## 🔹 1. **Qubit Engine (`states.py`)**

Implements the essential behavior of a quantum bit:

* Complex amplitudes (alpha, beta)
* Automatic normalization
* Probability calculations
* Measurement collapse
* Matrix-based gate application
* Tensor product for multi-qubit states

This is the mathematical heart of the simulator.

---

## 🔹 2. **Quantum Gates (`gates.py`)**

Fully manual gate matrices:

* **Hadamard (H)** – Creates superposition
* **Pauli X / Y / Z** – Bit flips & phase flips
* **Identity (I)**
* **CNOT** – Enables entanglement

All gates are implemented as 2×2 or 4×4 **unitary matrices**.

---

## 🔹 3. **Superposition Module (`superposition.py`)**

Generates:

* |+> = (|0> + |1>) / sqrt(2)
* |-> = (|0> – |1>) / sqrt(2)

By applying the Hadamard matrix directly to basis states.

---

## 🔹 4. **Entanglement Module (`entangle.py`)**

Builds 2-qubit Bell States using:

1. Superposition on the first qubit
2. Tensor product expansion
3. CNOT gate

Supports all standard Bell states:

* (00 + 11)
