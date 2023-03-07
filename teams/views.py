from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import TeamSerializer
from .models import Teams


# Create your views here.
@api_view(['GET'])
def get_teams(request):
    teams = Teams.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_team(request, pk):
    team = Teams.objects.get(name=pk)
    serializer = TeamSerializer(team, many=False)
    return Response(serializer.data)
