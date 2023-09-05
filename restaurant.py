#restaurant
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from customer import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String)
    restaurant_price = Column(String)

    def __init__(self, restaurant_name, restaurant_price):
        self.restaurant_name = restaurant_name
        self.restaurant_price = restaurant_price

    reviews = relationship("Review", back_populates="restaurant")



