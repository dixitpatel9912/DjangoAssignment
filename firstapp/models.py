from django.db import models

# Create your models here.
'''
class Login(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Login"


class Python(models.Model):
    Session = models.CharField(max_length=40)

    def __str__(self):
        return self.Session

    class Meta:
        verbose_name_plural = "Python"


class Student(models.Model):
    name = models.CharField(max_length=40, unique=False)
    Session = models.ForeignKey("Python", on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Student"
'''


class Update_data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    verify_email = models.EmailField(max_length=50)
    text = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
