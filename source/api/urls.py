from django.urls import path
from api import views

app_name = "api"

urlpatterns = [
    path('quotes/', views.QuoteListAPIView.as_view(), name='quote_list'),
    path('quote/create/', views.QuoteCreateAPIView.as_view(), name='quote_create'),
    path('quote/<int:pk>/detail/', views.QuoteDetailAPIView.as_view(), name='quote_detail'),
    path('quote/<int:pk>/update/', views.QuoteUpdateAPIView.as_view(), name='quote_update'),
    path('quote/<int:pk>/delete/', views.QuoteDeleteAPIView.as_view(), name='quote_delete'),
    path('quote/<int:pk>/rate/', views.QuoteRateAPIView.as_view(), name='quote_rate'),
]
