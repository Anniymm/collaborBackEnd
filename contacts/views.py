from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import contactsUs
from .serializers import contactsUsSerializer

class contactsUsView(APIView):
    def get(self, request):
        contact_info = contactsUs.objects.first()
        if contact_info:
            serializer = contactsUsSerializer(contact_info)
            return Response(serializer.data)
        return Response({'error': 'Contact information not found'}, status=404)

    def post(self, request):
        self.check_permissions(request) 
        serializer = contactsUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk=None):
        self.check_permissions(request)  
        contact_info = contactsUs.objects.first()
        if not contact_info:
            return Response({'error': 'Contact information not found'}, status=404)

        serializer = contactsUsSerializer(contact_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(contactsUsView, self).get_permissions()
