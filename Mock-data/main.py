from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from utils.generator import generate_epoch_data, save_epoch_json
import os

app = FastAPI(title="alldatai API", version="0.1")

# Endpoint raíz
@app.get("/")
def root():
    return {"message": "Welcome to the alldatai API"}

# Endpoint que genera un nuevo archivo JSON
@app.post("/generate")
def generate_data():
    data = generate_epoch_data()
    file_path = save_epoch_json(data)
    return {"status": "success", "file": os.path.basename(file_path)}

# Endpoint que devuelve el último archivo generado
@app.get("/latest")
def get_latest_file():
    data_dir = os.path.join(os.path.dirname(__file__), "data", "epoch")
    if not os.path.exists(data_dir):
        return JSONResponse(status_code=404, content={"error": "No data found"})

    files = sorted(
        [f for f in os.listdir(data_dir) if f.endswith(".json")],
        key=lambda x: os.path.getmtime(os.path.join(data_dir, x)),
        reverse=True,
    )

    if not files:
        return JSONResponse(status_code=404, content={"error": "No JSON files found"})

    latest_file = os.path.join(data_dir, files[0])
    return FileResponse(latest_file)

