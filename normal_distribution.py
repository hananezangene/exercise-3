import numpy as np
import matplotlib.pyplot as plt

def plot_normal_dist(n, mean=0, std=1):
    # Generate random numbers from normal distribution
    data = np.random.normal(mean, std, n)
    
    # Create histogram
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=100, density=True, alpha=0.7, color='skyblue')
    plt.title(f'Normal Distribution Histogram (n={n})')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.grid(True, alpha=0.3)
    plt.show()

# Plot for different n values
plot_normal_dist(10)
plot_normal_dist(1000)
plot_normal_dist(100000)