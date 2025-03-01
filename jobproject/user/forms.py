from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import CustomUser

#
# class Customusercreationform(UserCreationForm):
#     role_choice=[('Employee','Employee'),('Company','Company')]
#     role=forms.ChoiceField(choices=role_choice,widget=forms.Select,required=True)
#     class Meta:
#         model=User
#         fields=UserCreationForm.Meta.fields+('role')