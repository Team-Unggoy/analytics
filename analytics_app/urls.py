from django.urls import path
from analytics_app.views import LoginView
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='analytics_app/landing.html'), name="landing"),
    path('login/', LoginView.as_view(), name="login"),
    path('loginform/', LoginView.as_view(), name="login_form"),
]