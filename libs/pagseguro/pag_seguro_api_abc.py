import abc
from dataclasses import dataclass
from .serializers import SubscribeSerializer


@dataclass
class PreApprovalNotification:
    """
    {
        "name": "Teste",
        "code": "9336137C474785B004207F93F8D2C7C6",
        "date": "2022-04-29T15:53:17-03:00",
        "tracker": "71C091",
        "status": "ACTIVE",
        "reference": "16",
        "lastEventDate": "2022-04-29T15:53:18-03:00",
        "charge": "AUTO",
        "sender": {
            "name": "Paulo Roberto Cruz",
            "email": "paulo.cruz25@jurema.la",
            "phone": {
                "areaCode": "63",
                "number": "999999999"
            },
            "address": {
                "complement": "b",
                "addressRequired": true,
                "street": "Rua",
                "district": "c",
                "city": "SÃ£o FÃ©lix do Araguaia",
                "federationUnit": "MT",
                "postalCode": "78670000",
                "state": "MT",
                "number": "2",
                "country": "BRA",
                "complete": true
            }
        }
    }
    """
    name: str
    code: str
    date: str
    status: str


class PagSeguroApiABC(abc.ABC):

    @abc.abstractmethod
    def get_session(self) -> str:
        """get a pagseguro session id"""

    @abc.abstractmethod
    def subscribe(self, serializer: SubscribeSerializer) -> str:
        """create plan subscription"""

    @abc.abstractmethod
    def pre_approvals_get_notification(self, notification_code: str) -> PreApprovalNotification:
        """create plan subscription"""
