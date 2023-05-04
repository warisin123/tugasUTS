from django.shortcuts import render
from . models import JADWAL_IMSAKIYAH_1444_H
from . serializers import jadwalSerializer
# rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def readJADWAL_IMSAKIYAH_1444_H(request):
    JadwalImsyak = JADWAL_IMSAKIYAH_1444_H.objects.all()
    serializer = jadwalSerializer(JadwalImsyak, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detailJadwal(request,id):
    jadwalimsyak = JADWAL_IMSAKIYAH_1444_H.objects.get(pk=id) 
    serializer = jadwalSerializer(jadwalimsyak, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createJADWAL_IMSAKIYAH_1444_H(request):
    serializer = jadwalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateJADWAL_IMSAKIYAH_1444_H(request, id):
    JadwalImsak = JADWAL_IMSAKIYAH_1444_H.objects.get(pk=id)
    serializer = jadwalSerializer(instance=JadwalImsak, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteJADWAL_IMSAKIYAH_1444_H(request, id):
    JadwalImsak = JADWAL_IMSAKIYAH_1444_H.objects.get(pk=id)
    JadwalImsak.delete()

    
    return Response('we kampret datamu iki kehapus', status=204)

    
