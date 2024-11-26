# associations.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.base.model import BaseModelWithID


class BusinessClientAssociation(BaseModelWithID):
    __tablename__ = "business_client_association"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    business_id = Column(Integer, ForeignKey("businesses.id"), nullable=False)

    user = relationship("User", back_populates="business_associations")
    business = relationship("Business", back_populates="client_associations")
