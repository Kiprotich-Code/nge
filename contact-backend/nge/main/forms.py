from django import forms
from .models import WaitList

# Create your forms here 
class WaitListForm(forms.ModelForm):
    class Meta:
        model = WaitList
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={
              'class': 'form-control',
              'placeholder': 'example@gmail.com'  
            }),

            'message': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Please leave us a message!',
                'rows': 10
            }),
        }