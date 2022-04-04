from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsStaffPermission
from api.serializers import QuoteSerializer, QuoteChangeSerializer, QuoteRateSerializer, LIKE, DISLIKE
from rest_framework import permissions
from rest_framework import generics

from quote.models import Quote


class QuoteListAPIView(generics.ListAPIView):
    serializer_class = QuoteSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        if self.request.user.is_aunthenticated and self.request.user.is_staff:
            return Quote.objects.all()
        return Quote.objects.filter(approved=True)


class QuoteCreateAPIView(generics.CreateAPIView):
    serializer_class = QuoteSerializer
    permission_classes = (permissions.AllowAny,)


class QuoteDetailAPIView(generics.RetrieveAPIView):
    serializer_class = QuoteSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Quote.objects.all()

    def get_queryset(self):
        if self.request.user.is_aunthenticated and self.request.user.is_staff:
            return Quote.objects.all()
        return Quote.objects.filter(approved=True)


class QuoteUpdateAPIView(generics.UpdateAPIView):
    serializer_class = QuoteChangeSerializer
    permission_classes = (IsStaffPermission,)
    queryset = Quote.objects.all()


class QuoteDeleteAPIView(generics.DestroyAPIView):
    permission_classes = (IsStaffPermission,)
    queryset = Quote.objects.all()


class QuoteRateAPIView(generics.UpdateAPIView):
    serializer_class = QuoteRateSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Quote.objects.filter(approved=True)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data.get('rate') == LIKE:
            instance.rating += 1
        elif serializer.validated_data.get('rate') == DISLIKE:
            instance.rating -= 1
            instance.save()
        return Response(QuoteSerializer(instance).data)
