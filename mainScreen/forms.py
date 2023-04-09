from django import forms

from django.core.exceptions import ValidationError
import json

class ReviewFields(forms.Form):
    jsonfield = forms.CharField(widget=forms.Textarea(attrs={"rows":"20",'cols':'100'}))
