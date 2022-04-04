from rest_framework import serializers
from quote.models import Quote

LIKE = 'like'
DISLIKE = 'dislike'
RateChoices = (
    (LIKE, 'Лайк'),
    (DISLIKE, 'Дизлайк')
)


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class QuoteChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ("status",)


class QuoteRateSerializer(serializers.Serializer):
    rate = serializers.ChoiceField(choices=RateChoices)
