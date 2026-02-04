import uuid
import contextvars
from fastapi import Request
import structlog

request_id_contextvar = contextvars.ContextVar('request_id', default=None)

class RequestIDMiddleware:
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        request_id_contextvar.set(request_id)
        request.state.request_id = request_id
        
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
