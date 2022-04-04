from django.urls import path

from quote.views import IndexView

app_name = 'quote'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
