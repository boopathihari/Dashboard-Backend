from rest_framework import serializers
from .models import POCData, RequestStatus, EnterpriseEngagement, ConnectionRequest, POC, FunnelData

class POCDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = POCData
        fields = ['poc_name', 'task', 'start_date', 'end_date']

class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestStatus
        fields = ['status_type', 'count']


class EnterpriseEngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseEngagement
        fields = ['industry', 'engagement']



class ConnectionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionRequest
        fields = ['status', 'count']


class POCSerializer(serializers.ModelSerializer):
    class Meta:
        model = POC
        fields = ['status', 'count']



class FunnelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunnelData
        fields = ['request_received', 'poc_accepted', 'poc_delivered']