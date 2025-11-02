from fastapi import APIRouter

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


@router.put("/{role_id}", summary="Изменить роль")
async def edit_role(role_id: int, data: RoleAdd):
    async with async_session_maker() as session:
        role = await RoleRepository(session).update(data, id=role_id)
        await session.commit()

    return role


@router.delete("/{role_id}", summary="Удалить роль")
async def delete_role(role_id: int):
    async with async_session_maker() as session:
        role = await RoleRepository(session).delete(id=role_id)
        await session.commit()

    return {"status":  "OK", "data": role}
