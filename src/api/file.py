from fastapi import APIRouter
from fastapi.responses import FileResponse

from src.api.dep import DBDep

router = APIRouter(prefix="/files", tags=["Файлы"])


@router.get("/{filename}")
async def get_file(filename: str, file_type: str):
    return FileResponse(path=f"src/upload/{file_type}/{filename}")


@router.get("/info/{file_id}")
async def get_info_file(file_id: int, db: DBDep):
    return await db.files.get_one_or_none(id=file_id)
