import re
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(forms.Form):
    '''
    Form
    '''
    username = forms.CharField(label=_(u'Username'), max_length=30)
    email = forms.EmailField(label=_(u'Email'))
    password1 = forms.CharField(
        label=u'Password',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label=u'Password (Again)',
        widget=forms.PasswordInput()
    )

    '''
    Password validation
    '''

    def clean_password2(self):
        if 'password1' in self.changed_data:
            password1 = self.changed_data['password1']
            password2 = self.cleaned_data['password2']

            if password1 == password2:
                return password2
            raise forms.ValidationError('Passwords do not match.')

    '''
    Username validation
    '''

    def clean_username(self):
        username = self.changed_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')
