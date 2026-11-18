from django.db import models

# Create your models here.


class emp_table(models.Model):
    eid= models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=20)
    emp_salary= models.FloatField()