from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter(prefix="/files", tags=["Файлы"])


@router.get("/{filename}")
async def get_file(filename: str, file_type: str):
    return FileResponse(path=f"src/upload/{file_type}/{filename}")
