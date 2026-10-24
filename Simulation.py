"""
Dynamic Wi-Fi Bandwidth Allocation Simulation

Simulates:
- Students joining the network
- Students leaving the network
- Changing bandwidth demands
- Adaptive bandwidth allocation
- Fixed equal allocation
- Network utilization
"""

import random
import matplotlib.pyplot as plt

from allocator import allocate, fixed_equal


# Network settings

TOTAL_BANDWIDTH = 100

MAX_STUDENTS = 30

SIMULATION_TIME = 60

random.seed(42)


# Store simulation results

time_steps = []

active_students_history = []

total_demand_history = []

adaptive_utilization_history = []

equal_utilization_history = []


# Initially connected students

students = {}

for i in range(15):

    students[i] = random.uniform(1, 10)


# Run simulation

for t in range(SIMULATION_TIME):

    # Randomly disconnect students

    for student in list(students.keys()):

        if random.random() < 0.05:

            del students[student]


    # Randomly connect students

    for student in range(MAX_STUDENTS):

        if student not in students:

            if random.random() < 0.08:

                students[student] = random.uniform(1, 10)


    # Update bandwidth demands

    for student in students:

        students[student] = random.uniform(1, 15)


    # Prepare allocation inputs

    demands = list(students.values())

    weights = [1] * len(demands)


    # Calculate bandwidth allocations

    adaptive = allocate(
        TOTAL_BANDWIDTH,
        demands,
        weights
    )

    equal = fixed_equal(
        TOTAL_BANDWIDTH,
        demands
    )


    # Calculate utilization

    adaptive_utilization = (
        sum(adaptive) / TOTAL_BANDWIDTH
    ) * 100

    equal_utilization = (
        sum(equal) / TOTAL_BANDWIDTH
    ) * 100


    # Store results

    time_steps.append(t)

    active_students_history.append(
        len(students)
    )

    total_demand_history.append(
        sum(demands)
    )

    adaptive_utilization_history.append(
        adaptive_utilization
    )

    equal_utilization_history.append(
        equal_utilization
    )


print("Simulation completed successfully!")


# Graph 1: Connected students

plt.figure(figsize=(10, 5))

plt.plot(
    time_steps,
    active_students_history
)

plt.xlabel("Simulation Time Step")

plt.ylabel("Connected Students")

plt.title("Number of Students Connected to Wi-Fi")

plt.grid(True)

plt.show()


# Graph 2: Total bandwidth demand

plt.figure(figsize=(10, 5))

plt.plot(
    time_steps,
    total_demand_history,
    label="Total Demand"
)

plt.axhline(
    y=TOTAL_BANDWIDTH,
    linestyle="--",
    label="Available Bandwidth"
)

plt.xlabel("Simulation Time Step")

plt.ylabel("Bandwidth (Mbps)")

plt.title("Network Demand vs Available Bandwidth")

plt.legend()

plt.grid(True)

plt.show()


# Graph 3: Allocation comparison

plt.figure(figsize=(10, 5))

plt.plot(
    time_steps,
    adaptive_utilization_history,
    label="Adaptive Allocation"
)

plt.plot(
    time_steps,
    equal_utilization_history,
    label="Fixed Equal Allocation"
)

plt.xlabel("Simulation Time Step")

plt.ylabel("Bandwidth Utilization (%)")

plt.title("Adaptive vs Fixed Equal Bandwidth Allocation")

plt.legend()

plt.grid(True)

plt.show()


# Final statistics

average_adaptive = (
    sum(adaptive_utilization_history)
    / SIMULATION_TIME
)

average_equal = (
    sum(equal_utilization_history)
    / SIMULATION_TIME
)


print("\n=== SIMULATION RESULTS ===")

print(
    f"Average Adaptive Utilization: "
    f"{average_adaptive:.2f}%"
)

print(
    f"Average Fixed Equal Utilization: "
    f"{average_equal:.2f}%"
)

print(
    f"Utilization Difference: "
    f"{average_adaptive - average_equal:.2f} percentage points"
)
