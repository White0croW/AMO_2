import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Загрузка предобработанных данных
train_data_scaled = np.loadtxt("processed/train_data_scaled.csv", delimiter=",")

# Создание и обучение модели
model = LinearRegression()
model.fit(train_data_scaled, train_data_scaled)

# Сохранение модели
joblib.dump(model, "model.pkl")
