#!/bin/bash
set -x

# Запуск скрипта генерации данных
python data_generation.py

# Запуск скрипта предобработки данных
python model_preprocessing.py

# Запуск скрипта обучения модели
python model_training.py

# Запуск скрипта тестирования модели
python model_testing.py
