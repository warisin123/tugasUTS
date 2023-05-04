from rest_framework import serializers
from . models import JADWAL_IMSAKIYAH_1444_H 
class jadwalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JADWAL_IMSAKIYAH_1444_H
        fields = "__all__"
