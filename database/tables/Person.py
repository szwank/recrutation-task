from __future__ import annotations

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data.PersonData import PersonData
from .base import Base


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    gender = Column(String)
    name = Column(String)
    # location_id =
    email = Column(String)
    phone = Column(String)
    cell = Column(String)
    nat = Column(String)

    login = relationship("Login", back_populates="person")
    day_of_birth = relationship("DayOfBirth", back_populates="person")
    registered = relationship("Registered", back_populates="person")
    id_id = relationship("ID", back_populates="person")
    location = relationship("Location", back_populates="person")

    def __repr__(self):
        return f"<Person(name={self.name}, gender={self.gender}, email={self.email}, phone={self.phone}," \
               f" cell={self.cell}, nat={self.nat})>"

    @classmethod
    def from_data(cls, data: PersonData) -> Person:
        """Creates instance of class from PersonData object"""
        return cls(gender=data.gender,
                   name=data.name,
                   email=data.email,
                   phone=data.phone,
                   cell=data.cell,
                   nat=data.nat)