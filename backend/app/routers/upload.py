from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4
import shutil
from pathlib import Path
from ..models.schemas import UploadResponse

router = APIRouter(prefix="/upload", tags=["upload"])

UPLOAD_DIR = Path("/tmp/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    file_ext = Path(file.filename).suffix.lower()
    file_type = "other"
    if file.content_type.startswith("image/"):
        file_type = "image"
    elif file.content_type.startswith("audio/"):
        file_type = "audio"
    elif file.content_type.startswith("video/"):
        file_type = "video"

    file_id = f"{file_type}_{uuid4().hex}{file_ext}"
    dest = UPLOAD_DIR / file_id
    try:
        with dest.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to save file")

    return UploadResponse(file_id=file_id, file_type=file_type, detail="Uploaded successfully")
