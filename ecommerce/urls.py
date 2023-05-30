
from django.urls import path
from . import views
from .views import CategoryView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path("category/<slug:val>",views.CategoryView.as_view(),name='category'),
    path("category-title/<val>",views.CategoryTitle.as_view(),name='category-title'),
    path("product-detail/ <int:pk>",views.ProductDetail.as_view(),name='product-detail'),
    path('profile/' ,views.CustomerProfile,name='profile'),
    path('address/' ,views.address,name='address'),
    path('address/' ,views.address,name='address'),
    path('updateaddress/<int:pk>/', views.UpdateAddress, name='updateaddress'),
   
    # login authrntication
    
    path('register',views.register ,name='register'), 
    path('login',views.login ,name='login'), 
    
    # path('logout',views.logout,name='logout')
    
   
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


