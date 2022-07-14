from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import getCompanyData
from ..serializers import CompanySerializer,CompanySerializerPandas,CompanyAndDividensByPeriodSerializerPandas


class CompanyMagicFormula(APIView):

    # 1. List all
    def get(self, request, format=None):
        
        company = None     

        try:
            
            company = getCompanyData(request.query_params['stock'])

        except Exception as e:
            return Response(
            {
                "message": "Erro na obtenção de dados da empresa",
            },
            status=status.HTTP_400_BAD_REQUEST)
            
        companySerialized = CompanySerializerPandas(company, many=True)

        return Response({
            "content":companySerialized.data, 
        }, status=status.HTTP_200_OK)