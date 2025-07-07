import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load training data
train_data = pd.read_csv('train.csv', header=None)
X_train = train_data.iloc[:, :500].values  # Stock prices
y_train = train_data.iloc[:, 500].values   # S&P 500 index values

# Load test data
test_data = pd.read_csv('test.csv', header=None)
X_test = test_data.values  # Stock prices

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Save predictions to prediction.csv
np.savetxt('prediction.csv', predictions, delimiter=',', fmt='%.8f')
