from django.db import models



# Create your models here.
class Mobile(models.Model):
    projectname = models.CharField(max_length=100)
    username = models.CharField(max_length=120)
    workdescription = models.TextField(max_length=50)
    startdate = models.DateField()
    enddate = models.DateField()
    workhours = models.CharField(max_length=10)

    

    def _str_(self):
        return self.projectname
    
    