from sqlalchemy import Column
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, VARCHAR
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Server(Base):
    """orm model of the stored servers"""
    __tablename__ = 'servers'

    id = Column(Integer, primary_key=True)
    address = Column(VARCHAR(512), index=True)
    alias = Column(VARCHAR(256), nullable=True, unique=True)
    description = Column(VARCHAR(1024), nullable=True)

    def __repr__(self) -> str:
        return f"Server(id={self.id!r}, address={self.address!r}, alias={self.alias!r}, description{self.description!r})"


class CraftingRule(Base):
    """orm model of the crafting rule"""
    __tablename__ = 'crafting_rules'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(512), index=True)
    recipes = relationship('CraftingRuleRecipe', back_populates='rule')


class CraftingRuleRecipe(Base):
    """orm model of the crafting rule recipe"""
    __tablename__ = 'crafting_rule_recipes'

    id = Column(Integer, primary_key=True)
    rule_id = Column(Integer, ForeignKey('crafting_rules.id'))
    name = Column(VARCHAR(512), index=True)
    count = Column(Integer)
    rule = relationship('CraftingRule')
