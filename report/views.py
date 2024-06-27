from rest_framework import permissions, generics
from .models import Report
from .serializers import ReportSerializer
from jokes_main.permissions import IsOwnerOrReadOnly


class ReportList(generics.ListCreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Report.objects.all()
        else:
            return Report.objects.filter(author=user)  

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Report.objects.all()
        else:
            return Report.objects.filter(author=user) 