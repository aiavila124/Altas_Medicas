from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import QueuePool
import os


class Database():

    base_class = declarative_base()

    def __init__(self):
        
        connection_strings = self.__get_connection_strings()

        string_connection = connection_strings

        self.__engine = create_engine(string_connection, poolclass=QueuePool)
        self.__session_maker = sessionmaker(bind=self.__engine)
        self.session = self.__session_maker()

    def __get_connection_strings(self):

        read_string = "mysql+pymysql://{}:{}@{}/{}".format(
            os.getenv("DB_USER"),
            os.getenv("DB_PASSWORD"),
            os.getenv("DB_HOST"),
            os.getenv("DB_NAME"),
        )

        return read_string
