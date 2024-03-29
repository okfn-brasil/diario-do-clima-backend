from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from libs.services import services
from libs.querido_diario import QueridoDiarioABC


class CNPJPartnersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        cnpj = kwargs.get('cnpj', None)
        if cnpj is None:
            raise ValidationError({'cnpj': 'cnpj deve ser informado'})
            
        querido_diario: QueridoDiarioABC = services.get(QueridoDiarioABC)
        data = querido_diario.cnpj_list_partners(cnpj=cnpj)
        return Response(data)
