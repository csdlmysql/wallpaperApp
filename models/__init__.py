from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()
__all__ = ["Image", "Tag", "User"]

class Image(Base):
    __tablename__ = "image"

    user_id = Column(Integer, ForeignKey("user.id"))
    tags = relationship("Tag")

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    link = Column(String(1000))
    created_at = Column(DateTime, default=datetime.utcnow)



class Tag(Base):
    __tablename__ = "tag"

    user_id = Column(Integer, ForeignKey("user.id"))
    image_id = Column(Integer, ForeignKey("image.id"))

    id = Column(Integer, primary_key=True)
    name = Column(String(20))


class User(Base):
    __tablename__ = "user"

    tags = relationship("Tag", back_populates="user")
    images = relationship("Image", back_populates="user")

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    email = Column(String(50))
    device = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
