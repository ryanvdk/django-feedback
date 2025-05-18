from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def review(request):
    if request.method == "POST":
        input_username = request.POST["username"]
        if input_username == "":
            return render(request, "reviews/review.html", {
                "has_error": True
            })

        print(input_username)
        return HttpResponseRedirect("/thank-you")
    return render(request, "reviews/review.html", {
        "has_error": False
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
