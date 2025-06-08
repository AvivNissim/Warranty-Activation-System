
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base
import enum


Base = declarative_base()

class WarrantyStatus(str, enum.Enum):
  pending = "pending"
  approved = "approved"
  rejected = "rejected"
  manual_review = "manual_review"


class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  user_name = Column(String, unique=True, index=True, nullable=False)
  hashed_password = Column(String, nullable=False)
  is_admin = Column(Boolean, nullable=False, default = 0)
  warranties = relationship("Warranty", back_populates="installer")


class Warranty(Base):
  __tablename__ = "warranties"
  id = Column(Integer, primary_key=True, index=True)
  customer_name = Column(String, nullable=False)
  product_name = Column(String, nullable=False)
  installation_date = Column(String, nullable=False)
  invoice_path = Column(String, nullable=False)
  status = Column(Enum(WarrantyStatus), default=WarrantyStatus.pending)
  installer_id = Column(Integer, ForeignKey("users.id"))
  installer = relationship("User", back_populates="warranties")


