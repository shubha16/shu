from django.db import models


class Student1(models.Model):

    name = models.CharField(max_length=50)
    email_id = models.EmailField()
    contact_no = models.CharField(max_length=11)
    dat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
