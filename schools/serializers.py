from rest_framework import serializers
from schools.models import *

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'SchoolID', 'School', 'DistID','District')


class PerformanceSerializer(serializers.ModelSerializer):
#   schools = SchoolSerializer()

   class Meta:
       model = Performance
       fields = ('id', 'DistrictID', 'District', 'School', 'AcademicYear', 'Subject',
       'Subgroup', 'GradeLevel', 'ParticipationRate2014to2015', 'PercentageMeetsORExceeds2014to2015')
