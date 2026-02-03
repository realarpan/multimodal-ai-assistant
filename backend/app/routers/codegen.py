from fastapi import APIRouter
from ..models.schemas import CodeGenRequest, CodeGenResponse
from ..services.codegen import generate_code_from_description

router = APIRouter(prefix="/generate-code", tags=["codegen"])

@router.post("", response_model=CodeGenResponse)
async def generate_code(req: CodeGenRequest):
    code = await generate_code_from_description(req.description, req.context)
    return CodeGenResponse(code=code)
