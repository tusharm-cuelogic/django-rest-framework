from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from resttutorial.apiquickstart.serializers import UserSerializer, GroupSerializer, MyuserSerializer

from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class myuserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = MyuserSerializer
    # queryset = User.objects.all().order_by('-date_joined')
    # # print "=====>>>", queryset
    # data = serializers.serialize('json', queryset)
    # return HttpResponse(data, content_type='application/json')
    # # return HttpResponse(json.dumps(data), content_type="application/json")
    # # return JsonResponse(data, safe=False)
