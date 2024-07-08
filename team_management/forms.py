from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Booking
from .models import Players,Booking,Coaches

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DateInput(forms.DateInput):
    input_type = 'date'
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date':DateInput(),
        }

class PlayersForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = ['player_name','img','coach_name','description']


class CoachForm(forms.ModelForm):
    class Meta:
        model = Coaches
        fields = '__all__'