from django import forms

# Convention to end name with "Form"


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "Your Name must not be blank.",
        "max_length": "Please enter a shorter name."
    })

    review_text = forms.CharField(
        label="Your feedback", widget=forms.Textarea, max_length=200)

    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
