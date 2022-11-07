from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from company import views

urlpatterns = [
    path('company/', views.CompanyList.as_view()),
    path('company/<str:pk>/', views.CompanyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
