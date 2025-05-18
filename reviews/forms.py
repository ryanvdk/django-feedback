from django import forms

# Convention to end name with "Form"


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name")
