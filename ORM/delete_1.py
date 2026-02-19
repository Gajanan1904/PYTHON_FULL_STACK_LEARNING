# ORM - Object Relational Mapping
# Translator between Python and SQL
# installation command: pip install sqlalchemy

# SQL        -> PYTHON
# Table      -> Class
# Row        -> Object
# Column     -> Variable

# import create_engine to connect Python with database
from sqlalchemy import create_engine

# create SQLite database connection
# database file name: psq1.db
engine = create_engine("sqlite:///psq1.db")
print("Database connected")

# import declarative base for ORM mapping
from sqlalchemy.orm import declarative_base

# import column data types
from sqlalchemy import Column, Integer, String

# import sessionmaker to create session
from sqlalchemy.orm import sessionmaker

# create base class
Base = declarative_base()

# create Students table model
class Students(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True)  # primary key
    name = Column(String)                   # student name
    age = Column(Integer)                   # student age
    course = Column(String)                 # course name

# create table if not exists
Base.metadata.create_all(engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()

# if we want to delete all values from database
# delete all records from Students table
session.query(Students).delete()

# save changes to database
session.commit()

print("All records deleted successfully")


