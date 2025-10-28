from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

# Import routers correctly
from routes_auth import router as auth_router
from routes_core import router as core_router
from routes_fractals import router as fractal_router  # Updated import

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(BASE_DIR, "static")
if os.path.isdir(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Create templates directory if it doesn't exist
templates_dir = os.path.join(BASE_DIR, "templates")
os.makedirs(templates_dir, exist_ok=True)

# Routers
app.include_router(core_router)
app.include_router(auth_router) 
app.include_router(fractal_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://noahfractals.cab432.com",
        "https://e02drxt0kk.execute-api.ap-southeast-2.amazonaws.com",
        "http://localhost:8000",
        "http://YOUR_EC2_IP:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)