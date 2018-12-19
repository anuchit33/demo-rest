# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from customer.serializers import *
from rest_framework import generics
from customer.models import Customer
from rest_framework import permissions
from customer.pagination import LargeResultsSetPagination


class UserViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# class CustomerListView(generics.ListCreateAPIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
    
#     serializer_class = CustomerListSerializer

#     def get_queryset(self):

#         queryset = Customer.objects.all().order_by('-id')
#         code = self.request.query_params.get('code', None)

#         if code is not None:
#             queryset = queryset.filter(code = code)
#         return queryset

class CustomerListView(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerListSerializer
    pagination_class = LargeResultsSetPagination

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-id')

    def get_serializer_class(self):
        
        if self.request.method =='GET':
            return CustomerDetailSerializer
        else:
            return CustomerUpdateSerializer
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # permissions.IsAuthenticated,