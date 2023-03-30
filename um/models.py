from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    location = models.TextField()

    def __str__(self):
        return self.user.username
    
    
    
class Work_experience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    company = models.CharField(max_length=220, null=True, blank=True)
    job_title = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    job_description = models.TextField()
    job_title = models.TextField()

    def __str__(self):
        return self.candidate.user.username

class Education(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    school = models.TextField()
    degree = models.TextField()
    field_of_study = models.TextField()
    graduation_date = models.DateField()
    
    def __str__(self):
        return self.candidate

class Package(models.Model):
    name = models.CharField(max_length=300, blank=False, null=True)
    
    def __str__(self):
        return self.name
    

class Package_type(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    price = models.CharField(max_length=200)
    stripe_price_id = models.CharField(max_length=40)
    
    def __str__(self):
        return self.package
    
class Package_feature(models.Model):
    package = models.ForeignKey(Package_type, on_delete=models.CASCADE)
    feature = models.TextField()

    def __str__(self):
        return self.package
    