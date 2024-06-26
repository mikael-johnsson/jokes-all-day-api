from rest_framework import permissions, generics
from .models import Report
from .serializers import ReportSerializer
from jokes_main.permissions import IsOwnerOrReadOnly


class ReportList(generics.ListCreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Report.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Report.objects.all()