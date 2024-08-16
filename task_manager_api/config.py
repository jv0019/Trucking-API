import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:Admin0019@localhost/Task_Manager_API')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
