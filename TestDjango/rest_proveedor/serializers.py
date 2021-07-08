from rest_framework import serializers
from core.models import Cliente

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'