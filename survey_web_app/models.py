# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("氏名",max_length=128)
    age = models.IntegerField("年齢",null=True)
    answer_1 = models.TextField("好きな映画とその理由",max_length=512,null=True)
    answer_2 = models.TextField("好きなお店とその理由",max_length=512,null=True)
    creation_dt = models.DateField("",default=timezone.now,null=True)
