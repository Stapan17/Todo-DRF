from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import todo
from .serializers import todoSerializer


@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': 'todo-lists/',
        'Details View': 'todo-lists/<str:pk>/',
        'Create': 'todo-create',
    }

    return Response(api_urls)


@api_view(['GET'])
def todoLists(request):
    tasks = todo.objects.all()
    serializer = todoSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def todoDetails(request, pk):
    task = todo.objects.get(id=pk)
    serializer = todoSerializer(task, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
    serializer = todoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def todoUpdate(request, pk):
    task = todo.objects.get(id=pk)
    serializer = todoSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def todoDelete(request, pk):
    task = todo.objects.get(id=pk)
    task.delete()

    return Response("Todo Deleted Successfully!!")
