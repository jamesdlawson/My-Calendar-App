from pydantic import BaseSettings

class Settings(BaseSettings):
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "FastAPI"
    version: str = "0.0.0"
    disable_docs: bool = False

    class Config:
        env_file = ".env"

    def fastapi_kwargs(self):
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
            "disable_docs": self.disable_docs,
        }

