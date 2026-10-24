"""
Adaptive Wi-Fi Bandwidth Allocation System

This module implements:
1. Fixed equal bandwidth allocation
2. Demand-aware weighted bandwidth allocation
3. Redistribution of unused bandwidth
"""


def allocate(capacity, demands, weights):
    """
    Allocate bandwidth using weighted max-min fairness.

    Parameters:
        capacity: Total available bandwidth in Mbps
        demands: List of student bandwidth demands
        weights: List of student priority weights

    Returns:
        List of allocated bandwidth values
    """

    if capacity < 0:
        raise ValueError("Capacity must be nonnegative.")

    if len(demands) != len(weights):
        raise ValueError("Demands and weights must match.")

    if any(d < 0 for d in demands):
        raise ValueError("Demands cannot be negative.")

    if any(w <= 0 for w in weights):
        raise ValueError("Weights must be positive.")

    allocations = [0.0] * len(demands)

    active = {
        i for i, demand in enumerate(demands)
        if demand > 0
    }

    remaining = float(capacity)

    while active and remaining > 1e-9:

        total_weight = sum(
            weights[i] for i in active
        )

        shares = {
            i: remaining * weights[i] / total_weight
            for i in active
        }

        satisfied = {
            i for i in active
            if demands[i] - allocations[i] <= shares[i]
        }

        if not satisfied:
            for i in active:
                allocations[i] += shares[i]

            break

        for i in satisfied:
            needed = demands[i] - allocations[i]

            allocations[i] += needed
            remaining -= needed

        active -= satisfied

    return allocations


def fixed_equal(capacity, demands):
    """
    Allocate bandwidth using fixed equal limits.
    Unused shares are not redistributed.
    """

    if capacity < 0:
        raise ValueError("Capacity must be nonnegative.")

    if any(d < 0 for d in demands):
        raise ValueError("Demands cannot be negative.")

    if not demands:
        return []

    equal_share = capacity / len(demands)

    return [
        min(demand, equal_share)
        for demand in demands
    ]
