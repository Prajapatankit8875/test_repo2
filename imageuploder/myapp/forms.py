from django import forms
from.models import image

class imageForm(forms.ModelForm):
    class Meta:
        fields = '__all__'