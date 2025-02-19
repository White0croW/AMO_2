import numpy as np
import os

# Создаем папки для данных
os.makedirs("train", exist_ok=True)
os.makedirs("test", exist_ok=True)

# Генерация данных
np.random.seed(0)

# Создаем тренировочные данные
train_data = np.linspace(0, 100, 100) + np.random.normal(0, 5, 100)
np.savetxt("train/train_data.csv", train_data, delimiter=",")

# Создаем тестовые данные с аномалиями
test_data = np.linspace(0, 100, 50) + np.random.normal(0, 5, 50)
test_data[::10] += np.random.normal(0, 20, 5)  # Добавляем аномалии
np.savetxt("test/test_data.csv", test_data, delimiter=",")
