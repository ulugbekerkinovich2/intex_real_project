# Create your views here.
from django.contrib.auth import authenticate
from django.db.models import Count
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, filters, permissions, status

from . import serializers, models
from .serializers import UserSerializer1


def index(request):
    return render(request, 'index.html')


class ListCustomUser(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer1


class DetailCustomUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserPasswordSerializer

    # @api_view(['PATCH'])
    # @permission_classes([permissions.IsAuthenticated])
    # def patch(request):
    #     if request.method == 'PATCH':
    #         serializer = UserSerializer1(request.CustomUser, data=request.data, partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #         return Response(status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)


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
    # queryset = models.Zakaz.objects.filter(active='True')
    queryset = models.Zakaz.objects.all()
    serializer_class = serializers.ZakazSerializer

    # m = models.Karkas.objects.filter(nechtaligi__gte=1)
    #
    # print(queryset)
    # a = models.Zakaz.objects.filter(active="True").count()
    # print(a)
    # if queryset:
    #     a1 = a - 1
    #
    #     print(a1)
    #     v = models.Zakaz.objects.filter().delete()
    #     print(a1)

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
                        'username': str(user.username),
                        # 'is_staff': str(user.is_staff),
                        # 'is_superuser': str(user.is_superuser)

                    })

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
