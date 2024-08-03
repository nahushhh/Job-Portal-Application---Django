from django import forms

class CompanyLoginForm(forms.Form):
    email = forms.EmailField(label="Email", required=True, max_length=50)
    password = forms.CharField(label="Password", required=True, max_length=20)

