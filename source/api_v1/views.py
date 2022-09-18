import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from webapp.models import Article


class LikesView(LoginRequiredMixin, View):

    def get(self, request, *args, pk, **kwargs):
        article = Article.objects.get(pk=pk)
        user = self.request.user
        if user in article.likes.all():
            article.likes.remove(user)
        else:
            article.likes.add(user)

        return JsonResponse({"count": article.likes.count()})
