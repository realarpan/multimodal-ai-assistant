from .hf_client import hf_infer_text

CODE_SYSTEM_PROMPT = """You are a Python code generator.
Generate minimal, executable Python code using standard libraries and matplotlib when visualization is needed.
Return only code, no explanation.
"""

async def generate_code_from_description(description: str, context: str | None = None) -> str:
    prompt = CODE_SYSTEM_PROMPT + "\nUser request:\n" + description
    if context:
        prompt += "\nContext:\n" + context
    code = await hf_infer_text(prompt)
    # Best-effort cleanup: strip fenced blocks if LLM returns them.
    if "```" in code:
        parts = code.split("```")
        if len(parts) >= 3:
            return parts[2] if parts[1].strip().startswith("python") else parts[1]
    return code
