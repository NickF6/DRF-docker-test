from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Customer, Book
from .serializers import CustomerSerializer, BookSerializer
from rest_framework.decorators import action
from datetime import timedelta
from django.utils import timezone

class CustomerModelViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=['get'], detail=False)
    def last_week(self, request):
        end_date = timezone.now().date() + timedelta(days=1)
        start_date = timezone.now().date() - timedelta(days=6)
        last_week = self.queryset.filter(created_at__range=[start_date, end_date])
        serializer = self.get_serializer_class()(last_week, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def last_fornight(self, request):
        end_date = timezone.now().date() + timedelta(days=1)
        start_date = timezone.now().date() - timedelta(days=13)
        last_week = self.queryset.filter(created_at__range=[start_date, end_date])
        serializer = self.get_serializer_class()(last_week, many=True)
        return Response(serializer.data)
