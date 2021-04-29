from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.views.generic import TemplateView, CreateView
from django.views import View

class LoginView(View):
    template_name = 'analytics_app/dashboard.html'

    def post(self, request, *args, **kwargs):
        crdntls = {
            "usr": request.POST['usr'],
            "pwd": request.POST['pwd']
        }
        user = auth.authenticate(username = crdntls['usr'], password=crdntls['pwd'])
        if user:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("login")
            
class DashboardView(TemplateView):
    template_name = "analytics_app/dashboard.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, {})
        else:
            messages.info(request, "Access Denied")
            return redirect("login")
        


class SignupView(CreateView):
    model = User

def logout(request):
    auth.logout(request)
    return redirect('login')