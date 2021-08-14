from sqlalchemy import create_engine, text, Column
from sqlalchemy.engine import Engine
from sqlalchemy.sql.sqltypes import Integer, VARCHAR
from sqlalchemy.orm import registry

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Server(Base):
    """orm model of the stored servers"""
    __tablename__ = 'servers'

    id = Column(Integer, primary_key=True)
    address = Column(VARCHAR(512), index=True)
    alias = Column(VARCHAR(256), nullable=True, index=True)

    def __repr__(self) -> str:
        return f"Server(id={self.id!r}, address={self.address!r}, alias={self.alias!r})"


def new_engine(*, user='root', host='localhost', name='huahua'):
    dsn = f'mysql+pymysql://{user}@{host}/{name}'
    return create_engine(dsn, echo=True, future=True)


def add_server(engine: Engine, address, alias=None):
    with engine.connect() as conn:
        conn.execute(
            text(
                'INSERT INTO servers (address, alias) VALUES (:address, :alias)',
            ),
            [{"address": address, "alias": alias}]
        )
        conn.commit()
