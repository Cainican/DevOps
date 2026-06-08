import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

# Example data: Login attempts with features like time of day, IP address, and failed attempts
data = pd.DataFrame({
  # Hours of login attempts
  'time_of_day': [12, 14, 3, 18, 24, 9, 23, 2, 6, 17],

  # Number of failed attempts
  'failed_attempts': [0, 1, 2, 0, 3, 1, 5, 0, 1],

  # 1 = syccess, 0 = failure
  'success': [1, 1, 0, 1, 0, 1, 1, 0, 1, 1]
})

# Split data for model training
# Features
X = data[['time_of_day', 'failed_attempts']]

# Target (success or failure)
y = data['successful']

# Train an anomaly detection model (Isolation Forest)
# Assume 10% of data could be anomalous
model = IsolationForest(contamination=0.1)
model.fit(X)

# Predict anomlies (anomalies = -1, normal = 1)
anomalies = model.predict(X)

# Add predictions to the data
data['anomaly'] = anomalies

# Display results
print(data)