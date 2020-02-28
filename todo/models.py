from datetime import datetime
import secrets

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Unicode,
    Integer,
    DateTime,
    Boolean,
    relationship,
    ForeignKey
)

Base = declarative_base()

class Task(Base):
    """Task column for managing each ToDo"""
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    note = Column(Unicode)
    creation_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('user', back_populates='tasks')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs);
        self.creation_date = datetime.now()

class User(Base):
    """User column for each user"""
    id = Column(Integer, primary_key=True)
    username = Column(Unicode, nullable=False)
    email = Column(Unicode, nullable=False)
    password = Column(Unicode, nullable=False)
    date_joined = Column(DateTime, nullable=False)
    token = Column(Unicode, nullable=False)
    tasks = relationship("Task", back_populates="user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.date_joined = datetime.now()
        self.token = secrets.token_urlsafe(64)
