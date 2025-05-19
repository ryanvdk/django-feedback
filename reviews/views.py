from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .forms import ReviewForm
from .models import Review
# Create your views here.


class ReviewView(CreateView):
    model = Review
    # Alternatively to declaring the fields, you can declare a form_class and point to the custom created form.
    # form_class = ReviewForm
    # fields = "__all__"
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"

#     # Override the form_valid form to manipulate validated data.
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request, "reviews/review.html", {
#             "form": form
#         })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    # Context Data. Must call super, but not need to return it.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Context works!"
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    # Without this the data is exposed to the template as object_list
    context_object_name = "reviews"

    # Can still add methods to get more control.

    # get_queryset allows you to filter the data to display
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gte=4)
    #     return data

# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context


class ReviewDetailsView(DetailView):
    # This View type uses the primary key to identify which item to access. "reviews/<int:pk>"
    # Data is accessible in the tamplate through the model name or the "object" keyword
    template_name = "reviews/review_details.html"
    model = Review


# class ReviewDetailsView(TemplateView):
#     template_name = "reviews/review_details.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # id = self.kwargs.get("id")
#         review_id = kwargs["id"]
#         review = Review.objects.get(id=review_id)
#         context["title"] = f"{review.user_name}'s Review"
#         context["details"] = review.review_text
#         context["rating"] = review.rating
#         return context

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
