from __future__ import annotations

from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from data.LocationData import LocationData
from .base import Base


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    city = Column(VARCHAR)
    state = Column(VARCHAR)
    country = Column(VARCHAR)
    postcode = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))

    person = relationship("Person", back_populates="location")
    coordinates = relationship("Coordinates", back_populates="location")
    timezone = relationship("TimeZone", back_populates="location")

    def __repr__(self):
        return f"<Location(city={self.city}, state={self.state}, country={self.country}, postcode={self.postcode})>"

    @classmethod
    def from_data(cls, data: LocationData) -> Location:
        """Creates instance of class from LocationData object"""
        return cls(city=data.city,
                   state=data.state,
                   country=data.country,
                   postcode=data.postcode,
                   )
