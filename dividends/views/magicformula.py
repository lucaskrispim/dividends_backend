
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from ..services.magicformula import getCompaniesAndSectors
from ..models import Company,CompanyAndDividends
from ..serializers import CompanySerializerMagicFormula

class CompanyMagicFormula(APIView):
    # 1. List all
    def get(self, request, format=None):
        
        companies = None     

        try:
            
            companies,sectors = getCompaniesAndSectors()
            
            p = Paginator(companies, request.query_params['size'])
            
            page_obj = p.get_page(request.query_params['page'])

        except Exception as e:
            return Response(
            {
                "message": "Erro na obtenção de dados das empresas",
            },
            status=status.HTTP_400_BAD_REQUEST)
            
        companiesSerialized = CompanySerializerMagicFormula(page_obj, many=True)

        return Response({
            "content":companiesSerialized.data, 
            "number": int(request.query_params['page']),
            "totalElements": len(companies),
            "totalPages": int(len(companies)/int(request.query_params['size'])),
            "first": not page_obj.has_previous(),
            "last": not page_obj.has_next()
        }, status=status.HTTP_200_OK)