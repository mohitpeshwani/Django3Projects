from django import forms
from employee.models import Feedback
class FeedbackForm(forms.ModelForm):
    class Meta:
        model =Feedback
        fields = ['name','email','feedback']