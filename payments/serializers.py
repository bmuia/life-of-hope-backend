from rest_framework import serializers 
from .models import Payment
from .utils import is_valid_phone_number

class MpesaPaymentValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['sender_phone', 'amount']

    def validate(self, data):
        if data['amount'] <= 0:
            raise serializers.ValidationError('Amount must not be less than 0')
        
        if not is_valid_phone_number(data['sender_phone']):
            raise serializers.ValidationError("Phone number must be valid and start with +254...")
        
        return data
    

        
