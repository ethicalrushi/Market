from django.shortcuts import get_object_or_404, render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from rest_framework.generics import RetrieveAPIView
from django.http import JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
import json
from django.views.generic.base import View
from django.urls import resolve


class StockList(APIView):

	def get(self,request):
		stocks = Stock.objects.all()
		serializer = StockSerializer(stocks, many=True)
		return Response(serializer.data)


def index(request):
	return render(request,'index.html')