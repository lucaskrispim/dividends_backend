from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import getCandleStickByCompanyData,getDividendsByCompanyData,getRsiByCompanyData
from ..serializers import StockSerializerPandas,StockCandleSerializerPandas,RsiSerializerPandas
import json

class CandlestickByStock(APIView):

    # 1. List all
    def get(self, request, format=None):
        
        company = None     

        try:
            company = getCandleStickByCompanyData(request.query_params['stock'])
        except Exception as e:
            return Response(
            {
                "message": "Erro na obtenção de dados da empresa",
            },
            status=status.HTTP_400_BAD_REQUEST)
        
        companyCandleSerialized = StockCandleSerializerPandas(company, many=True)
        
        return Response(companyCandleSerialized.data,status=status.HTTP_200_OK)


class DividendsByStock(APIView):

    # 1. List all
    def get(self, request, format=None):
        
        company = None     

        try:
            dividends = getDividendsByCompanyData(request.query_params['stock'])
        except Exception as e:
            return Response(
            {
                "message": "Erro na obtenção de dados da empresa",
            },
            status=status.HTTP_400_BAD_REQUEST)

        companyDividendsSerialized = StockSerializerPandas(dividends, many=True)

        return Response(companyDividendsSerialized.data, status=status.HTTP_200_OK)

class IndicatorByStock(APIView):

    # 1. List all
    def get(self, request, format=None):
        
        rsi = None     

        try:
            rsi = getRsiByCompanyData(request.query_params['stock'])
        except Exception as e:
            return Response(
            {
                "message": "Erro na obtenção de dados da empresa",
            },
            status=status.HTTP_400_BAD_REQUEST)
        
        rsiSerialized = RsiSerializerPandas(rsi, many=True)
        
        return Response(rsiSerialized.data,status=status.HTTP_200_OK)