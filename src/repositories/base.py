from typing import Any, List, Optional

from sqlalchemy import select, delete, insert, update
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    model = None
    schema: BaseModel = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_filtered(self, *filters: Any, **filter_by: Any) -> List[BaseModel]:
        query = select(self.model).filter(*filters).filter_by(**filter_by)
        result = await self.session.execute(query)

        return [self.schema.model_validate(model) for model in result.scalars().all()]

    async def get_all(self) -> List[BaseModel]:
        return await self.get_filtered()

    async def get_one_or_none(self, *args, **kwargs) -> Optional[BaseModel]:
        query = select(self.model).filter(*args).filter_by(**kwargs)
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        if not model:
            return None
        return self.schema.model_validate(model)

    async def add(self, data: BaseModel, **kwargs: Any) -> BaseModel:
        add_data_stmt = insert(self.model).values(**data.model_dump(), **kwargs).returning(self.model)
        result = await self.session.execute(add_data_stmt)
        model = result.scalar_one()

        return self.schema.model_validate(model)

    async def add_bulk(self, data: list[BaseModel]) -> list[BaseModel]:
        add_data_stmt = insert(self.model).values([item.model_dump() for item in data]).returning(self.model)
        result = await self.session.execute(add_data_stmt)

        return [self.schema.model_validate(model) for model in result.scalars().all()]

    async def update(self, data: BaseModel, **filter_by: Any) -> BaseModel:
        update_data_stmt = update(self.model).filter_by(**filter_by).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(update_data_stmt)
        model = result.scalar_one()

        return self.schema.model_validate(model)

    async def delete(self, **filter_by: Any) -> BaseModel:
        delete_stmt = delete(self.model).filter_by(**filter_by).returning(self.model)
        result = await self.session.execute(delete_stmt)
        model = result.scalar_one()

        return self.schema.model_validate(model)
