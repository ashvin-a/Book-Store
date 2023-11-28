from django import forms
from .models import Review
# class ReviewForm(forms.Form):
    # username = forms.CharField(label="Your name",max_length=100,error_messages={
    #     "required":"Your name musnt be empty",
    #     "max_length":"Its too lengthy" #Used for custom error msg 
    # })
    # review_text = forms.CharField(widget=forms.Textarea,label="Your feedback",
    #                               max_length=500)
    # rating = forms.IntegerField(min_value=1,max_value=10,label="Your Rating")
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'#You could mention specific fields using ['','']
        # exlude = ['']