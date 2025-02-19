import numpy as np
from sklearn.preprocessing import StandardScaler
import os

# Загрузка данных
train_data = np.loadtxt("train/train_data.csv", delimiter=",")
test_data = np.loadtxt("test/test_data.csv", delimiter=",")

# Предобработка данных
scaler = StandardScaler()
train_data_scaled = scaler.fit_transform(train_data.reshape(-1, 1))
test_data_scaled = scaler.transform(test_data.reshape(-1, 1))

# Сохранение предобработанных данных
os.makedirs("processed", exist_ok=True)
np.savetxt("processed/train_data_scaled.csv", train_data_scaled, delimiter=",")
np.savetxt("processed/test_data_scaled.csv", test_data_scaled, delimiter=",")
