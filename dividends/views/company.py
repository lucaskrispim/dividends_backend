# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Company,CompanyAndDividends
from ..services import storeAllCompanies,storeDividendsByPeriodAndByCompany
from ..serializers import CompanySerializer,CompanySerializerPandas,CompanyAndDividensByPeriodSerializerPandas
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
            print("0")
            companies = Company.objects.order_by('dy').reverse()
            print("1")
            p = Paginator(companies, request.query_params['size'])
            print("2")
            page_obj = p.get_page(request.query_params['page'])
        except Exception as e:
            return Response(
            {
                "message": "Erro na obtenção de dados das empresas",
            },
            status=status.HTTP_400_BAD_REQUEST)
            
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, format=None):

        try:
            if request.query_params['action'] == "storeAll":
                storeAllCompanies()
            else:
                storeDividendsByPeriodAndByCompany()
        except Exception as e:
            return Response(
            {
                "message": "Erro no armazenamento de dados das empresas",
            },
            status=status.HTTP_400_BAD_REQUEST)

        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CompanyLastDyByPeriod(APIView):

    # 1. List all
    def get(self, request, format=None):

        companies = None     

        try:

            if request.query_params['period'] == '5y':
                companies = CompanyAndDividends.objects.order_by('dy5').reverse()
            elif request.query_params['period'] == '3y':
                companies = CompanyAndDividends.objects.order_by('dy3').reverse()
            elif request.query_params['period'] == '1y':
                companies = CompanyAndDividends.objects.order_by('dy1').reverse()
    
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
                companies = CompanyAndDividends.objects.order_by('r5').reverse()
            elif request.query_params['period'] == '3y':
                companies = CompanyAndDividends.objects.order_by('r3').reverse()
            elif request.query_params['period'] == '1y':
                companies = CompanyAndDividends.objects.order_by('r1').reverse()
    
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