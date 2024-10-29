from django.db import models

class POCData(models.Model):
    poc_name = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.poc_name

class RequestStatus(models.Model):
    status_type = models.CharField(max_length=50)  # e.g., 'Open', 'In Progress', 'Closed'
    count = models.IntegerField()

    def __str__(self):
        return self.status_type


class EnterpriseEngagement(models.Model):
    industry = models.CharField(max_length=100)
    engagement = models.IntegerField()

    def __str__(self):
        return f"{self.industry} - {self.engagement}"
    

class ConnectionRequest(models.Model):
    status = models.CharField(max_length=50)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.status}: {self.count}"
    

class POC(models.Model):
    status = models.CharField(max_length=50)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.status}: {self.count}"
    
    
class FunnelData(models.Model):
    request_received = models.IntegerField()
    poc_accepted = models.IntegerField()
    poc_delivered = models.IntegerField()

    def __str__(self):
        return f"FunnelData({self.request_received}, {self.poc_accepted}, {self.poc_delivered})"
