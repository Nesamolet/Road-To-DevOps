from fastapi import FastAPI
import models, database, routes

app = FastAPI()

# Создаём таблицы
models.Base.metadata.create_all(bind=database.engine)

# Подключаем роуты
app.include_router(routes.router)
