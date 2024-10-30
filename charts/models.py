from django.db import models

class POCData(models.Model):
    poc_name = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.poc_name

class RequestStatus(models.Model):
    status_type = models.CharField(max_length=50)  
    count = models.IntegerField()

    def __str__(self):
        return self.status_type


class UserStatus(models.Model):
    status_type = models.CharField(max_length=50)  
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

class SessionData(models.Model):
    SESSION_QUARTERS = [
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4'),
    ]
    USER_TYPES = [
        ('Startup', 'Startup'),
        ('Enterprise', 'Enterprise'),
    ]

    quarter = models.CharField(max_length=2, choices=SESSION_QUARTERS)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    session_duration = models.FloatField()  
