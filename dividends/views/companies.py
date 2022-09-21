# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Company,CompanyAndDividends
from ..serializers import CompanySerializer,CompanySerializerPandas,CompanyAndDividensByPeriodSerializerPandas
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

b3 =  ['IRBR3',	'BBAS3',	'EMBR3',	'AZUL4',	'HYPE3',	'YDUQ3',	'BRKM5',	'GOLL4',	'MRFG3',	'SOMA3',	'ABEV3',	'BBSE3','ENBR3','LWSA3','COGN3',	'CVCB3',
'DXCO3',	'CPLE6',	'CMIG4',	'SBSP3','LREN3',	'BBDC4','ELET3','JHSF3','ELET6',	'POSI3',	'RADL3',	'CIEL3',	'EGIE3',	'AMER3',	'CCRO3',	'RAIL3',	
'JBSS3',	'ASAI3','ITSA4',	'TIMS3',	'CRFB3',	'BBDC3',	'QUAL3',	'CPFE3',	'BEEF3',	'FLRY3',	'MULT3',	'SLCE3',	'MRVE3',	'PETR4','TOTS3',	'UGPA3',	
'ECOR3',	'ITUB4',	'CYRE3', 'VBBR3', 'RENT3',	'BRML3',	'VIIA3',	'VIVT3',	'PCAR3',	'CSAN3', 'BRFS3', 'SUZB3', 'B3SA3', 'EZTC3',	 'CASH3',	'PETR3',	
'BPAN4',	'MGLU3',	'PETZ3',	'WEGE3',	'ENEV3',	'HAPV3',	'RRRP3', 'GOAU4', 'USIM5',	'EQTL3',	'BRAP4', 'GGBR4', 'NTCO3',	 'PRIO3', 'CMIN3',	'ALPA4',	
'VALE3', 'RDOR3',	 'CSNA3']

class CompanyTest(APIView):
    def get(self, request, format=None):
        return Response(
            {
                "msg": "Ok estamos no ar",
            },
            status=status.HTTP_200_OK)


class CompanyLastDy(APIView):

    # 1. List all
    def get(self, request, format=None):
        
        companies = None     

        try:
            
            companies = Company.objects.filter(abbreviation__in=b3).order_by('dy').reverse()
            
            p = Paginator(companies, request.query_params['size'])
            
            page_obj = p.get_page(request.query_params['page'])
        except Exception as e:
            return Response(
            {
                "message": "Erro na obtenção de dados das empresas",
            },
            status=status.HTTP_400_BAD_REQUEST)
            
        companiesSerialized = CompanySerializerPandas(page_obj, many=True)
        return Response({
            "content":companiesSerialized.data, 
            "number": int(request.query_params['page']),
            "totalElements": len(companies),
            "totalPages": int(len(companies)/int(request.query_params['size'])),
            "first": not page_obj.has_previous(),
            "last": not page_obj.has_next()
        }, status=status.HTTP_200_OK)

class CompanyLastDyByPeriod(APIView):

    # 1. List all
    def get(self, request, format=None):

        companies = None     

        try:

            if request.query_params['period'] == '5y':
                companies = CompanyAndDividends.objects.filter(abbreviation__in=b3).order_by('dy5').reverse()
            elif request.query_params['period'] == '3y':
                companies = CompanyAndDividends.objects.filter(abbreviation__in=b3).order_by('dy3').reverse()
            elif request.query_params['period'] == '1y':
                companies = CompanyAndDividends.objects.filter(abbreviation__in=b3).order_by('dy1').reverse()
    
            p = Paginator(companies, request.query_params['size'])
            page_obj = p.get_page(request.query_params['page'])
            
        except Exception as e:
            return Response(
            {
                "message": "Erro na obtenção de dados das empresas",
            },
            status=status.HTTP_400_BAD_REQUEST)

        companiesSerialized = CompanyAndDividensByPeriodSerializerPandas(page_obj,many=True)

        return Response(companiesSerialized.data, status=status.HTTP_200_OK)

class CompanyLastReturnByPeriod(APIView):

    # 1. List all
    def get(self, request, format=None):

        companies = None     

        try:

            if request.query_params['period'] == '5y':
                companies = CompanyAndDividends.objects.filter(abbreviation__in=b3).order_by('r5').reverse()
            elif request.query_params['period'] == '3y':
                companies = CompanyAndDividends.objects.filter(abbreviation__in=b3).order_by('r3').reverse()
            elif request.query_params['period'] == '1y':
                companies = CompanyAndDividends.objects.filter(abbreviation__in=b3).order_by('r1').reverse()
    
            p = Paginator(companies, request.query_params['size'])
            page_obj = p.get_page(request.query_params['page'])
        except Exception as e:
            return Response(
            {
                "message": "Erro na obtenção de dados das empresas",
            },
            status=status.HTTP_400_BAD_REQUEST)

        companiesSerialized = CompanyAndDividensByPeriodSerializerPandas(page_obj,many=True)

        return Response(companiesSerialized.data, status=status.HTTP_200_OK)