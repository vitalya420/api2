# user.pyi
from typing import Optional, List

from app.base.model import BaseCachableModelWithID
from app.models.associations import BusinessClientAssociation
from app.models.business import Business

class User(BaseCachableModelWithID):
    phone: str
    password: str
    photo: Optional[str]
    is_admin: bool

    businesses_administered: Optional[Business]
    business_associations: List[BusinessClientAssociation]
