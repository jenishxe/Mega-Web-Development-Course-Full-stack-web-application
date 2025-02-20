from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(required=True, label="Full Name", help_text='Enter your fullname!')
    rating = forms.IntegerField(min_value=1, max_value=5)
    text = forms.CharField(label='Your Feedback!', widget=forms.Textarea, max_length=200)
