from application.models import *
from django import forms
# from .models import source, user

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit, ButtonHolder


class signupForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(signupForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class loginForm(UserCreationForm):

    class Meta:

        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'fill this out',
                'username',
                'password',
            ),
        )

class preferenceForm(forms.ModelForm):
    
    class Meta:
        model = source_select
        fields = '__all__'
