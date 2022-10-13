from django.db import models

# Create your models here.
class Role(models.Model):
    roleid = models.IntegerField(max_length=10, primary_key=True)
    rolename = models.CharField(max_length=20)

    class Meta:
        db_table = 'role'