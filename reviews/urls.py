from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"),
    path("thank-you", views.ThankYouView.as_view(), name="thank-you"),
    path("reviews/", views.ReviewListView.as_view(), name="review-list"),
    path("reviews/favorite", views.AddFavoriteView.as_view(),
         name="favorite-review"),
    path("reviews/<int:pk>",
         views.ReviewDetailsView.as_view(), name="review-details")
]
