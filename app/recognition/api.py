import os
import shutil
import tempfile
import uuid
from fastapi import APIRouter, File, UploadFile, BackgroundTasks
from app.ml.src.predictor import Predictor

router = APIRouter()
predictor = Predictor()

# Dictionary to store the processing status and result
tasks = {}
# Variable to store the last uploaded task ID
last_task_id = None

def process_file(task_id: str, file_path: str):
    """Background task to process the file."""
    result = predictor(file_path)
    tasks[task_id]['status'] = 'completed'
    tasks[task_id]['result'] = result
    os.remove(file_path)  # Cleanup after processing

@router.post("/upload")
async def upload_voice(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    global last_task_id

    temp_file_path = f"/tmp/{file.filename}"

    with open(temp_file_path, "wb") as temp_file:
        shutil.copyfileobj(file.file, temp_file)

    task_id = str(uuid.uuid4())
    tasks[task_id] = {'status': 'processing', 'result': None}
    
    last_task_id = task_id

    background_tasks.add_task(process_file, task_id, temp_file_path)

    return {"task_id": task_id}


@router.get("/status")
async def status():
    if not last_task_id or last_task_id not in tasks:
        return {"error": "No recent tasks available"}

    task_info = tasks[last_task_id]
    return {"status": task_info['status'], "result": task_info['result']}
