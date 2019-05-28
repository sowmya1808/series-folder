from rest_framework import serializers

class EmpSerializer(serializers.Serializer):
    ename = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=20)
