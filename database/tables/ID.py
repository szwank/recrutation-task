from __future__ import annotations

from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from data.IDData import IDData
from .base import Base


class ID(Base):
    __tablename__ = 'id'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)
    value = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))

    person = relationship("Person", back_populates="id_id")

    def __repr__(self):
        return f"<ID(name={self.name}, value={self.value})>"

    @classmethod
    def from_data(cls, data: IDData) -> ID:
        """Creates instance of class from IDData object"""
        return cls(name=data.name,
                   value=data.value)

