from django.urls import path
from . import views

urlpatterns = [
    path('staircase/list/', views.StaircaseListView.as_view(), name='staircase_list'),
    path('staircase/create/', views.StaircaseCreateView.as_view(), name='staircase_create'),
    path('staircase/<int:pk>/update/', views.StaircaseUpdateView.as_view(), name='staircase_update'),
    path('staircase/<int:pk>/delete/', views.StaircaseDeleteView.as_view(), name='staircase_delete'),
    path('staircase/<int:pk>/detail/', views.StaircaseDetailView.as_view(), name='staircase_detail'),
]
