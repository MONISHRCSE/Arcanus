from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.firewall import router as firewall_router
import sys

# Windows requires a different event loop for high performance
if sys.platform == "win32":
    import asyncio
    try:
        import winloop
        asyncio.set_event_loop_policy(winloop.EventLoopPolicy())
    except ImportError:
        pass
else:
    import uvloop
    uvloop.install()

app = FastAPI(
    title="Agentic AI Firewall",
    description="3-Layer Privacy-Preserving Enterprise Firewall API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow the Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(firewall_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}
