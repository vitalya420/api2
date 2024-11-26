# user.py

from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from app.base.model import BaseCachableModelWithID
from app.constants import MAX_PHONE_LENGTH, MAX_PASSWORD_LENGTH, MAX_STRING_LENGTH


class User(BaseCachableModelWithID):
    __tablename__ = "users"

    phone = Column(String(MAX_PHONE_LENGTH), nullable=False, unique=True, index=True)
    first_name = Column(String(MAX_STRING_LENGTH), nullable=True)
    last_name = Column(String(MAX_STRING_LENGTH), nullable=True)
    password = Column(String(MAX_PASSWORD_LENGTH), nullable=True)
    photo = Column(String(MAX_STRING_LENGTH), nullable=True)
    is_admin = Column(Boolean, default=False)

    businesses_administered = relationship(
        "Business", uselist=False, back_populates="admin"
    )
    business_associations = relationship(
        "BusinessClientAssociation", back_populates="user"
    )
