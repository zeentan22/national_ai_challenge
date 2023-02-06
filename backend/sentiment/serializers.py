from rest_framework import serializers
from .models import History, Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"

class HistorySerializer(serializers.ModelSerializer):
    history_data = DataSerializer(many=True)

    class Meta:
        model = History
        fields = [
            'time',
            'history_data',
        ]
        write_only_fields = ["user_input"]
    
    def create(self, validated_data):
        history_data = validated_data.pop("history_data")
        history_instance = History.objects.create(**validated_data)
        
        for data in history_data:
            Data.objects.create(history=history_instance, **data) # point FK to history instance
        
        return history_instance