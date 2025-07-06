from django.db import models

# Create your models here.
class Payment(models.Model):
    transaction_id = models.CharField(unique=True)
    amount = models.PositiveIntegerField()
    sender_phone = models.CharField(max_length=15)
    sender_name = models.CharField(max_length=100)
    transaction_time = models.DateTimeField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Confirmed ksh{self.amount} sent by{self.sender_name} at {self.received_at} received Successfully."
    