import json
import os
import random
import uuid
from datetime import datetime

# Ruta donde se guardarán los archivos
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "epoch")

def generate_epoch_data():
    """Genera un dataset simulado tipo Garmin (epoch)"""
    return {
        "userId": "user_001",
        "timestamp": datetime.utcnow().isoformat(),
        "epochId": str(uuid.uuid4()),
        "heartRate": random.randint(60, 160),
        "steps": random.randint(0, 200),
        "stressLevel": random.randint(0, 100),
        "calories": round(random.uniform(0.5, 3.0), 2),
        "activityType": random.choice(["rest", "walk", "run", "cycle"])
    }

def save_epoch_json(data):
    """Guarda el archivo JSON con un nombre único"""
    os.makedirs(DATA_PATH, exist_ok=True)
    file_name = f"epoch_{data['epochId']}.json"
    file_path = os.path.join(DATA_PATH, file_name)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return file_path

