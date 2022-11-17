from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ItemSerializer
from .mixins import SerializerByMethodMixin
from .models import Item



class ListCreateItemView(SerializerByMethodMixin, ListCreateAPIView):

    queryset = Item.objects.all()
    serializer_map = {
        "GET": ItemSerializer,
        "POST": ItemSerializer,
    }


class RetrieveUpdateItemView(RetrieveUpdateDestroyAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Create your views here.
