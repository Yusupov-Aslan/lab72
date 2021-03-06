from django.shortcuts import render
from django.views import View

from quote.models import Quote


class IndexView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            quotes = Quote.objects.all()
        else:
            quotes = Quote.objects.filter(status='approved')
        return render(request, 'index.html', {'quotes': quotes})


class QuoteDetailView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        quote = Quote.objects.get(id=pk)
        return render(request, "quote_detail.html", {"quote": quote})
