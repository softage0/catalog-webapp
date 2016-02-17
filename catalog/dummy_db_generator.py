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
session.query(User).delete()
session.query(Category).delete()
session.query(CategoryItem).delete()
session.commit()


# Create dummy user
admin = User(name="admin", email="softage0@gmail.com",
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
items.append(CategoryItem(title="Snowboard", description="Best snowboard for this year",
                          category=categories[random.randrange(0, cat_size-1)], user=admin))
items.append(CategoryItem(title="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                          category=categories[random.randrange(0, cat_size-1)], user=admin))
items.append(CategoryItem(title="French Fries", description="with garlic and parmesan",
                          category=categories[random.randrange(0, cat_size-1)], user=admin))
items.append(CategoryItem(title="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                          category=categories[random.randrange(0, cat_size-1)], user=admin))
items.append(CategoryItem(title="Chocolate Cake", description="fresh baked and served with ice cream",
                          category=categories[random.randrange(0, cat_size-1)], user=admin))
items.append(CategoryItem(title="Root Beer", description="16oz of refreshing goodness",
                          category=categories[random.randrange(0, cat_size-1)], user=admin))
items.append(CategoryItem(title="Iced Tea", description="with Lemon",
                          category=categories[random.randrange(0, cat_size-1)], user=admin))
items.append(CategoryItem(title="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
                          category=categories[random.randrange(0, cat_size-1)], user=admin))
items.append(CategoryItem(title="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                          category=categories[random.randrange(0, cat_size-1)], user=admin))
items.append(CategoryItem(title="Peking Duck", description=" A famous duck dish from Beijing\
 that has been prepared since the imperial era. The meat is prized for its thin, crisp skin,\
  with authentic versions of the dish serving mostly the skin and little meat, sliced in front\
   of the diners by the cook",
                          category=categories[random.randrange(0, cat_size-1)], user=admin))
items.append(CategoryItem(title="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame,\
 cucumber with wasabi soy sauce ",
                          category=categories[random.randrange(0, cat_size-1)], user=admin))

for item in items:
    session.add(item)
session.commit()


# menuItem4 = MenuItem(user_id=1, name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
#                      price="12", course="Entree", restaurant=restaurant2)
#
# session.add(menuItem4)
# session.commit()
#
# menuItem5 = MenuItem(user_id=1, name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
#                      price="14", course="Entree", restaurant=restaurant2)
#
# session.add(menuItem5)
# session.commit()
#
# menuItem6 = MenuItem(user_id=1, name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
#                      price="12", course="Entree", restaurant=restaurant2)
#
# session.add(menuItem6)
# session.commit()
#
#
# # Menu for Panda Garden
# restaurant1 = Restaurant(user_id=1, name="Panda Garden")
#
# session.add(restaurant1)
# session.commit()
#
#
# menuItem1 = MenuItem(user_id=1, name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
#                      price="$8.99", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem1)
# session.commit()
#
# menuItem2 = MenuItem(user_id=1, name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
#                      price="$6.99", course="Appetizer", restaurant=restaurant1)
#
# session.add(menuItem2)
# session.commit()
#
# menuItem3 = MenuItem(user_id=1, name="Gyoza", description="light seasoning of Japanese gyoza with salt and soy sauce, and in a thin gyoza wrapper",
#                      price="$9.95", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem3)
# session.commit()
#
# menuItem4 = MenuItem(user_id=1, name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
#                      price="$6.99", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem4)
# session.commit()
#
# menuItem2 = MenuItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
#                      price="$9.50", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem2)
# session.commit()
#
#
# # Menu for Thyme for that
# restaurant1 = Restaurant(user_id=1, name="Thyme for That Vegetarian Cuisine ")
#
# session.add(restaurant1)
# session.commit()
#
#
# menuItem1 = MenuItem(user_id=1, name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
#                      price="$2.99", course="Dessert", restaurant=restaurant1)
#
# session.add(menuItem1)
# session.commit()
#
# menuItem2 = MenuItem(user_id=1, name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
#                      price="$5.99", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem2)
# session.commit()
#
# menuItem3 = MenuItem(user_id=1, name="Honey Boba Shaved Snow",
#                      description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price="$4.50", course="Dessert", restaurant=restaurant1)
#
# session.add(menuItem3)
# session.commit()
#
# menuItem4 = MenuItem(user_id=1, name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
#                      price="$6.95", course="Appetizer", restaurant=restaurant1)
#
# session.add(menuItem4)
# session.commit()
#
# menuItem5 = MenuItem(user_id=1, name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
#                      price="$7.95", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem5)
# session.commit()
#
# menuItem2 = MenuItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
#                      price="$6.80", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem2)
# session.commit()
#
#
# # Menu for Tony's Bistro
# restaurant1 = Restaurant(user_id=1, name="Tony\'s Bistro ")
#
# session.add(restaurant1)
# session.commit()
#
#
# menuItem1 = MenuItem(user_id=1, name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
#                      price="$13.95", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem1)
# session.commit()
#
# menuItem2 = MenuItem(user_id=1, name="Chicken and Rice", description="Chicken... and rice",
#                      price="$4.95", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem2)
# session.commit()
#
# menuItem3 = MenuItem(user_id=1, name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
#                      price="$6.95", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem3)
# session.commit()
#
# menuItem4 = MenuItem(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
#                      description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", course="Dessert", restaurant=restaurant1)
#
# session.add(menuItem4)
# session.commit()
#
# menuItem5 = MenuItem(user_id=1, name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
#                      price="$7.95", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem5)
# session.commit()
#
#
# # Menu for Andala's
# restaurant1 = Restaurant(user_id=1, name="Andala\'s")
#
# session.add(restaurant1)
# session.commit()
#
#
# menuItem1 = MenuItem(user_id=1, name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
#                      price="$9.95", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem1)
# session.commit()
#
# menuItem2 = MenuItem(user_id=1, name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
#                      price="$7.95", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem2)
# session.commit()
#
# menuItem3 = MenuItem(user_id=1, name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
#                      price="$6.50", course="Appetizer", restaurant=restaurant1)
#
# session.add(menuItem3)
# session.commit()
#
# menuItem4 = MenuItem(user_id=1, name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
#                      price="$6.75", course="Appetizer", restaurant=restaurant1)
#
# session.add(menuItem4)
# session.commit()
#
# menuItem2 = MenuItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
#                      price="$7.00", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem2)
# session.commit()
#
#
# # Menu for Auntie Ann's
# restaurant1 = Restaurant(user_id=1, name="Auntie Ann\'s Diner' ")
#
# session.add(restaurant1)
# session.commit()
#
# menuItem9 = MenuItem(user_id=1, name="Chicken Fried Steak",
#                      description="Fresh battered sirloin steak fried and smothered with cream gravy", price="$8.99", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem9)
# session.commit()
#
#
# menuItem1 = MenuItem(user_id=1, name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
#                      price="$2.99", course="Dessert", restaurant=restaurant1)
#
# session.add(menuItem1)
# session.commit()
#
# menuItem2 = MenuItem(user_id=1, name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
#                      price="$10.95", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem2)
# session.commit()
#
# menuItem3 = MenuItem(user_id=1, name="Morels on toast (seasonal)",
#                      description="Wild morel mushrooms fried in butter, served on herbed toast slices", price="$7.50", course="Appetizer", restaurant=restaurant1)
#
# session.add(menuItem3)
# session.commit()
#
# menuItem4 = MenuItem(user_id=1, name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
#                      price="$8.95", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem4)
# session.commit()
#
# menuItem2 = MenuItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
#                      price="$9.50", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem2)
# session.commit()
#
# menuItem10 = MenuItem(user_id=1, name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
#                       price="$1.99", course="Dessert", restaurant=restaurant1)
#
# session.add(menuItem10)
# session.commit()
#
#
# # Menu for Cocina Y Amor
# restaurant1 = Restaurant(user_id=1, name="Cocina Y Amor ")
#
# session.add(restaurant1)
# session.commit()
#
#
# menuItem1 = MenuItem(user_id=1, name="Super Burrito Al Pastor",
#                      description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", price="$5.95", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem1)
# session.commit()
#
# menuItem2 = MenuItem(user_id=1, name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
#                      price="$7.99", course="Entree", restaurant=restaurant1)
#
# session.add(menuItem2)
# session.commit()
#
#
# restaurant1 = Restaurant(user_id=1, name="State Bird Provisions")
# session.add(restaurant1)
# session.commit()
#
# menuItem1 = MenuItem(user_id=1, name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
#                      price="$5.95", course="Appetizer", restaurant=restaurant1)
#
# session.add(menuItem1)
# session.commit
#
# menuItem1 = MenuItem(user_id=1, name="Guanciale Chawanmushi",
#                      description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)", price="$6.95", course="Dessert", restaurant=restaurant1)
#
# session.add(menuItem1)
# session.commit()
#
#
# menuItem1 = MenuItem(user_id=1, name="Lemon Curd Ice Cream Sandwich",
#                      description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews", price="$4.25", course="Dessert", restaurant=restaurant1)
#
# session.add(menuItem1)
# session.commit()
#
#
# print "added menu items!"
