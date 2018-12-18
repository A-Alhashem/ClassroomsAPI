from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from classes.models import Classroom
from .models import ClassroomListSerializer, ClassroomDetailSerializer, ClassroomCreateSerializer

# Create your views here.


class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer


class ClassroomDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class ClassroomCreateView(CreateAPIView):
    serializer_class = ClassroomCreateSerializer

    def perform_create(self, serializer):
    	serializer.save(teacher=self.request.user)



class ClassroomUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'