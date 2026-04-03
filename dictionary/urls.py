from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),
    path('home/', views.home, name="home"),
    path('submit/', views.submit, name="submit"),
    path('admin-panel/', views.admin_panel, name="admin_panel"),
    path('approve/<int:id>/', views.approve, name="approve"),
    path('reject/<int:id>/', views.reject, name="reject"),
]