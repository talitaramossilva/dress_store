from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Dress(Base):
    __tablename__ = 'dresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(200), unique=True)
    size = Column(String(1))
    color = Column(String(50))
    price = Column(Float)

    def __init__(self, description : str, size: str, color: int, price: int):
        """
        Define a dress with the folowing attibutes:
            - size
            - color
            - price
        """
        self.description = description
        self.size = size
        self.color = color
        self.price = price

    def __repr__(self):
        return f"<Dress(id={self.id}, size='{self.size}', price={self.price})>"
