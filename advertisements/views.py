from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from advertisements.permissions import IsOwner
from advertisements.models import Advertisement
from advertisements.filters import AdvertisementFilter
from advertisements.serializers import AdvertisementSerializer
from django_filters import rest_framework as filters

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action not in ["update", "partial_update", "destroy", "create"]:
            return [AllowAny()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwner(), IsAuthenticated()]
        else:
            return [IsAuthenticated()]

