from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Define the Restaurant, Customer, and Review models
class Restaurant(Base):
    _tablename_ = 'restaurants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    
    reviews = relationship("Review", back_populates="restaurant")
    
    def customers(self):
        return [review.customer for review in self.reviews]

class Customer(Base):
    _tablename_ = 'customers'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    favorite_restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    
    favorite_restaurant = relationship("Restaurant")
    reviews = relationship("Review", back_populates="customer")
    
    def restaurants(self):
        return [review.restaurant for review in self.reviews]
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def favorite_restaurant(self):
        return self.favorite_restaurant
    
    def set_favorite_restaurant(self, restaurant):
        self.favorite_restaurant = restaurant
    
    def add_review(self, restaurant, rating):
        new_review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        session.add(new_review)
        session.commit()
    
    def delete_reviews(self, restaurant):
        reviews_to_delete = session.query(Review).filter(Review.restaurant_id == restaurant.id, Review.customer_id == self.id).all()
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

class Review(Base):
    _tablename_ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")
    
    def full_review(self):
        restaurant_name = self.restaurant.name if self.restaurant else " Restaurant"
        customer_name = self.customer.full_name() if self.customer else " Customer"
        return f"Review for {restaurant_name} by {customer_name}: {self.star_rating} stars."

# Create the database tables
Base.metadata.create_all(engine)

# Sample data
customer1 = Customer(first_name="Mark", last_name="Travis")
restaurant1 = Restaurant(name=" Voyager Restaurant", price=3)
customer1.add_review(restaurant1, 4)


customer1.set_favorite_restaurant(restaurant1)


session.commit()

# Test the methods
print(customer1.favorite_restaurant.name)
print(restaurant1.reviews[0].full_review())