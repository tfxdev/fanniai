from django.db import models
from django.db.models import Q


class CandidateQueryset(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (
                Q(phone__icontains=query)
                | Q(location__icontains=query)
                | Q(user__username__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs


class CandidateManager(models.Manager):
    def get_queryset(self):
        return CandidateQueryset(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class WorkExperienceQueryset(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (
                Q(company__icontains=query)
                | Q(job_title__icontains=query)
                | Q(candidate__phone__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs


class WorkExperienceManager(models.Manager):
    def get_queryset(self):
        return WorkExperienceQueryset(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class EducationQueryset(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (
                Q(candidate__phone__icontains=query)
                | Q(school__icontains=query)
                | Q(degree__icontains=query)
                | Q(field_of_study__icontains=query)
                | Q(graduation_date__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs


class EducationManager(models.Manager):
    def get_queryset(self):
        return EducationQueryset(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)
