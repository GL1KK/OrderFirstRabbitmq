from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str  
    DB_PORT: int  
    DB_USER: str 
    DB_PASS: str  
    DB_NAME: str 
    JWT_SECRET_KEY: str
    USERNAME_ADMIN: str
    PASSWORD_ADMIN: str
    TOKEN: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8"  
    )

settings = Settings()
