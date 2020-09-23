from django.urls import path
from . import views

app_name = 'corona'

urlpatterns = [
    path('', views.index, name="index"),
    path('result/', views.PatientListView.as_view(), name="PatientListView"),
    path('detail/<int:id>', views.detail, name="detail"),
]
