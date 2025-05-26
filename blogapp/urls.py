from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('myblogs/', myblogs, name='myblogs'),
    path('create_blog/', BlogCreateView.as_view(), name='add'),
    path('<int:pk>/update_blog/', BlogUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete_blog/', BlogDeleteView.as_view(), name='delete'),
    # API url
    path('api/v1/', CreateListBlog.as_view(), name='api_product'),
    path('api/v1/<int:pk>/', UpDelRetBlog.as_view(), name='api_product'),
]
