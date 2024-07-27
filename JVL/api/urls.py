from django.urls import path , include
from users.views import ProductListCreateView, ProductRetrieveUpdateDestroyView
from users.views import *
from panel.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/',profile,name='profile'),
    path('category/',category,name='category'),
    path('consumer/',consumer,name='consumer'),
    path('subcategory/',subcategory,name='subcategory'),
    # path('product/',product,name='product'),
    path('product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('order/',order,name='order'),
    path('addtocart/',addtocart,name='addtocart'),
    path('wishList/',wishList,name='wishList'),
    path('review/',review,name='review'),
    path('requests/',requests,name='requests'),
    path('consumerpanel/',consumerpanel,name='consumerpanel'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
