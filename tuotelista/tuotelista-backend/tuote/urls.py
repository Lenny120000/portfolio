from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from tuote import views
from .views import TuoteViewSet#,ReactLoginView, LogoutView, 
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.contrib import admin

product_router = DefaultRouter()

product_router.register(r'products', TuoteViewSet)

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('tuote/', views.TuoteList.as_view(), name='tuote-list'),
    path('tuote/<int:pk>', views.TuoteDetail.as_view(), name='tuote-detail'),
    path('tuote/uploads/', views.TuoteImage.as_view(), name='tuote-image'),
    path('tuote/ReactView', views.ReactView.as_view(), name='tuote-react'),
    #path('users/', views.UserList.as_view(), name='user-list'),
    #path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    #path('react/login/', ReactLoginView.as_view(), name='login'),
    #path('auth/logout/', LogoutView.as_view(), name='logout'),
    #path('auth/', include('rest_framework.urls')),
    #path('admin/', admin.site.urls),
]) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""path('auth/login/', LoginView.as_view(), name='login'),"""
