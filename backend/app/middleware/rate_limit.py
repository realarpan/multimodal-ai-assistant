from fastapi import Request, HTTPException
import redis
from app.core.config import get_settings

class RateLimitMiddleware:
    def __init__(self, app, requests_per_minute: int = 60):
        self.app = app
        self.requests_per_minute = requests_per_minute
        self.redis_client = redis.from_url(get_settings().REDIS_URL)
    
    async def __call__(self, request: Request, call_next):
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"
        
        try:
            current = self.redis_client.incr(key)
            if current == 1:
                self.redis_client.expire(key, 60)
            
            if current > self.requests_per_minute:
                raise HTTPException(status_code=429, detail="Rate limit exceeded")
        except redis.ConnectionError:
            pass  # Fail open if Redis is down
        
        return await call_next(request)
