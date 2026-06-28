import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# ==========================
# Load node table
# ==========================
df = pd.read_csv(r"Assignment_1\node_table.csv")   # Change filename if needed

# ==========================
# Function to compute gamma
# ==========================
def plot_degree_distribution(degrees, title):
    # Remove zero degrees (cannot take log)
    degrees = degrees[degrees > 0]

    # Count frequency of each degree
    degree_counts = degrees.value_counts().sort_index()

    k = degree_counts.index.values.astype(float)
    Pk = degree_counts.values.astype(float)

    # Normalize frequencies to probabilities
    Pk = Pk / Pk.sum()

    # Log transform
    log_k = np.log10(k)
    log_Pk = np.log10(Pk)

    # Linear regression
    slope, intercept, r_value, p_value, std_err = linregress(log_k, log_Pk)

    gamma = -slope

    # Plot
    plt.figure(figsize=(6,5))
    plt.scatter(log_k, log_Pk, color='blue', label='Data')

    plt.plot(
        log_k,
        intercept + slope*log_k,
        color='red',
        label=f'Fit\nγ = {gamma:.3f}\nR² = {r_value**2:.3f}'
    )

    plt.xlabel('log10(Degree)')
    plt.ylabel('log10(P(k))')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"{title}")
    print(f"Gamma = {gamma:.4f}")
    print(f"Slope = {slope:.4f}")
    print(f"R² = {r_value**2:.4f}")
    print("-"*40)

# ==========================
# In-degree
# ==========================
plot_degree_distribution(df["indegree"], "In-degree Distribution")

# ==========================
# Out-degree
# ==========================
plot_degree_distribution(df["outdegree"], "Out-degree Distribution")