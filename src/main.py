import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.config import settings

from api import router as api_router
from core.models import db_helper
from api.main_page import main_route
from api.recipes import recipe_route

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    print("dispose engine")
    await db_helper.dispose()

main_app = FastAPI(lifespan=lifespan)
main_app.include_router(main_route)
main_app.include_router(recipe_route)
main_app.include_router(api_router, prefix=settings.api.prefix,)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,

    )