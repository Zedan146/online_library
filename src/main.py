# ruff: noqa: E402
import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.api.role import router as role_router
from src.api.auth import router as auth_router
from src.api.book import router as book_router
from src.api.file import router as file_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(role_router)
app.include_router(book_router)
app.include_router(file_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
