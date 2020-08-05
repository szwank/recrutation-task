from __future__ import annotations

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from data.RegisteredData import RegisteredData
from .base import Base


class Registered(Base):
    __tablename__ = 'registered'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    age = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))

    person = relationship("Person", back_populates="registered")

    def __repr__(self):
        return f"<Registered(date={self.date}, age={self.age})>"

    @classmethod
    def from_data(cls, data: RegisteredData) -> Registered:
        """Creates instance of class from RegistereData object"""
        return cls(date=data.date,
                   age=data.age)
