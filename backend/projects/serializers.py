from rest_framework import serializers


from . import models as project_models
from users.serializers import CustomUserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project_models.Projects
        read_only_fields = ['id']
        fields = [
            'id',

            'title',
            'description',
            'banner_image',
            
            'total_budget',
            'budget_per_beneficiary',

            'start_date',
            'end_date'
        ]


class ProjectCoordinatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = project_models.ProjectCoordinators
        read_only_fields = ['id']
        fields = [
            'id',

            'project',
            'coordinator',

            'assign_date_time',
        ]


class ProjectBeneficiarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = project_models.ProjectBeneficiaries
        read_only_fields = ['id', 'benefit_receive_date_time', 'beneficiary_join_date_time']
        fields = [
            'id',

            'project',
            'beneficiary',
            'benefactor',

            'benefit_receive_date_time',
            'beneficiary_join_date_time',
        ]
