#main
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from customer import Base, Customer
from restaurant import Restaurant
from review import Review

engine = create_engine('sqlite:///mydatabase.db')


Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

new_customer = Customer(firstName='Victor', lastName='Njoroge')
new_restaurant = Restaurant(restaurant_name='Epashikino Resort and Spa', restaurant_price='4000$')
new_review = Review(customer=new_customer, restaurant=new_restaurant, rating=5, comments='Great experience')


session.add(new_customer)
session.add(new_restaurant)
session.add(new_review)
session.commit()

session.close()
