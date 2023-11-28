from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField()