# --*-- coding:utf-8 --*--
# Author: heliuhong2
# Time: 2022/8/18 下午8:04
from urllib.parse import quote_plus as urlquote
import sqlalchemy
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker

class MySQLStorage(object):
    def __init__(self,real_data = False) -> None:
        """Initialize MySQL connection.
        real_data: False in project excise,True if you have actual mysql config
        """
        self.real_data = real_data
        if self.real_data:
            connect_uri = "mysql+pymysql://{username}:{password}@{host}:{port}/{base}"
            connect_uri = connect_uri.format(
                username="user_name",
                password=urlquote("password"),
                host="host",
                port="port",
                base="db_name",
            )

            stream_engine = sqlalchemy.create_engine(connect_uri, echo=False)
            self.Session = scoped_session(sessionmaker(bind=stream_engine, autocommit=True))

    def extract_result_insert_to_db(self,result_list):
        '''
        insert reulst to db
        result_list: text extract data
        :return:
        '''
        if self.real_data:
            try:
                session = self.Session()
                sql_insert = "insert sql"
                insert_result = session.execute(sql_insert)
                session.close()
            except sqlalchemy.exc.OperationalError as e:
                print(e)

