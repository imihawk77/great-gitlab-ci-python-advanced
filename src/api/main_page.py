from fastapi import APIRouter

main_route = APIRouter()


@main_route.get("/", tags=["Главная страница"])
def main_page():
    return {"message": "Main page"}