from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import date

# Import our tools
# This is the database connection file
from db import engine, session
from config import settings

# These are our models
from models import Base, Links, LinksModel


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()

# Setup our origins...
# ...for now it's just our local environments
origins = [
    "http://localhost:*"
]

# Add the CORS middleware...
# ...this will pass the proper CORS headers
# https://fastapi.tiangolo.com/tutorial/middleware/
# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Root Route"}


@app.get('/links')
def get_links():
    links = session.query(Links)
    return links.all()


@app.post('/links/add')
async def add_link(link_data: LinksModel):
    link = Links(title=link_data.title,
                 long_url=link_data.long_url,
                 short_url=link_data.short_url,
                 user_id=1)
    session.add(link)
    session.commit()
    return {"Link Added": link.title}
