from .hf_client import hf_infer_vision, hf_infer_audio, hf_infer_text
from .rag import query_documents, add_document
from ..core.celery_app import celery
from ..core.logging_config import logger

@celery.task(name="app.services.ml_inference.process_multimodal_task")
def process_multimodal_task(
    session_id: str,
    text: str,
    image_bytes: bytes | None = None,
    audio_bytes: bytes | None = None,
) -> str:
    logger.info("processing_multimodal", session_id=session_id)
    insights = []

    if image_bytes:
        vision_out = celery.app.loop.run_until_complete(
            hf_infer_vision(image_bytes, f"Describe the scene and emotions. User query: {text}")
        )
        insights.append(f"Vision analysis:\n{vision_out}")

    if audio_bytes:
        transcript = celery.app.loop.run_until_complete(hf_infer_audio(audio_bytes))
        insights.append(f"Audio transcript:\n{transcript}")
        text = text + "\n\nTranscript:\n" + transcript

    rag_context = query_documents(text) if text else ""
    if rag_context:
        insights.append(f"RAG context:\n{rag_context}")

    reasoning_prompt = (
        "You are a multimodal reasoning assistant. Combine the following signals into a helpful explanation.\n\n"
        + "\n\n".join(insights)
        + f"\n\nUser question:\n{text}"
    )

    reasoning = celery.app.loop.run_until_complete(hf_infer_text(reasoning_prompt))
    add_document(f"session-{session_id}", reasoning, {"session_id": session_id})
    return reasoning
