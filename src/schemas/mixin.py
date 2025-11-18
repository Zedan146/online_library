from typing import Any, ClassVar

from pydantic import BaseModel, field_validator, ConfigDict


class NonEmptyStringMixin(BaseModel):
    """Миксин с исключением определенных полей"""
    EXCLUDED_FIELDS: ClassVar[set[str]] = set()

    @field_validator("*", mode="before")
    def validate_all_string_fields(cls, v: Any, info) -> Any:
        if (info.field_name not in cls.EXCLUDED_FIELDS and
                isinstance(v, str)):
            stripped = v.strip()
            if not stripped:
                raise ValueError(f"Поле {info.field_name} не может быть пустым")
            return stripped
        return v

    model_config = ConfigDict(from_attributes=True)
