"""
Basic Bandwidth Allocation Experiment

Compares fixed equal allocation with
adaptive bandwidth allocation.
"""

from allocator import allocate, fixed_equal


capacity = 100

demands = [10, 30, 80]

weights = [1, 1, 1]


equal = fixed_equal(
    capacity,
    demands
)

adaptive = allocate(
    capacity,
    demands,
    weights
)


print("=== WI-FI BANDWIDTH ALLOCATION ===")

print(f"\nTotal Capacity: {capacity} Mbps")

print("\nStudent Results:")

for i in range(len(demands)):

    print(f"\nStudent {i+1}")

    print(f"Demand: {demands[i]} Mbps")

    print(
        f"Fixed Equal: {equal[i]:.2f} Mbps"
    )

    print(
        f"Adaptive: {adaptive[i]:.2f} Mbps"
    )


equal_utilization = (
    sum(equal) / capacity
) * 100

adaptive_utilization = (
    sum(adaptive) / capacity
) * 100


print("\n=== NETWORK UTILIZATION ===")

print(
    f"Fixed Equal: {equal_utilization:.2f}%"
)

print(
    f"Adaptive: {adaptive_utilization:.2f}%"
)
