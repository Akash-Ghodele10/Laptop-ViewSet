
from rest_framework import viewsets
from .models import LenovoData
from .serializer import LenovoSerializer



class LenovoView(viewsets.ModelViewSet):
    queryset = LenovoData.objects.all()
    serializer_class = LenovoSerializer


