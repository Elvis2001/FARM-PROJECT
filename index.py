from fastapi import FastAPI
from routes.student import student_router


app = FastAPI(
    title="FARM FastAPI Application",
    description="This is a FARM FastAPI application.",

)

app.include_router(student_router)