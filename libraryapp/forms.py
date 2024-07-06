from django import forms
from django.contrib.auth.models import User




class UserResgiterationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password","email"]
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}),
            "last_name":forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),
            "username":forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            "password":forms.TextInput(attrs={'class':'form-control','placeholder':'password'}),
            "email":forms.TextInput(attrs={'class':'form-control','placeholder':'email'})
            
        }
        
        
class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username":forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            "password":forms.TextInput(attrs={'class':'form-control','placeholder':'password'})
            }
class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password","email"]
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}),
            "last_name":forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),
            "username":forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            "password":forms.TextInput(attrs={'class':'form-control','placeholder':'password'}),
            "email":forms.TextInput(attrs={'class':'form-control','placeholder':'email'})
            
        }
        
    
        