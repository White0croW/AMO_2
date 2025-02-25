#!/bin/bash
set -x

# Activate the virtual environment
source venv/Scripts/activate

# Install dependencies if not already installed
pip install -r requirements.txt

# Run the data generation script
python data_generation.py

# Run the data preprocessing script
python model_preprocessing.py

# Run the model training script
python model_training.py

# Run the model testing script
python model_testing.py

# Deactivate the virtual environment
deactivate