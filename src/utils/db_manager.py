from src.repositories.book import BookRepository, FileRepository
from src.repositories.role import RoleRepository
from src.repositories.user import UserRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.roles = RoleRepository(self.session)
        self.users = UserRepository(self.session)
        self.books = BookRepository(self.session)
        self.files = FileRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def flush(self):
        await self.session.flush()

    def add(self, model):
        self.session.add(model)
