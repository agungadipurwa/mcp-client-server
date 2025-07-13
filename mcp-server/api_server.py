import contextlib
from fastapi import FastAPI
from main import mcp as logtime

import os

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(logtime.session_manager.run())
        yield


app = FastAPI(lifespan=lifespan)
app.mount("/mcp", mcp_server.streamable_http_app())

PORT = os.environ.get("PORT", 1000)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port = PORT)