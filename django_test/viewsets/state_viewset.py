from rest_framework import viewsets
from http import HTTPStatus
from rest_framework.response import Response

from django_test.models.state_model import State
from django_test.serializers.state_serializer import StateSerializer


class StateViewSet(viewsets.ModelViewSet):
    pass
    # serializer_class = StateSerializer
    # queryset = State.objects.all()

    # def get_queryset(self):
    #     queryset = State.objects.all()
    #     return queryset

    # def list(self, request, *args, **kwargs):
    #     return Response('hello', HTTPStatus.ACCEPTED)
