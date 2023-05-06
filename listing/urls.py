from django.urls import path
from . import views

urlpatterns = [
 path('listing/', views.ContactList.as_view()),
 path('Llsting_detail/<int:pk>/', views.ListingDetail.as_view()),

]

