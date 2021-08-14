from typing import List
import sqlalchemy
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import select
from model import Server


class ServerList:
    """Server list interface"""
    async def resolve(self, alias: str) -> Server:
        """Resolve server by alias"""
        pass

    async def add(self, server: Server):
        pass

    async def all(self) -> List[Server]:
        pass


class AliasConflictException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__('Alias duplicated')


class DatabaseServerList(ServerList):
    """Server list presisted by a database"""

    def __init__(self, engine: Engine):
        self.engine = engine

    async def resolve(self, alias: str) -> Server:
        with Session(self.engine) as session:
            return session.query(Server).filter_by(alias=alias).first()

    async def add(self, server: Server):
        try:
            with Session(self.engine) as session:
                session.add(server)
                session.commit()
                return
        except sqlalchemy.exc.IntegrityError as err:
            # assume this is a duplicated error because currently the only constraint is the UNIQUE index of the alias column
            raise AliasConflictException() from err

    async def all(self) -> List[Server]:
        with Session(self.engine) as session:
            return session.query(Server).limit(100).all()
