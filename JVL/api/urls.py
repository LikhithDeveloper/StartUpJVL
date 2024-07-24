from django.urls import path , include
from users.views import *
from panel.views import *

urlpatterns = [
    path('profile/',profile,name='profile'),
    path('category/',category,name='category'),
    path('consumer/',consumer,name='consumer'),
    path('subcategory/',subcategory,name='subcategory'),
    path('product/',product,name='product'),
    path('order/',order,name='order'),
    path('addtocart/',addtocart,name='addtocart'),
    path('wishList/',wishList,name='wishList'),
    # path('review/',review,name='review'),
    path('requests/',requests,name='requests'),
    path('consumerpanel/',consumerpanel,name='consumerpanel'),
]
