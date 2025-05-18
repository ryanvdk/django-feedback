from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
# Create your views here.


def review(request):
    # if request.method == "POST":
    #     input_username = request.POST["username"]
    #     if input_username == "":
    #         return render(request, "reviews/review.html", {
    #             "has_error": True
    #         })

    #     print(input_username)
    #     return HttpResponseRedirect("/thank-you")

    form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
