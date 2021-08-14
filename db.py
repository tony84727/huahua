from sqlalchemy import create_engine


def new_engine(*, user='root', host='localhost', name='huahua'):
    dsn = f'mysql+pymysql://{user}@{host}/{name}'
    return create_engine(dsn, echo=True, future=True)
