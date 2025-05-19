from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review
# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
            "form": form
        })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    # Context Data. Must call super, but not need to return it.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Context works!"
        return context


class ReviewListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context


class ReviewDetailsView(TemplateView):
    template_name = "reviews/review_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get("id")
        review = Review.objects.get(id=id)
        context["title"] = f"{review.user_name}'s Review"
        context["details"] = review.review_text
        return context

# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thank_you.html")


# def review(request):
#     if request.method == "POST":

#         # existing_data = Review.objects.get(pk=1)
#         # form = ReviewForm(request.POST, instance=existing_data)

#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             # review = Review(
#             #     user_name=form.cleaned_data["user_name"], review_text=form.cleaned_data["review_text"], rating=form.cleaned_data["rating"])
#             # review.save()
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })


# def thank_you(request):
#     return render(request, "reviews/thank_you.html")
