# Adaptive Wi-Fi Bandwidth Allocation System

## Project Overview

This project demonstrates how rational functions and
mathematical algorithms can be used to simulate
adaptive Wi-Fi bandwidth allocation.

The system distributes limited bandwidth among
students according to their individual demands
and priority weights.

The project is a mathematical simulation and does
not control an actual Wi-Fi network.

## Mathematical Model

### 1. Equal Allocation

B(n) = B_T / n

Where:

- B_T = Total available bandwidth
- n = Number of connected students
- B(n) = Equal bandwidth share per student

### 2. Weighted Allocation

B_i = (w_i / Σw_j) × B_T

Where:

- B_i = Bandwidth allocated to student i
- w_i = Priority weight of student i
- Σw_j = Sum of priority weights

### 3. Demand-Aware Allocation

The algorithm considers each student's bandwidth
demand and redistributes unused capacity.

The allocation must satisfy:

- Total allocation <= Total capacity
- Individual allocation <= Individual demand
- Allocations >= 0

## Project Files

| File | Description |
|------|-------------|
| allocator.py | Core mathematical allocation algorithm |
| demo.py | Three-student bandwidth experiment |
| simulation.py | Dynamic 30-student network simulation |
| test_allocator.py | Automated mathematical tests |
| requirements.txt | Python dependencies |
| README.md | Project documentation |

## Running the Project

Install the required library:

```bash
pip install -r requirements.txt
```

Run the basic experiment:

```bash
python demo.py
```

Run the dynamic simulation:

```bash
python simulation.py
```

Run the automated tests:

```bash
python -m unittest -v test_allocator.py
```

## Experimental Example

Total bandwidth: 100 Mbps

Student demands:

- Student 1: 10 Mbps
- Student 2: 30 Mbps
- Student 3: 80 Mbps

Adaptive allocations:

- Student 1: 10 Mbps
- Student 2: 30 Mbps
- Student 3: 60 Mbps

Total allocated bandwidth: 100 Mbps

## Limitations

This project uses simulated student demands.

It does not measure actual network traffic or
enforce bandwidth limits on a router.

The fixed equal model represents rigid bandwidth
limits without redistribution. It is not intended
to represent every conventional network scheduler.

## Educational Purpose

This project was developed to demonstrate the
application of rational functions, proportional
relationships, mathematical constraints, and
computational simulation to resource allocation.
