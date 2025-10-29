from fastapi import APIRouter, Body, Query

from src.database import async_session_maker
from src.repositories.role import RoleRepository
from src.schemas.role import RoleAdd

router = APIRouter(prefix="/role", tags=["Роли"])


@router.get("/", summary="Получить все роли")
async def get_role():
    async with async_session_maker() as session:
        return await RoleRepository(session).get_all()


@router.post("/", summary="Добавить роль")
async def create_role(data: RoleAdd):
    async with async_session_maker() as session:
        role = await RoleRepository(session).add(data)
        await session.commit()

        return role
