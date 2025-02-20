from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = 'sqlite:///kohvikud.db'
ENGINE = create_engine(DB_URL, echo=False)

Session = sessionmaker(bind=ENGINE)
