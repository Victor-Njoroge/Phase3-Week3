#review
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from customer import Base
from restaurant import Restaurant

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    rating = Column(Integer)
    comments = Column(String)

    customer = relationship("Customer", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews")

    def __init__(self, customer, restaurant, rating, comments):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.comments = comments


