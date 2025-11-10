from fastapi import APIRouter

from src.api.dep import DBDep
from src.schemas.role import RoleAdd

router = APIRouter(prefix="/role", tags=["Роли"])


@router.get("/", summary="Получить все роли")
async def get_role(db: DBDep):
    return await db.roles.get_all()


@router.post("/", summary="Добавить роль")
async def create_role(data: RoleAdd, db: DBDep):
    role = await db.roles.add(data)
    await db.commit()

    return role


@router.put("/{role_id}", summary="Изменить роль")
async def edit_role(role_id: int, data: RoleAdd, db: DBDep):
    role = await db.roles.update(data, id=role_id)
    await db.commit()

    return role


@router.delete("/{role_id}", summary="Удалить роль")
async def delete_role(role_id: int, db: DBDep):
    role = await db.roles.delete(id=role_id)
    await db.commit()

    return {"status":  "OK", "data": role}
