from django import forms


# Customer Create Form
class CustomerCreateForm(forms.Form):
    f_name = forms.CharField(label="First Name", max_length=20)
    l_name = forms.CharField(label="Last Name", max_length=20)
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
