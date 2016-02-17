import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, CategoryItem
from config import config

engine = create_engine(config.DB_URL)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Delete existing DB
session.query(CategoryItem).delete()
session.query(Category).delete()
session.query(User).delete()
session.commit()


# Create dummy user
admin = User(name="admin", email="softage3@gmail.com",
             picture='https://lh5.googleusercontent.com/-rXt7YCTSUS8/AAAAAAAAAAI/AAAAAAAAAEk/tKXxlyexJZw/photo.jpg')
session.add(admin)
session.commit()


# Add categories
categories = list()
categories.append(Category(name="Soccer", user=admin))
categories.append(Category(name="Basketball", user=admin))
categories.append(Category(name="Baseball", user_id=admin.id, user=admin))
categories.append(Category(name="Frisbee", user_id=admin.id, user=admin))
categories.append(Category(name="Snowboarding", user_id=admin.id, user=admin))
categories.append(Category(name="Rock Climbing", user_id=admin.id, user=admin))
categories.append(Category(name="Foosball", user_id=admin.id, user=admin))
categories.append(Category(name="Skating", user_id=admin.id, user=admin))
categories.append(Category(name="Hockey", user_id=admin.id, user=admin))

for category in categories:
    session.add(category)
session.commit()

cat_size = len(categories)


# Add items
items = list()

for i in range(50):
    items.append(CategoryItem(title="Snowboard"+str(i), description="Best snowboard for this year",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Veggie Burger"+str(i),
                              description="Juicy grilled veggie patty with tomato mayo and lettuce",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="French Fries"+str(i), description="with garlic and parmesan",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Chicken Burger"+str(i),
                              description="Juicy grilled chicken patty with tomato mayo and lettuce",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Chocolate Cake"+str(i), description="fresh baked and served with ice cream",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Root Beer"+str(i), description="16oz of refreshing goodness",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Iced Tea"+str(i), description="with Lemon",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Grilled Cheese Sandwich"+str(i), description="On texas toast with American Cheese",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Chicken Stir Fry"+str(i),
                              description="With your choice of noodles vegetables and sauces",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Peking Duck"+str(i), description="A famous duck dish from Beijing\
     that has been prepared since the imperial era.",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Spicy Tuna Roll"+str(i), description="Seared rare ahi, avocado, edamame,\
     cucumber with wasabi soy sauce ",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Nepali Momo"+str(i),
                              description="Steamed dumplings made with vegetables, spices and meat.",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Beef Noodle Soup"+str(i),
                              description="A Chinese noodle soup made of stewed or red braised beef,\
                               beef broth, vegetables and Chinese noodles.",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Ramen"+str(i), description="a Japanese noodle soup dish.",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Pho"+str(i), description="a Vietnamese noodle soup consisting of broth,\
     linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Chinese Dumplings"+str(i),
                              description="a common Chinese dumpling which generally\
                               consists of minced meat and finely chopped vegetables wrapped\
                                into a piece of dough skin.",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Gyoza"+str(i), description="light seasoning of Japanese gyoza with salt and soy sauce,\
     and in a thin gyoza wrapper",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))
    items.append(CategoryItem(title="Stinky Tofu"+str(i),
                              description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                              category=categories[random.randrange(0, cat_size-1)], user=admin))

for item in items:
    session.add(item)
session.commit()


print "added menu items!"
