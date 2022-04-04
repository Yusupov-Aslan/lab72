from django.urls import path

from quote.views import IndexView, QuoteDetailView

app_name = 'quote'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', QuoteDetailView.as_view(), name='quote_detail_view'),
]
