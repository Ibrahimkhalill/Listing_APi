from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from listing.models import *
from listing.serializers import ListingSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import  viewsets
from django.db.models import Q
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ListingPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class ContactList(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    pagination_class = ListingPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location','bathrooms','amenities']
    
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes =[TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['price']
    # ordering = ['price']
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        property = self.get_object()
        if property.owner == request.user:
            return self.destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

  
    




  