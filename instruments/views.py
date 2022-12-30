from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Instrument
from .serializers import InstrumentSerializer
from dacapo_api.permissions import IsOwnerOrReadOnly


class InstrumentList(APIView):
    """
    This view lists all instruments and authenticated users can create a
    new item to sell.
    The method below (perform_create) binds the creator of an item as the owner
    to that entry.
    """

    serializer_class = InstrumentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        instruments = Instrument.objects.all()
        serializer = InstrumentSerializer(
            instruments, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = InstrumentSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class InstrumentDetail(APIView):
    """
    This view lists an individual instrument by its id.
    The view contains methods to get, update and delete an item, if the user
    is also the owner.
    """
    serializer_class = InstrumentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            instrument = Instrument.objects.get(pk=pk)
            self.check_object_permissions(self.request, instrument)
            return instrument
        except Instrument.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        instrument = self.get_object(pk)
        serializer = InstrumentSerializer(
            instrument, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        instrument = self.get_object(pk)
        serializer = InstrumentSerializer(
            instrument, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        instrument = self.get_object(pk)
        instrument.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
