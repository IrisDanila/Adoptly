from django import forms
from .models import AdoptionRequest

class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['name', 'email', 'phone', 'about_you', 'reason_for_adoption', 'experience_with_pets']
        widgets = {
            'about_you': forms.Textarea(attrs={'rows': 3}),
            'reason_for_adoption': forms.Textarea(attrs={'rows': 3}),
            'experience_with_pets': forms.Textarea(attrs={'rows': 3}),
        }



class BreedDetectionForm(forms.Form):
    image = forms.ImageField(label="Upload an image of the dog")

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'name',
            'date_of_birth',
            'age',
            'species',
            'breed',
            'description',
            'image',
            'is_available',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }