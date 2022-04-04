from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from . import serializers, models


def index(request):
    return render(request, 'index.html')


class ListCustomUser(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer1


class DetailCustomUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer1


class ListKarkas(generics.ListCreateAPIView):
    queryset = models.Karkas.objects.all()
    serializer_class = serializers.KarkasSerializer


class DetailKarkas(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Karkas.objects.all()
    serializer_class = serializers.KarkasSerializer


class ListNaduvnie(generics.ListCreateAPIView):
    queryset = models.Naduvnie.objects.all()
    serializer_class = serializers.NaduvnieSerializer


class DetailNaduvnie(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Naduvnie.objects.all()
    serializer_class = serializers.NaduvnieSerializer


class ListZakaz(generics.ListCreateAPIView):
    queryset = models.Zakaz.objects.all()
    serializer_class = serializers.ZakazSerializer


class DetailZakaz(generics.ListCreateAPIView):
    queryset = models.Zakaz.objects.all()
    serializer_class = serializers.ZakazSerializer


class ListKonsultatsi(generics.ListCreateAPIView):
    queryset = models.Kansultatsi.objects.all()
    serializer_class = serializers.KansultatsiySerializer


class DetailKonsultatsi(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Kansultatsi.objects.all()
    serializer_class = serializers.KansultatsiySerializer


from rest_framework_simplejwt.tokens import RefreshToken


class GetCustomToken(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        admin = self.serializer_class(data=request.data)

        if admin.is_valid():
            print(admin.validated_data)
            try:
                user = authenticate(username=admin.validated_data['username'],
                                    password=admin.validated_data['password'])
                print(user.is_active, user.is_staff, user.is_superuser, user.username, user.password)

                if user:
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        # 'is_active': str(user.is_active),
                        # 'is_staff': str(user.is_staff),
                        # 'is_superuser': str(user.is_superuser)

                    })

            except Exception as e:
                print(e)
            return Response({'detail': 'User topilmadi, qaytadan urinib ko\'ring'})
        return Response(admin.errors)
