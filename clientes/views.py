from rest_framework import viewsets, filters
from clientes.serializer import Cliente, ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['ativo']
    search_fields = ['nome', 'cpf', 'rg']
    ordering_fields = ['nome']
