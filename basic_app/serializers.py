from rest_framework import serializers

from . import models
from .models import CustomUser, Karkas, Naduvnie, Zakaz, Kansultatsi, Kategoriya, Asosiy, Customs
from django.db.models import F


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


#

class CustomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customs
        fields = '__all__'
