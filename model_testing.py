import numpy as np
import joblib
from sklearn.metrics import mean_squared_error

# Загрузка модели
model = joblib.load("model.pkl")

# Загрузка предобработанных тестовых данных
test_data_scaled = np.loadtxt("processed/test_data_scaled.csv", delimiter=",")
test_data_scaled = test_data_scaled.reshape(-1, 1)

# Прогнозирование
predictions = model.predict(test_data_scaled)

# Оценка модели
mse = mean_squared_error(test_data_scaled, predictions)
print(f"Mean Squared Error: {mse}")
