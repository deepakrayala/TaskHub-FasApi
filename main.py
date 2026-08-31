from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.init import *

app = FastAPI()

#Enable Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://taskhub-2api.onrender.com"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#Registers all routers
app.include_router(AuthenticationRouter)
app.include_router(TaskRouter)

@app.get("/")
def home():
    return "Started..."
