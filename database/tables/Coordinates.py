from __future__ import annotations

from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from data.CoordinatesData import CoordinatesData
from .base import Base


class Coordinates(Base):
    __tablename__ = 'coordinates'

    id = Column(Integer, primary_key=True)
    latitude = Column(VARCHAR)
    longitude = Column(VARCHAR)
    location_id = Column(Integer, ForeignKey('location.id'))

    location = relationship("Location", back_populates="coordinates")

    def __repr__(self):
        return f"<Coordinates(latitude={self.latitude}, longitude={self.longitude})>"

    @classmethod
    def from_data(cls, data: CoordinatesData) -> Coordinates:
        """Creates instance of class from CoordinatesData object"""
        return cls(latitude=data.latitude,
                   longitude=data.longitude)
