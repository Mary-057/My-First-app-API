from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import register_guest, dashboard_view, GuestCreateView, GuestUpdateView, GuestDeleteView, GuestDetailView
urlpatterns = [
    path('', register_guest, name='register'),
    path('success/', views.guest_saved_success, name='saved_success'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('guest/create/', GuestCreateView.as_view(), name='guest_create'),
    path('guest/view/<int:pk>/', GuestDetailView.as_view(), name='guest_detail'),
    path('guest/update/<int:pk>/', GuestUpdateView.as_view(), name='guest_update'),
    path('guest/delete/<int:pk>/', GuestDeleteView.as_view(), name='guest_delete'),
]