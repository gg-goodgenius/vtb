from core.database import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String)
    email = Column(String)
    role = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean)

    card_histories = relationship("CardHistory", back_populates="user")
