from django.urls import path
from . import views


urlpatterns = [
    path('contractor/list/', views.ContractorListView.as_view(), name='contractor_list'),
    path('contractor/create/', views.ContractorCreateView.as_view(), name='contractor_create'),
    path('contractor/<int:pk>/detail/', views.ContractorDetailView.as_view(), name='contractor_detail'),
    path('contractor/<int:pk>/update/', views.ContractorUpdateView.as_view(), name='contractor_update'),
    path('contractor/<int:pk>/delete/', views.ContractorDeleteView.as_view(), name='contractor_delete'),
]
