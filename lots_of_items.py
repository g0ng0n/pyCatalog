from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Gonzo Opera", email="gonzo@operations.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Items for Soccer
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Ball", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category1)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Gloves", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category1)

session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Boots", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Canilleras", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category1)

session.add(item2)
session.commit()

item5 = Item(user_id=1, name="Gloves 33", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category1)
session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Ball Nike", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category1)
session.add(item6)
session.commit()

item7 = Item(user_id=1, name="Argentina Jersey", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category1)
session.add(item7)
session.commit()

# Items for Basket
category2 = Category(user_id=1, name="Basket")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Ball", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category2)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Gloves", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category2)

session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Boots", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category2)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Canilleras", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category2)

session.add(item2)
session.commit()

item5 = Item(user_id=1, name="Gloves 33", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category2)
session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Ball Nike", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category2)
session.add(item6)
session.commit()

item7 = Item(user_id=1, name="Argentina Jersey", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category2)
session.add(item7)
session.commit()

# Items for Volley
category3 = Category(user_id=1, name="Volley")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Ball", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category3)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Gloves", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category3)

session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Boots", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category3)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Canilleras", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category3)

session.add(item2)
session.commit()

item5 = Item(user_id=1, name="Gloves 33", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category3)
session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Ball Nike", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category3)
session.add(item6)
session.commit()

item7 = Item(user_id=1, name="Argentina Jersey", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "+
                                                     "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "+
                                                     "when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    category=category3)
session.add(item7)
session.commit()



print "added menu items!"