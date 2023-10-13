from core.database import Base
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Bank(Base):
    __tablename__ = "bank"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    address = Column(String)
    city = Column(String)
    have_vip = Column(Boolean)
    have_ramp = Column(Boolean)
    have_prime = Column(Boolean)
    lat = Column(Float)
    lon = Column(Float)
    for_person = Column(Boolean)
    for_juridical = Column(Boolean)

    schedule = relationship("Schedule", back_populates="bank")


class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True, index=True)

    day = Column(Integer)
    start_time = Column(Integer)
    end_time = Column(Integer)
    for_person = Column(Boolean)

    bank = relationship("Bank", back_populates="schedule")
    bank_id = Column(Integer, ForeignKey("bank.id"))
