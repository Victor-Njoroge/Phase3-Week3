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
fname=input("Enter first name: ")
lname=input("Enter last name: ")

rname=input("Enter Restaurant name: ")
rprice=input("Enter price: ")


rate=int(input("Enter rate 1-5: "))
comment=input("Enter comment: ")
new_customer = Customer(firstName=fname, lastName=lname)
new_restaurant = Restaurant(restaurant_name=rname, restaurant_price=rprice)
new_review = Review(customer=new_customer, restaurant=new_restaurant, rating=rate, comments=comment)

def review_customers():
    try:
        
        customers = session.query(Customer).all()

        for customer in customers:
            print(f"Customer ID: {customer.id}, Name: {customer.firstName} {customer.lastName}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

review_customers()


def review_restaurants():
    try:
        restaurants=session.query(Restaurant).all()

        for restaurant in restaurants:
            print(f"Restaurant ID: {restaurant.id} Name: {restaurant.restaurant_name} Price: {restaurant.restaurant_price} ")

    except Exception as e:
        print(f"An error occured: {e}")

    finally:
        session.close()
review_restaurants()







    
session.add(new_customer)
session.add(new_restaurant)
session.add(new_review)
session.commit()

session.close()




    