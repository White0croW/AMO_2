#!/bin/bash
python3 -m venv venv  # Создаем виртуальное окружение
source venv/bin/activate  # Активируем его
pip install -r AMO_2/requirments.txt

echo "---- 1. Генерация данных ----"
python3 AMO_2/data_generation.py || { echo "Ошибка генерации данных" >&2; exit 1; }

echo "---- 2. Предобработка данных ----"
python3 AMO_2/model_preprocessing.py || { echo "Ошибка предобработки" >&2; exit 1; }

echo "---- 3. Обучение модели ----"
python3 AMO_2/model_training.py || { echo "Ошибка обучения" >&2; exit 1; }

echo "---- 4. Тестирование модели ----"
python3 AMO_2/model_testing.py || { echo "Ошибка тестирования" >&2; exit 1; }

echo "Конвейер успешно завершен!"

# Deactivate the virtual environment
deactivate
