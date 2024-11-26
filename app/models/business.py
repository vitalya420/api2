# business.py
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Business(Base):
    __tablename__ = "businesses"

    name = Column(String, primary_key=True)
    business_admin_id = Column(ForeignKey("users.id"), nullable=False)

    business_admin = relationship(
        "User",
        back_populates="businesses_administered",
        foreign_keys=[business_admin_id],
    )
    client_associations = relationship(
        "BusinessClientAssociation", back_populates="business"
    )
