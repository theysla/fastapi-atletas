from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):  # Ajustar para o mesmo nome usado abaixo
    DB_URL: str = Field(default='postgresql+asyncpg://workout:workout@localhost/workout')

settings = Settings()
