from django import forms
from .models import User, Test, Question, Option, UserAttempts, UserResponses
from django.db.models import Q
from django.contrib.auth import authenticate


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'mobile')
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username_text = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user_name = User.objects.filter(Q(username=username_text)).first()
        if user_name:
            username = user_name.username
        else:
            raise forms.ValidationError("No user with this username or mobile.")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Username/password is incorrect")


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('test_name', 'test_date', 'status')
        widgets = {
            'test_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Test Name'}),
            'test_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('select_test', 'text_question', 'img_question')
        widgets = {
            'text_question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type the question'}),

            'select_test': forms.TextInput(attrs={'class': 'form-control', "hidden": "hidden"}),
        }


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ('select_question', 'select_option', 'option_status')
        widgets = {
            'select_option': forms.TextInput(attrs={'class': 'form-control'}),
            'option_status': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

