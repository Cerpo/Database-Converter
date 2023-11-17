import sqlalchemy
from src.config import cfg


def create_engine():
    db_url = ('mysql+pymysql://' +
              cfg.get_value('datasource', 'user') + ':' +
              cfg.get_value('datasource', 'password') + '@' +
              cfg.get_value('datasource', 'host') + '/' +
              cfg.get_value('datasource', 'database'))
    return sqlalchemy.create_engine(db_url)
