
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from .models import Base


load_dotenv()
DATABASE_URL = os.getenv("sqlite:///./warranty.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def init_db():
  Base.metadata.create_all(bind=engine)

