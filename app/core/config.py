from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://bmf:bmf@localhost:5432/listings"
    service_name: str = "listing-service"

settings = Settings()