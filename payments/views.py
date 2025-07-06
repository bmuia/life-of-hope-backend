from rest_framework import status
from .serializers import MpesaPaymentValidationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class MpesaPaymentValidationView(APIView):
    def post(self,request):
        serializer = MpesaPaymentValidationSerializer(data=request.data)

        if serializer.is_valid():
            return Response({
                "ResultCode": 0,
                "ResultDesc": "Accepted"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "ResultCode": 1,
                "ResultDesc": "Rejected",
                "Errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

