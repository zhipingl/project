import numpy as np
import pandas as pd

# Set the seed to make the results reproducible
np.random.seed(123)

# Set the number of samples and features
n_samples = 1000
n_features = 10

# Generate random data
X = np.random.randn(n_samples, n_features)
y = np.random.randint(0, 2, n_samples)

# Convert to pandas DataFrame and save to CSV
df = pd.DataFrame(np.column_stack([X, y]), columns=[f"feature_{i+1}" for i in range(n_features)] + ["target"])
df.to_csv("dataset.csv", index=False)