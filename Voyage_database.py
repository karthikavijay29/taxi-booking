from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:Vi@29112004@localhost:3306/moon"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Voyage(Base):
    __tablename__ = 'voyage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone = Column(String)
    date = Column(String)
    when = Column(String)
    pickup_location = Column(String)
    drop_location = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
