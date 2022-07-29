from rest_framework import viewsets, mixins

from .models import *
from .serializers import *
from .permissions import IsSuperUserOrStaffEditAndAuthenticatedReadOnly


class BeneficiariesViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):
    queryset = Beneficiaries.objects.all()
    serializer_class = BeneficiarySerializer
    permission_classes = [IsSuperUserOrStaffEditAndAuthenticatedReadOnly]


class DistrictViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [IsSuperUserOrStaffEditAndAuthenticatedReadOnly]


class ThanaViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):
    queryset = Thana.objects.all()
    serializer_class = ThanaSerializer
    permission_classes = [IsSuperUserOrStaffEditAndAuthenticatedReadOnly]


class PostCodeViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):
    queryset = PostCode.objects.all()
    serializer_class = PostCodeSerializer
    permission_classes = [IsSuperUserOrStaffEditAndAuthenticatedReadOnly]


class WardViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    permission_classes = [IsSuperUserOrStaffEditAndAuthenticatedReadOnly]


class VillageViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [IsSuperUserOrStaffEditAndAuthenticatedReadOnly]


class BeneficiaryAddressViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):
    queryset = BeneficiaryAddress.objects.all()
    serializer_class = BeneficiaryAddressSerializer
    permission_classes = [IsSuperUserOrStaffEditAndAuthenticatedReadOnly]
