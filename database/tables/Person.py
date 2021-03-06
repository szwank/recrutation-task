from __future__ import annotations

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data.PersonData import PersonData
from .base import Base


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    gender = Column(String)
    email = Column(String)
    phone = Column(String)
    cell = Column(String)
    nat = Column(String)

    login = relationship("Login", back_populates="person")
    name = relationship("Name", back_populates="person")
    day_of_birth = relationship("DayOfBirth", back_populates="person")
    registered = relationship("Registered", back_populates="person")
    id_relationship = relationship("ID", back_populates="person")
    location = relationship("Location", back_populates="person")

    def __repr__(self):
        return f"<Person(gender={self.gender}, email={self.email}, phone={self.phone}," \
               f" cell={self.cell}, nat={self.nat})>"

    def __str__(self):
        return self.__repr__()

    def __format__(self, fmt):
        return f'{{:{fmt}}}'.format(self.__repr__())

    @classmethod
    def from_data(cls, data: PersonData) -> Person:
        """Creates instance of class from PersonData object"""
        return cls(gender=data.gender,
                   email=data.email,
                   phone=data.clean_phone_number,
                   cell=data.cell,
                   nat=data.nat)