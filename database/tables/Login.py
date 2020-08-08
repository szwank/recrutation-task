from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from data.LoginData import LoginData
from database.types.String import String as StringRegex

class Login(Base):
    __tablename__ = 'login'

    id = Column(Integer, primary_key=True)
    uuid = Column(String)
    username = Column(String)
    password = Column(StringRegex)
    salt = Column(String)
    md5 = Column(String)
    sha1 = Column(String)
    sha256 = Column(String)
    person_id = Column(Integer, ForeignKey('person.id'))

    person = relationship("Person", back_populates="login")

    def __repr__(self):
        return f"<Login(uuid={self.uuid}, username={self.username}, password={self.password}," \
               f" salt={self.salt}, md5={self.md5}, sha1={self.sha1}, sha256={self.sha256})>"

    @classmethod
    def from_data(cls, data: LoginData) -> Login:
        """Creates instance of class from LoginData LoginData"""
        return cls(uuid=data.uuid,
                   username=data.username,
                   password=data.password,
                   salt=data.salt,
                   md5=data.md5,
                   sha1=data.sha1,
                   sha256=data.sha256)
