from django.urls import path
from . import views


urlpatterns = [
    path('work_type/list/', views.WorkTypeListView.as_view(), name='work_type_list'),
    path('work_type/create/', views.WorkTypeCreateView.as_view(), name='work_type_create'),
    path('work_type/<int:pk>/detail/', views.WorkTypeDetailView.as_view(), name='work_type_detail'),
    path('work_type/<int:pk>/update/', views.WorkTypeUpdateView.as_view(), name='work_type_update'),
    path('work_type/<int:pk>/delete/', views.WorkTypeDeleteView.as_view(), name='work_type_delete'),
]
