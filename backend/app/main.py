from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.logging_config import setup_logging, logger
from .routers import upload, chat, codegen, metrics, ws

setup_logging()
app = FastAPI(title="Real-Time Multimodal AI Assistant")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(chat.router)
app.include_router(codegen.router)
app.include_router(metrics.router)
# WebSocket route via app.router directly; FastAPI handles this.
app.include_router(ws.router)

@app.get("/")
def read_root():
    logger.info("root_ping")
    return {"message": "Multimodal AI Assistant backend is running"}
