from src.database import async_session_maker
from src.repositories.role import RoleRepository
from src.schemas.role import RoleAdd


async def test_create_role():
    role_data = RoleAdd(title="admin")
    async with async_session_maker() as session:
        role = await RoleRepository(session).add(role_data)

        print(f"{role=}")
