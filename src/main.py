from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.api import router as api_router
from src.api.ingredient import ingredient_route
from src.api.main_page import main_route
from src.api.recipes import recipe_route
from src.core.config import settings
from src.core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    yield
    print("dispose engine")
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(main_route)
main_app.include_router(recipe_route)
main_app.include_router(ingredient_route)
main_app.include_router(
    api_router,
    prefix=settings.api.prefix,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
