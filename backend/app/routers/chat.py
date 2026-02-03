from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator
from ..models.schemas import ChatRequest
from ..services.ml_inference import process_multimodal_task
from ..core.logging_config import logger

router = APIRouter(prefix="/chat", tags=["chat"])

async def sse_stream(text: str, session_id: str) -> AsyncGenerator[bytes, None]:
    # Naive streaming: chunk by sentence for demo.
    chunks = text.split(". ")
    for i, c in enumerate(chunks):
        payload = {"session_id": session_id, "content": c, "finished": i == len(chunks) - 1}
        yield f"data: {payload}\n\n".encode("utf-8")

@router.post("/stream")
async def chat_stream(request: Request, body: ChatRequest):
    if not body.messages:
        raise HTTPException(status_code=400, detail="No messages")
    user_msg = body.messages[-1].content
    logger.info("chat_request", session_id=body.session_id)

    # For brevity, ignore actual file loading and Celery; directly call task sync.
    result_text = process_multimodal_task(
        session_id=body.session_id,
        text=user_msg,
        image_bytes=None,
        audio_bytes=None,
    )
    return StreamingResponse(
        sse_stream(result_text, body.session_id),
        media_type="text/event-stream",
    )
