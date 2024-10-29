from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import POCData, RequestStatus, EnterpriseEngagement , ConnectionRequest , POC, FunnelData
from .serializers import POCDataSerializer, RequestStatusSerializer, EnterpriseEngagementSerializer, ConnectionRequestSerializer , POCSerializer ,FunnelDataSerializer

class POCDataListView(generics.ListAPIView):
    queryset = POCData.objects.all()
    serializer_class = POCDataSerializer

class RequestStatusListView(generics.ListAPIView):
    queryset = RequestStatus.objects.all()
    serializer_class = RequestStatusSerializer


class EnterpriseEngagementListView(generics.ListAPIView):
    queryset = EnterpriseEngagement.objects.all()
    serializer_class = EnterpriseEngagementSerializer



class ConnectionRequestView(APIView):
    def get(self, request):
        # Get connection requests data
        data = ConnectionRequest.objects.all()
        serializer = ConnectionRequestSerializer(data, many=True)
        return Response(serializer.data)
    
class POCView(APIView):
    def get(self, request):
        # Get POC data
        data = POC.objects.all()
        serializer = POCSerializer(data, many=True)
        return Response(serializer.data)
    

class FunnelDataView(APIView):
    def get(self, request):
        # Assuming you want the latest funnel data
        data = FunnelData.objects.latest('id')  # Get the latest record
        serializer = FunnelDataSerializer(data)
        return Response(serializer.data)
