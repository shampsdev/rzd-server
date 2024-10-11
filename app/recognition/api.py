import os
import shutil
import tempfile
from fastapi import APIRouter, File, UploadFile

from app.ml.src.predictor import Predictor

router = APIRouter()

@router.post('/upload')
async def upload_voice(file: UploadFile = File(...)):
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_file_path = os.path.join(tmpdir, file.filename)
        
        with open(temp_file_path, "wb") as temp_file:
            shutil.copyfileobj(file.file, temp_file)
            
        predictor = Predictor()
        
        result = predictor(temp_file_path)
        
    return {"result": result}