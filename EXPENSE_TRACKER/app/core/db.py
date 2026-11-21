from sqlalchemy import create_engine #create new engine instance
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///./expense.db"

#create engine
engine = create_engine(
    DATABASE_URL,
    connect_args = {
        "check_same_thread" : False
    }
)



#session
LocalSession = sessionmaker(
    bind = engine,
    autocommit = False,
    autoFlush = False
)


#dependency
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()