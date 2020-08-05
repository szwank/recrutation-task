from __future__ import annotations

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from data.DayOfBirthData import DayOfBirthData
from .base import Base


class DayOfBirth(Base):
    __tablename__ = 'day_of_birth'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    age = Column(Integer)
    days_to_birthday = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))

    person = relationship("Person", back_populates="day_of_birth")

    def __repr__(self):
        return f"<DayOfBirth(date={self.date}, age={self.age}, days_to_birthday={self.days_to_birthday})>"

    @classmethod
    def from_data(cls, data: DayOfBirthData) -> DayOfBirth:
        """Creates instance of class from DayOfBirthData object"""
        return cls(date=data.date,
                   age=data.age,
                   days_to_birthday=data.days_to_birthday)
