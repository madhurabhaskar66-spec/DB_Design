
# customer support

# return order
# update profile
# update password
# filter products
# payment modes
# share a product link
# upload image and find similar products
from sqlalchemy import create_engine

Base = declarative_base()

class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Integer)
    total = Column(Integer)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Wishlist(Base):
    __tablename__ = 'wishlists'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    category = Column(String)
    stock = Column(Integer)
    image = Column(String)
    size = Column(String)#7 sizes
    color = Column(String) # 20 colors
    brand = Column(String)
    isprime= Column(Boolean)
    taxpercent= Column(Integer)


class ProductReview(Base):
    __tablename__ = 'product_reviews'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer)
    review = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)  

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String) 
    phone = Column(String)
    isprime= Column(Boolean)
    

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    price = Column(Integer)
    total = Column(Integer)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    payment_type=Column(String)
    payment_status=Column(String)
    

class OrderDetails(Base):
    __tablename__ = 'order_details'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Integer)
    total = Column(Integer)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

