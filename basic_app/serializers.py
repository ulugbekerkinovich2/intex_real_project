from rest_framework import serializers, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from . import models
from .models import CustomUser, Karkas, Naduvnie, Zakaz, Kansultatsi, Kategoriya, Asosiy, Customs
from django.db.models import F


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(style={'input_type': 'username'})
    password = serializers.CharField(style={'input_type': 'password'})
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

    # def update(self, instance, validated_data):
    #     return models.CustomUser.objects.make_password(validated_data, instance, self)


class UserPasswordSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'password',
            'username',
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"write_only": True},
        }

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


import requests

API_TOKEN = '5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA'


class KarkasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karkas
        fields = '__all__'

    # def create(self, validated_data):
    #     ob = models.Karkas.objects.create(**validated_data)
    #     print(ob)
    #     chats = [935920479]
    #     # a = [1, 2, 3]
    #     for id in chats:
    #         requests.get(
    #             url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id={id}&parse_mode=HTML&text={ob}")
    #     return ob


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


class CustomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customs
        fields = '__all__'


