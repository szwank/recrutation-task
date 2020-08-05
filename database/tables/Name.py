from __future__ import annotations

from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from data.NameData import NameData
from .base import Base


class Name(Base):
    __tablename__ = 'name'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR)
    first = Column(VARCHAR)
    last = Column(VARCHAR)
    person_id = Column(Integer, ForeignKey('person.id'))

    person = relationship("Person", back_populates="name_relationship")

    def __repr__(self):
        return f"<Name(title={self.title}, first={self.first}, last={self.last})>"

    @classmethod
    def from_data(cls, data: NameData) -> Name:
        """Creates instance of class from NameData LoginData"""
        return cls(title=data.title,
                   first=data.first,
                   last=data.last)
