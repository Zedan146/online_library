from sqlalchemy import select, delete, insert, update
from pydantic import BaseModel


class BaseRepository:
    model = None
    schema: BaseModel = None

    def __init__(self, session):
        self.session = session

    async def get_filtered(self, *filters, **filter_by):
        query = select(self.model).filter(*filters).filter_by(**filter_by)
        result = await self.session.execute(query)

        return result.scalars().all()

    async def get_all(self):
        return await self.get_filtered()

    async def add(self, data: BaseModel, **kwargs):
        add_data_stmt = insert(self.model).values(**data.model_dump(), **kwargs).returning(self.model)
        result = await self.session.execute(add_data_stmt)

        return result.scalar_one()
