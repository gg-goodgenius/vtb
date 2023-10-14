from core.database import Base
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

bank_services_link = Table(
    "bank_services_link",
    Base.metadata,
    Column("bank_id", ForeignKey("bank.id"), primary_key=True),
    Column("bankservice_id", ForeignKey("bankservice.id"), primary_key=True),
)


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
    services = relationship("BankService", secondary="bank_services_link", back_populates="banks")


class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True, index=True)

    day = Column(Integer)
    start_time = Column(Integer)
    end_time = Column(Integer)
    for_person = Column(Boolean)

    bank = relationship("Bank", back_populates="schedule")
    bank_id = Column(Integer, ForeignKey("bank.id"))


class BankService(Base):
    __tablename__ = "bankservice"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    time = Column(Integer)

    banks = relationship("Bank", secondary="bank_services_link", back_populates="services")
