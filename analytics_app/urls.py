from django.urls import path
from analytics_app.views import LoginView, logout, DashboardView, signup
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='analytics_app/landing.html'), name="landing"),
    path('login/', TemplateView.as_view(template_name='analytics_app/login.html'), name="login"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('signup/', TemplateView.as_view(template_name='analytics_app/signup.html'), name="signup"),
    
    path('logout/', logout, name="logout"),
    path('loginform/', LoginView.as_view(), name="login_form"),
    path('signupform/', signup, name="signup_form"),
]