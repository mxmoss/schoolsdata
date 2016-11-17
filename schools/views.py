from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from schools.models import School,Performance
from schools.serializers import *


@api_view(['GET', 'POST'])
def school_list(request, format=None):
   """
   List all snippets, or create a new film.
   """
   if request.method == 'GET':
       schools = School.objects.all()
       serializedSchool = SchoolSerializer(schools, many=True)
       return Response(serializedSchool.data)

   elif request.method == 'POST':
       serializedSchool = SchoolWriteSerializer(data=request.data)
       if serializedSchool.is_valid():
           serializedSchool.save()
           return Response(serializedSchool.data, status=status.HTTP_201_CREATED)
       return Response(serializedSchool.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def school_detail(request, pk, format=None):
   """
   Retrieve, update or delete a film instance.
   """
   try:
       school = School.objects.get(pk=pk)
   except School.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

   if request.method == 'GET':
       serializer = SchoolSerializer(school)
       return Response(serializer.data)

   elif request.method == 'PUT':
       serializer = SchoolSerializer(school, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   elif request.method == 'DELETE':
       school.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def performance_list(request, format=None):
   """
   List all snippets, or create a new film.
   """
   if request.method == 'GET':
       performances = Performance.objects.all()
       serializer = PerformanceSerializer(performances, many=True)
       return Response(serializer.data)

   elif request.method == 'POST':
       serializer = PerformanceSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def performance_detail(request, pk, format=None):
   """
   Retrieve, update or delete a performance instance.
   """
   try:
       performance = Performance.objects.get(pk=pk)
   except Performance.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

   if request.method == 'GET':
       serializer = PerformanceSerializer(performance)
       return Response(serializer.data)

   elif request.method == 'PUT':
       serializer = PerformanceSerializer(performance, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   elif request.method == 'DELETE':
       performance.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)