from django.urls import path
from . import views

urlpatterns = [
    path('visitor/list/', views.VisitorListView.as_view(), name='visitor_list'),
    path('visitor/create/', views.VisitorCreateView.as_view(), name='visitor_create'),
    path('visitor/<int:pk>/update/', views.VisitorUpdateView.as_view(), name='visitor_update'),
    path('visitor/<int:pk>/detail/', views.VisitorDetailView.as_view(), name='visitor_detail'),
    path('visitor/<int:pk>/delete/', views.VisitorDeleteView.as_view(), name='visitor_delete'),
]
