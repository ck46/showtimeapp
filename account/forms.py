from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser


class SignUpForm(UserCreationForm):
	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name','profileImages', 'iucnumber' , 'decodertype',  'phonenumber', 'email', 'password1', 'password2')


# class SignUpForm(UserCreationForm):
# 	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

# 	class Meta:
# 		model = CustomUser
# 		fields = ('username','firstname', 'surname', 'email', 'decodertype', 'decodernumber', 'password1', 'password2')


# class CustomUserCreationForm(UserCreationForm):

# 	class Meta:
# 		model = CustomUser
# 		fields = ('username','firstname', 'surname', 'email', 'decodertype', 'decodernumber', 'password1', 'password2')
