# -*- coding: utf-8 -*-
from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ("name","age","answer_1","answer_2")
        exclude = ("id","creation_dt")
