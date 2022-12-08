from django import forms
from .models import Game_Info
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Customer Create Form
class CustomerCreateForm(forms.Form):
    f_name = forms.CharField(label="First Name", max_length=20)
    l_name = forms.CharField(label="Last Name", max_length=20)
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(label="Password", max_length=20)
    age = forms.IntegerField(label="Age")


# Customer Edit Form
class CustomerEditForm(forms.Form):
    id = forms.IntegerField(label="ID")
    f_name = forms.CharField(label="First Name", max_length=20)
    l_name = forms.CharField(label="Last Name", max_length=20)
    age = forms.IntegerField(label="Age")


# Customer Delete Form
class CustomerDeleteForm(forms.Form):
    id = forms.IntegerField(label="ID")


# Employee Create Form
class EmployeeCreateForm(forms.Form):
    emp_first_name = forms.CharField(label="First Name", max_length=20)
    emp_last_name = forms.CharField(label="Last Name", max_length=20)
    emp_pay = forms.IntegerField(label="Pay")


# Employee Edit Form
class EmployeeEditForm(forms.Form):
    id = forms.IntegerField(label="ID")
    emp_first_name = forms.CharField(label="First Name", max_length=20)
    emp_last_name = forms.CharField(label="Last Name", max_length=20)
    emp_pay = forms.IntegerField(label="Pay")


# Employee Edit Form
class EmployeeDeleteForm(forms.Form):
    id = forms.IntegerField(label="ID")


class CusBuyForm(forms.ModelForm):
    class Meta:
        model = Game_Info
        fields = ['Games']


class RegisterForm(UserCreationForm):
    f_name = forms.CharField(max_length=20, label="First Name")
    l_name = forms.CharField(max_length=20, label="Last Name")
    age = forms.IntegerField()

    class Meta:
        model = User
        fields = ["f_name", "l_name", "age", "username", "password1", "password2"]
        help_texts = {'username': None, 'email': None, }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
