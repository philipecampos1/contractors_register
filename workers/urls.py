from django.urls import path
from . import views


urlpatterns = [
    path('worker/list/', views.WorkerListView.as_view(), name='worker_list'),
    path('worker/create/', views.WorkerCreateView.as_view(), name='worker_create'),
    path('worker/<int:pk>/update/', views.WorkerUpdateView.as_view(), name='worker_update'),
    path('worker/<int:pk>/delete/', views.WorkerDeleteView.as_view(), name='worker_delete'),
    path('worker/<int:pk>/detail/', views.WorkerDetailView.as_view(), name='worker_detail'),

]
