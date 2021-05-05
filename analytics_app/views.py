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
            messages.error(request, "Invalid credentials")
            return redirect("login")
            
class DashboardView(TemplateView):
    template_name = "analytics_app/dashboard.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, {})
        else:
            messages.error(request, "Access Denied")
            return redirect("login")
        


def signup(request):
    if request.method == "POST":
        new_user = User.objects.create_user(
            username=request.POST['username'], 
            email=request.POST['email'], 
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'])
        
        if new_user:
            messages.success(request, "You have created new account. Enter credentials to login.")
            return redirect("login")
        else:
            raise("Did not create user")


def logout(request):
    auth.logout(request)
    return redirect('login')