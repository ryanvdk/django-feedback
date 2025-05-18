from django import forms

# Convention to end name with "Form"


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "Your Name must not be blank.",
        "max_length": "Please enter a shorter name."
    })
