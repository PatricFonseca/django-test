from rest_framework import serializers


class StateSerializer(serializers.Serializer):
    state = serializers.CharField()

    def create(self, validated_data):
        return validated_data
