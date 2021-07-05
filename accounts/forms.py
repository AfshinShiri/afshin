from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'نام کاربری خود را وارد کنید'}) )
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'ایمیل خود را وارد کنید'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'نام خود را وارد کنید'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی خود را وارد کنید'}))
    password_1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'کلمه عبور را وارد کنید'}))
    password_2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'کلمه عبور را مجدد وارد کنید'}))

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError(' این نام کاربری از قبل وجود دارد')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(' این ایمیل از قبل وجود دارد')
        return email

    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2:
            raise forms.ValidationError('پسورد های وارد شده هماهنگ نیستند')
        elif len(password2) < 8:
            raise forms.ValidationError('پسورد شما حداقل باید 8 کاراکتر باشد')
        elif not any(x.isupper() for x in password2):
            raise forms.ValidationError('لطفا در پسورد خود حداقل از یک حروف بزرگ استفاده کنید')

        return password1

class UserLoginForm(forms.Form):
    user = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'نام کاربری یا ایمیل خود را وارد کنید'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'کلمه عبو خود را وارد کنید'}))