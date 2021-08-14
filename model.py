from sqlalchemy import Column
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
