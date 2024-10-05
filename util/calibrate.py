import numpy as np


def calibrate(
    losses,
    candidate_thresholds,
    num_samples=13368,
    delta=0.05,
    epsilon=0.05,
):
    """
    Implements Algorithm 1 for calibrating CALM with δ, ε tolerance levels.

    Parameters:
    - losses: list of losses for each threshold (Li for textual or risk consistency)
    - delta: global consistency tolerance level
    - epsilon: tolerance level for p-value
    - candidate_thresholds: list of candidate thresholds λ (in descending order)

    Returns:
    - λ_min: minimum threshold that satisfies the tolerance
    """
    # Initialize λ_min to 1 as per the pseudocode
    lambda_min = 1
    # Iterate over each candidate threshold λ in decreasing order
    for i, lambda_j in enumerate(candidate_thresholds):
        # Estimate the expectation of the loss E_hat(λ_j)
        E_hat_lambda_j = (
            40.8814 - losses[i]
        ) / 100  # Assuming `losses` is a dict mapping λ to loss values

        # Compute the p-value based on Hoeffding's inequality
        p_j = np.exp(-2 * num_samples * (max(0, delta - E_hat_lambda_j)) ** 2)

        # If p_j exceeds the tolerance ε, update and return λ_min
        if p_j > epsilon:
            print("a")
            return lambda_min
        lambda_min = lambda_j

    # Return the minimum λ
    return lambda_min


# Calibrating early using the algorithm
lambda_min = calibrate(
    losses=[40.2458, 40.0091, 39.7386, 39.237, 38.6828, 37.8713],
    candidate_thresholds=[0.9, 0.8, 0.7, 0.6, 0.5, 0.4],
)
print(f"Calibrated λ_min for early: {lambda_min}")

# Calibrating early using the algorithm
lambda_min = calibrate(
    losses=[40.151, 40.0149, 39.5224, 39.1374, 38.4574, 37.7045],
    candidate_thresholds=[0.9, 0.8, 0.7, 0.6, 0.5, 0.4],
)
print(f"Calibrated λ_min for 3_6: {lambda_min}")
