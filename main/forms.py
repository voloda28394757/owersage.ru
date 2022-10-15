from tkinter import Widget
from django import forms
from .models import GunsModel
class Gans_form(forms.ModelForm):
    # name=forms.CharField()
    # quality=forms.CharField()
    # discription=forms.CharField(widget=forms.Textarea)
    # price=forms.IntegerField(min_value=1, max_value=10000)
    class Meta:
        model=GunsModel
        # fields=["name", "quality", "discription", "price"]\
        fields="__all__"
        # exclude=["name"]
        widgets={"price":forms.NumberInput(attrs={"min":1, "max":10000})}


