from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from basic_app import views

urlpatterns = [
    path('user/', views.ListCustomUser.as_view()),
    path('user/<int:pk>', views.DetailCustomUser.as_view()),
    path('tokens/', views.GetCustomToken.as_view()),
    path('product/', views.ListKarkas.as_view()),
    path('product/<int:pk>', views.DetailKarkas.as_view()),
    path('naduvnie/', views.ListNaduvnie.as_view()),
    path('naduvnie/<int:pk>', views.DetailNaduvnie.as_view()),
    path('zakaz/', views.ListZakaz.as_view()),
    path('zakaz/<int:pk>', views.DetailZakaz.as_view()),
    path('kansultatsi/', views.ListKonsultatsi.as_view()),
    path('kansultatsi/<int:pk>', views.DetailKonsultatsi.as_view()),
    path('kategoriya/', views.ListKategoriya.as_view()),
    path('kategoriya/<int:pk>', views.DetailKategoriya.as_view()),
    path('asosiy/', views.ListAsosiy.as_view()),
    path('asosiy/<int:pk>', views.DetailAsosiy.as_view()),

    path('auth-token/', TokenObtainPairView.as_view()),
    path('auth-verify/', TokenVerifyView.as_view()),
    path('auth-refresh/', TokenRefreshView.as_view()),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
