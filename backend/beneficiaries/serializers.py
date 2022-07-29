from rest_framework import serializers

from .models import Beneficiaries, BeneficiaryAddress, District, Thana, PostCode, Ward, Village


class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiaries
        read_only_fields = ['id', 'last_updated_at', 'created_at',]
        fields = [
            'id',

            'first_name',
            'last_name',
            'date_of_birth',
            'phone_number',

            'profile_picture',
            'description',

            'last_updated_at',
            'created_at',
        ]


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        read_only_fields = ['id']
        fields = ['name', 'description']


class ThanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thana
        read_only_fields = ['id']
        fields = ['name', 'description']


class PostCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCode
        read_only_fields = ['id']
        fields = ['name', 'description']


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        read_only_fields = ['id']
        fields = ['name', 'description']


class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        read_only_fields = ['id']
        fields = ['name', 'description']


class BeneficiaryAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BeneficiaryAddress
        read_only_fields = ['id', 'beneficiary']
        fields = [
            'id',

            'beneficiary',

            'district',
            'thana',
            'post_code',
            'ward',
            'village',
        ]
