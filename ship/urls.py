# urls.py
from django.urls import path
from .views import (
    UploadFileView, TitanicListView, TitanicCreateView,
    TitanicUpdateView, TitanicDeleteView, TitanicTableView
)

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    path('titanic/', TitanicListView.as_view(), name='titanic_list'),
    path('titanic/create/', TitanicCreateView.as_view(), name='titanic_create'),
    path('titanic/update/<int:pk>/', TitanicUpdateView.as_view(), name='titanic_edit'),
    path('titanic/delete/<int:pk>/', TitanicDeleteView.as_view(), name='titanic_delete'),
    path('titanic/table/', TitanicTableView.as_view(), name='titanic_table'),
]
