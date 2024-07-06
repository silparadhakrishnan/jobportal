from django.shortcuts import render,redirect
from django.views import View
from libraryapp.forms import UserResgiterationForm,UserLoginForm,UserEditForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.generic import UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'

class UserHomeView(TemplateView):
    template_name='userhome.html'

class UserRegisterView(View):
    def get(self,request):
        form=UserResgiterationForm()
        return render(request,'register.html',{'form':form})
    def post(self,request):
        form=UserResgiterationForm(request.POST)
        if form.is_valid():
            formdata=form.cleaned_data
            User.objects.create_user(**formdata)
            return HttpResponse("registered")
        else:
            return HttpResponse("invalid")
        
        
class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            return redirect('userhome_view')
        else:
            return HttpResponse("invalid")
        
class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home_view')

class UserprofileView(View):
    def get(self,request,*args,**kwargs):
        user=User.objects.filter(username=request.user)
        return render(request,'user_profile.html',{'user':user})
class UserEditView(UpdateView):
    model=User
    template_name='useredit.html'
    form_class=UserEditForm
    pk_url_kwarg='id'
    success_url=reverse_lazy('userhome_view')
    
    
class UserDeleteView(DeleteView):
    model=User
    template_name='userdelete.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('userhome_view')
    
    

    
    
    

        
        
        

        
    
