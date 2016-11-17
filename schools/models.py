from django.db import models

# Create your models here.

class School(models.Model):
    SchoolID  = models.IntegerField(blank=False)
    School  = models.CharField(max_length=65, blank=False)
    District  = models.CharField(max_length=65, blank=False)
    DistID  = models.IntegerField(blank=False)

    class Meta:
        ordering = ('School',)

    def __str__(self):
        return self.School

class Performance(models.Model):
    DistrictID = models.IntegerField()
    District = models.CharField(max_length=255, default='')
    SchoolID  = models.CharField(max_length=255, blank=True, default='')
#    School = models.ForeignKey(School)
    School = models.CharField(max_length=255)
    AcademicYear = models.IntegerField()
    Subject = models.CharField(max_length=255,  default='')
    Subgroup = models.CharField(max_length=255, default='')
    GradeLevel = models.CharField(max_length=255, default='')
    ParticipationRate2014to2015 = models.FloatField(null=True, )
    PercentageMeetsORExceeds2014to2015 = models.FloatField(null=True,)

    class Meta:
        ordering = ('School',)

    def __str__(self):
        return self.School
