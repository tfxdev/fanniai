from django.db import models
from django.contrib.auth.models import User
from um import managers


class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    location = models.TextField()
    objects = managers.CandidateManager()

    def __str__(self):
        return self.user.username


class WorkExperience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    company = models.CharField(max_length=220, null=True, blank=True)
    job_title = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    job_description = models.TextField()
    job_title = models.TextField()

    objects = managers.WorkExperienceManager()

    def __str__(self):
        return self.candidate.user.username


class Education(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    school = models.TextField()
    degree = models.TextField()
    field_of_study = models.TextField()
    graduation_date = models.DateField()

    objects = managers.EducationManager()

    def __str__(self):
        return self.candidate.user.username


class Package(models.Model):
    name = models.CharField(max_length=300, blank=False, null=True)
    sub_title = models.CharField(max_length=30, blank=False)
    price = models.IntegerField()
    feature = models.TextField()
    stripe_price_id = models.CharField(max_length=40)

    def __str__(self):
        return self.package.name


class PackageFeature(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    feature = models.CharField(max_length=255)

    def __str__(self):
        return self.package.name
