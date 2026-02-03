import httpx
from ..core.config import get_settings

settings = get_settings()

HF_HEADERS = {
    "Authorization": f"Bearer {settings.hf_api_token}",
}

async def hf_infer_vision(image_bytes: bytes, prompt: str) -> str:
    # Example with an open LLaVA-like endpoint on HF Inference API.[web:7]
    url = "https://api-inference.huggingface.co/models/liuhaotian/llava-v1.5-7b"
    async with httpx.AsyncClient(timeout=120) as client:
        files = {"image": image_bytes}
        data = {"inputs": prompt}
        r = await client.post(url, headers=HF_HEADERS, data=data, files=files)
        r.raise_for_status()
        out = r.json()
        if isinstance(out, list) and out and "generated_text" in out[0]:
            return out[0]["generated_text"]
        return str(out)

async def hf_infer_audio(audio_bytes: bytes) -> str:
    # Whisper automatic speech recognition endpoint.[web:7]
    url = "https://api-inference.huggingface.co/models/openai/whisper-small"
    async with httpx.AsyncClient(timeout=300) as client:
        r = await client.post(url, headers=HF_HEADERS, data=audio_bytes)
        r.raise_for_status()
        out = r.json()
        return out.get("text", str(out))

async def hf_infer_text(prompt: str) -> str:
    # Open-source LLM (Grok-like reasoning via open model, e.g. Mistral).[web:7]
    url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    async with httpx.AsyncClient(timeout=120) as client:
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": 512, "temperature": 0.4}}
        r = await client.post(url, headers=HF_HEADERS, json=payload)
        r.raise_for_status()
        out = r.json()
        if isinstance(out, list) and out and "generated_text" in out[0]:
            return out[0]["generated_text"]
        return str(out)
