from rest_framework import viewsets, mixins


from .models import Projects, ProjectCoordinators, ProjectBeneficiaries
from .serializers import ProjectSerializer, ProjectCoordinatorSerializer, ProjectBeneficiarySerializer
from .permissions import IsAdminEditOrAuthenticatedReadOnly


class ProjectsViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin
):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminEditOrAuthenticatedReadOnly]


class ProjectCoordinatorsViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = ProjectCoordinators.objects.all()
    serializer_class = ProjectCoordinatorSerializer
    permission_classes = [IsAdminEditOrAuthenticatedReadOnly]


class ProjectBeneficiariesViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = ProjectBeneficiaries.objects.all()
    serializer_class = ProjectBeneficiarySerializer
    permission_classes = [IsAdminEditOrAuthenticatedReadOnly]
