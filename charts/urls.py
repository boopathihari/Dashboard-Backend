from django.urls import path
from .views import POCDataListView, RequestStatusListView,EnterpriseEngagementListView,ConnectionRequestView,POCView, FunnelDataView

urlpatterns = [
    path('poc-data/', POCDataListView.as_view(), name='poc-data'),
    path('request-status/', RequestStatusListView.as_view(), name='request-status'),
    path('enterprise-engagement/', EnterpriseEngagementListView.as_view(), name='enterprise-engagement'),
    path('connection-requests/', ConnectionRequestView.as_view(), name='connection-requests'),
    path('poc/', POCView.as_view(), name='poc-list'),
    path('funnel/', FunnelDataView.as_view(), name='funnel-data'),
]
