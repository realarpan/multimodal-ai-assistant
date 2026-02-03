from pydantic import BaseModel, Field
from typing import Optional, List

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    session_id: str
    messages: List[ChatMessage]
    image_id: Optional[str] = None
    audio_id: Optional[str] = None
    video_id: Optional[str] = None

class ChatResponseChunk(BaseModel):
    session_id: str
    content: str
    finished: bool = False

class UploadResponse(BaseModel):
    file_id: str
    file_type: str
    detail: str

class CodeGenRequest(BaseModel):
    description: str = Field(..., description="What code should be generated?")
    context: Optional[str] = None

class CodeGenResponse(BaseModel):
    code: str

class TokenData(BaseModel):
    sub: str
