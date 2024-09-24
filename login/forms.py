from django.contrib.auth.forms import AuthenficationForm
from

class AuthForm(AuthenficationForm):
    class Meta:
        models = user
        fields = ['username', 'password']
