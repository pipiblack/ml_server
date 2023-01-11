from rest_framework import serializers
from apps.endpoints.models import Endpoint
from apps.endpoints.models import MLAlgorithm
from apps.endpoints.models import MLAlgorithmstatus
from apps.endpoints.models import MLRequests

class EndpointSerializer(serializers.ModelSerializer):
    class meta:
        model = Endpoint
        read_only_fields = {"id","name","owner","Time_created"}
        fields = read_only_fields

class MLAlgorithmSerializer(serializers.ModelSerializer):
    current_status = serializers.SerializerMethodField(read_only=True)

    def get_current_status(self,MLalgorithm):
                return MLAlgorithmstatus.objects.filter(parent_mlalgorithm=MLalgorithm).latest('created_at').status
    class meta:
        model = MLAlgorithm
        read_only_fields = {"name","description","code","version","Time_created","parent_endpoint"}
        fields = read_only_fields

class MLAlgorithmstatusSerializer(serializers.ModelSerializer):
    class meta:
        model = MLAlgorithmstatus
        read_only_fields = {"id","active"}
        fields = ("id", "active", "status", "created_by", "created_at", "parent_mlalgorithm")



class MLRequestsSerializer(serializers.ModelSerializer):
    class meta:
        model = MLRequests
        read_only_fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "created_at",
            "parent_mlalgorithm",
        )
        fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "created_at",
            "parent_mlalgorithm",
        )




