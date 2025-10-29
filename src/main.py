# ruff: noqa: E402
import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.api.role import router as router_role

app = FastAPI()

app.include_router(router_role)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
