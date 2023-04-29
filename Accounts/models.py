from django.db import models

# Create your models here.

class newModel(models.Model):
   
    
    name = models.CharField(max_length=150)

    class Meta:
        db_table = "my new table for database"