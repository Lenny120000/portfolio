from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from tuote import views
from .views import LogoutView, TuoteViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

product_router = DefaultRouter()

product_router.register(r'products', TuoteViewSet)

urlpatterns = [
    path('tuote/', views.TuoteList.as_view()),
    path('tuote/<int:pk>', views.TuoteDetail.as_view()),
    path('tuote/uploads/', views.TuoteImage.as_view()),
    path('tuote/ReactView', views.ReactView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('api-auth/logout/', LogoutView.as_view(), name='logout'),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns) 
