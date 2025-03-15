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