from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware

clients_apps = ["http://localhost:3000", "http://localhost:8000"]

#create app
app = FastAPI(
    title="FARM FastAPI Application",
    description="This is a FARM FastAPI application.",

)

#register router
app.include_router(student_router)

# Add CORS middleware to allow requests from the specified client applications(domains)
app.add.middleware(
    CORSMiddleware,
    allow_origins=clients_apps,
    allow_methods=["*"],
    allow_headers=["*"],    
    allow_credentials=True
)