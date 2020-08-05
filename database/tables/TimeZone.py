from __future__ import annotations

from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from data.TimeZoneData import TimeZoneData
from .base import Base


class TimeZone(Base):
    __tablename__ = 'timezone'

    id = Column(Integer, primary_key=True)
    time = Column(VARCHAR)
    description = Column(VARCHAR)
    location_id = Column(Integer, ForeignKey('location.id'))

    location = relationship("Location", back_populates="timezone")

    def __repr__(self):
        return f"<TimeZone(time={self.time}, description={self.description})>"

    @classmethod
    def from_data(cls, data: TimeZoneData) -> TimeZone:
        """Creates instance of class from TimeZoneData object"""
        return cls(time=data.time,
                   description=data.description)
