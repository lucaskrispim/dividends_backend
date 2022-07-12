# todo/todo_api/urls.py : API urls.py
from django.urls import path
from .views import CompanyLastDy,CompanyLastDyByPeriod,CompanyLastReturnByPeriod,CompanyTest,CompanyMagicFormula

urlpatterns = [
    path('api/test', CompanyTest.as_view()),
    path('api', CompanyLastDy.as_view()),
    path('api/companiesanddividendsbyperiod', CompanyLastDyByPeriod.as_view()),
    path('api/companiesandreturnsbyperiod', CompanyLastReturnByPeriod.as_view()),
    path('api/companiesmagicformula', CompanyMagicFormula.as_view()),
]