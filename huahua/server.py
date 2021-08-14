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


class DatabaseServerList(ServerList):
    """Server list presisted by a database"""

    def __init__(self, engine: Engine):
        self.engine = engine

    async def resolve(self, alias: str) -> Server:
        with Session(self.engine) as session:
            server = session.execute(
                select(Server).filter_by(alias=alias),
            ).scalar_one()
            if server:
                return server
            else:
                return session.execute(select(Server).filter_by(alias=alias)).scalar_one()

    async def add(self, server: Server):
        with Session(self.engine) as session:
            session.add(server)
            session.flush()
            return
