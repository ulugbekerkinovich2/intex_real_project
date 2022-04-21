from rest_framework import serializers

from . import models
from .models import CustomUser, Karkas, Naduvnie, Zakaz, Kansultatsi, Kategoriya, Asosiy


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    # is_active = serializers.BooleanField()
    # is_staff = serializers.BooleanField()
    # is_superuser = serializers.BooleanField()
    # password = serializers.CharField(style={'input_type': 'password'})
    # is_superuser = serializers.BooleanField()


class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = 'id', 'username', 'password', 'is_active', 'is_staff', 'is_superuser'

    def create(self, validated_data):
        return models.CustomUser.objects.create_user(**validated_data)


class KarkasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karkas
        fields = '__all__'


class NaduvnieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Naduvnie
        fields = '__all__'


class ZakazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zakaz
        fields = '__all__'


class KansultatsiySerializer(serializers.ModelSerializer):
    class Meta:
        model = Kansultatsi
        fields = '__all__'


class KategotiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoriya
        fields = '__all__'


class AsosiySerializer(serializers.ModelSerializer):
    class Meta:
        model = Asosiy
        fields = '__all__'
