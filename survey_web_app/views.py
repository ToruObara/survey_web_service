from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView,ListView
from . import forms
from . import models

class CreationView(CreateView):
    model = models.Question
    form_class = forms.QuestionForm
    template_name = "Creation.html"
    success_url = "/"

class AllDeleteView(ListView):
#    models.Question.objects.all().delete()
    model = models.Question
    template_name = "List.html"
    def get_queryset(self):
        models.Question.objects.all().delete()
        queryset = models.Question.objects.all()
        return queryset

class ListDataView(ListView):
    model = models.Question
    template_name = "List.html"
