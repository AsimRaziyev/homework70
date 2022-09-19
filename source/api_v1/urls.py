from django.urls import path, include

from api_v1.views import LikesView

app_name = "api_v1"

urlpatterns = [
    path('likes/<int:pk>/', LikesView.as_view(), name="likes"),

]
