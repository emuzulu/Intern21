from sqlalchemy import Column, Integer, String, DateTime, Date
from database import Base
from datetime import datetime
from datetime import date
from crypt import encrypt

class Application(Base):
    __tablename__ = 'applications'
    id = Column(Integer, primary_key=True)
    company = Column(String(50), nullable=False)
    role = Column(String(20), nullable=False)
    date = Column(DateTime(timezone=False), nullable=False)

    def __init__(self, company, role, date):
        self.company = company
        self.role = role
        self.date = datetime.now()
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(16), unique=True)
    password = Column(String(50), nullable=False)
    email = Column(String(30), nullable=False)


    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    
