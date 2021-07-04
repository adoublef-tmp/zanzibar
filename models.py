from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # organization_id = Column(Integer, ForeignKey("organizations.id"))
    # organization = relationship("Organization", backref="repositories", lazy=True)


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # organization_id = Column(Integer, ForeignKey("organizations.id"))
    # organization = relationship("Organization", backref="teams", lazy=True)


class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(Text)
    closed = Column(Boolean, default=False)

    # repository_id = Column(Integer, ForeignKey("repositories.id"))
    # repository = relationship("Repository", backref="issues", lazy=True)
    # reporter_id = Column(Integer, ForeignKey("users.id"))
    # reporter = relationship("User", backref="issues_created", lazy=True)
