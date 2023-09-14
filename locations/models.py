from django.db import models

# Create your models here.

class County(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class SubCounty(models.Model):
    name = models.CharField(max_length=50)
    county=models.ForeignKey(County ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
  
 

class Region(models.Model):
    name=models.CharField(max_length=60)
    subcounty=models.ForeignKey(SubCounty ,related_name='subcounty_regions',on_delete=models.CASCADE)  
    county=models.ForeignKey(County ,related_name='county_regions',on_delete=models.CASCADE)    
    is_city=models.BooleanField(default=False)

    def __str__(self):
        return self.name



