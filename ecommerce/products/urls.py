from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('',views.home, name="home"),
    path('add_category/',views.add_category, name="add_category"),
    path('category_list/',views.category_list, name="category_list"),
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)