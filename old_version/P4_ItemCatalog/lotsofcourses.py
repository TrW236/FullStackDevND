from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Institute, Base, Course, User

engine = create_engine('sqlite:///institutes_courses.db')
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
User1 = User(
    name="Robo Barista",
    email="tinnyTim@udacity.com",
    picture='https://pbs.twimg.com/profile_images/2671170543/'
    '18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# ---
inst_rob = Institute(
    name="Institute of Robotics",
    user_id=1)
session.add(inst_rob)
session.commit()

pro_con = Course(
    user_id=1,
    name="Process Control",
    description="The Control of Processes",
    institute=inst_rob)
session.add(pro_con)
session.commit()

robotics = Course(
    user_id=1,
    name="Robotics",
    description="The Science of Robots",
    institute=inst_rob)
session.add(robotics)
session.commit()

# ---
inst_automotive = Institute(
    user_id=1,
    name="Institute of Automotive Engineering")
session.add(inst_automotive)
session.commit()

automo_dynamics = Course(
    user_id=1,
    name="Automotive Dynamics",
    description="The Dynamics of Automobiles",
    institute=inst_automotive)
session.add(automo_dynamics)
session.commit()

automo_assist_sys = Course(
    user_id=1,
    name="Driving Assistance System",
    description="The Assistance Systems of Automobiles",
    institute=inst_automotive)
session.add(automo_assist_sys)
session.commit()

print "Finished added courses into the db."
