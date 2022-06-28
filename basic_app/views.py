# Create your views here.
from django.contrib.auth import authenticate
from django.db.models import Count
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, filters, permissions, status
import random
from . import serializers, models
from .serializers import UserSerializer1


def index(request):
    from hashlib import sha256
    h = sha256()
    h1 = sha256()
    h.update(b'pythonintexstaff')
    h1.update(b'shahzodyovqochevadmin')
    hash = h.hexdigest()
    hash1 = h1.hexdigest()
    print(hash)
    print(hash1)
    # 3027cff872b877cecba79292ff911fd3d293d737d632c8f6cc2dbcce6bb98959
    # ccbf593217b5ba77f5ca47e7b1e9c9a82e73c65ba407ba801a446d81922f1b1a

    return render(request, 'index.html')


class ListCustomUser(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer1


class DetailCustomUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserPasswordSerializer


class ListKarkas(generics.ListCreateAPIView):
    queryset = models.Karkas.objects.filter(nechtaligi__gte=1)
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

    filter_backends = [filters.SearchFilter]
    search_fields = ['date_time']


class DetailZakaz(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Zakaz.objects.all()
    serializer_class = serializers.ZakazSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['date_time']


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
        from hashlib import sha256
        staff = sha256()
        super = sha256()
        staff.update(b'pythonintexstaff')
        super.update(b'shahzodyovqochevadmin')
        hash_staff = staff.hexdigest()
        hash_super = super.hexdigest()
        # print(hash_staff)
        # print(hash_super)
        admin = self.serializer_class(data=request.data)

        if admin.is_valid():
            # print(admin.validated_data)
            try:
                user = authenticate(username=admin.validated_data['username'],
                                    password=admin.validated_data['password'])
                # print(user.is_active, user.is_staff, user.is_superuser, user.username, user.password)

                if user:
                    if (user.is_active == True) and (user.is_staff == True) and (user.is_superuser == False):
                        refresh = RefreshToken.for_user(user)
                        return Response({
                            'refresh': str(refresh),
                            'access': str(refresh.access_token),
                            'username': str(user.username),
                            'is_active': user.is_active,
                            'is_staff': user.is_staff,
                            'is_superuser': user.is_superuser,
                            'hash_code for staff': hash_staff

                        })
                    print(user.is_active)
                    if (user.is_active == True) and (user.is_staff == True) and (user.is_superuser == True):
                        refresh = RefreshToken.for_user(user)
                        return Response({
                            'refresh': str(refresh),
                            'access': str(refresh.access_token),
                            'username': str(user.username),
                            'is_active': user.is_active,
                            'is_staff': user.is_staff,
                            'is_superuser': user.is_superuser,
                            'status_admin': hash_super

                        })
                    print(user.is_active)



            except Exception as e:
                print(e)
            return Response({'detail': 'User topilmadi, qaytadan urinib ko\'ring'})
        return Response(admin.errors)


class ListKategoriya(generics.ListCreateAPIView):
    queryset = models.Kategoriya.objects.all()
    serializer_class = serializers.KategotiyaSerializer


class DetailKategoriya(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Kategoriya.objects.all()
    serializer_class = serializers.KategotiyaSerializer


class ListAsosiy(generics.ListCreateAPIView):
    queryset = models.Asosiy.objects.all()
    serializer_class = serializers.AsosiySerializer


class DetailAsosiy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Asosiy.objects.all()
    serializer_class = serializers.AsosiySerializer


class ListCustoms(generics.ListCreateAPIView):
    queryset = models.Customs.objects.all()
    serializer_class = serializers.CustomsSerializer


class DetailCustoms(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customs.objects.all()
    serializer_class = serializers.CustomsSerializer
