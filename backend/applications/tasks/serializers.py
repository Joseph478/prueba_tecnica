from rest_framework import serializers
from .models import Task

class TaskSerializerRequest(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            # 'user',
        )
        
class TaskSerializerResponse(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
        )

class TaskSerializerPaginate(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'user',
        )