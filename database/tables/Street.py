from __future__ import annotations

from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from data.StreetData import StreetData
from .base import Base


class Street(Base):
    __tablename__ = 'street'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    name = Column(VARCHAR)
    location_id = Column(Integer, ForeignKey('location.id'))

    location = relationship("Location", back_populates="street")

    def __repr__(self):
        return f"<TimeZone(time={self.time}, description={self.description})>"

    @classmethod
    def from_data(cls, data: StreetData) -> Street:
        """Creates instance of class from StreetData object"""
        return cls(number=data.number,
                   name=data.name)
