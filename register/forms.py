from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import Users


class UForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    phoneno = forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
    c_password=forms.CharField(max_length=100)

    def clean_username(self):
        print("checking name")
        username = self.cleaned_data['username']
        name_l = username.lower()
        r = Users.objects.filter(username=username)
        print(r.count())
        if len(name_l)<4:
            raise ValidationError("MINIMUM 4 CHARACTERS FOR USERNAME!!")
        if r.count():
            raise  ValidationError("USERNAME ALREADY TAKEN!!")
        return name_l


    def clean_phoneno(self):
        print("checking phoneno")
        phoneno = self.cleaned_data['phoneno']
        r=Users.objects.filter(phoneno=phoneno)
        print(r.count())
        if len(phoneno)!=10:
            raise ValidationError("ENTER VALID PHONE NUMBER!!")
        if r.count():
            raise  ValidationError("PHONE NUMBER ALREADY TAKEN!!")
        return phoneno


    def clean_email(self):
        print("checking email")
        email = self.cleaned_data['email']
        r = Users.objects.filter(email=email)
        print(r.count())
        if r.count():
            raise ValidationError("EMAIL ALREADY TAKEN!!")
        return email

    def clean_password(self):
        password=self.cleaned_data['password']
        if len(password)<8:
            raise ValidationError("MINUMUM 8 CHARACTERS FOR PASSWORD!!")

        return password

    def clean_c_password(self):
        c_password=self.cleaned_data['c_password']
        if len(c_password)<8:
            raise ValidationError("MINUMUM 8 CHARACTERS FOR PASSWORD!!")

        return c_password

    def clean(self):
        print("checking passwords")
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('c_password')

        if password1 and password2 and password1 != password2:
            raise ValidationError("TYPE THE SAME PASSWORDS!!")

        return password2


class MsgForm(forms.Form):
    message = forms.CharField(max_length=100000)


    def clean_username(self):
        print("checking name")
        message = self.cleaned_data['message']
        return message

class SearchForm1(forms.Form):
    user = forms.CharField(max_length=30)


    def clean_user(self):
        user = self.cleaned_data['user']
        return user


class SearchForm2(forms.Form):
    user_=forms.CharField(max_length=30)

    def clean_user1(self):
        user_=self.cleaned_data['user_']
        return user_


   

   