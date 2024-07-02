from django.urls import path
from report import views

urlpatterns = [
    path('report/', views.ReportList.as_view()),
    path('report/<int:pk>/', views.ReportDetail.as_view())
]
