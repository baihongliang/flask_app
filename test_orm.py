from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host ='localhost'
user ='root'
password ='rootroot'
db ='test'
charset ='utf8mb4'

Base = declarative_base()

class User(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)


def test_orm():
    print(password)
    engine = create_engine(
        f'mysql+pymysql://{user}:{password}@{host}/{db}'.format(
            host=host, db=db, user=user, password=password),
        echo=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # 数据插入
    u1 = User(
        username="bhl",
        password="password",
        email="bhl@ceshiren.com"
    )
    session.add(u1)
    session.commit()

    # 数据查询
    u2 = session.query(User).filter_by(username="bhl").first()
    print(u2.username)