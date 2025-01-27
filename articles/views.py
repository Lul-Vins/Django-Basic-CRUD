from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from articles.models import Article
from articles.serializers import ArticleSerializer

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()  # Todos los artículos de la base de datos
    serializer_class = ArticleSerializer

class ArticlePerID(RetrieveAPIView):
    queryset = Article.objects.all()  # Usamos `all()` porque la consulta se hace en `get_object()`
    serializer_class = ArticleSerializer

    def get_object(self):
        # Recupera el artículo según el ID pasado en la URL
        return Article.objects.get(id=self.kwargs['id'])

class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        # Esto guarda el artículo en la base de datos
        serializer.save()


class ArticleDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'

    def get_queryset(self):
        # Usamos self.kwargs['id'] para obtener el parámetro de la URL
        id = self.kwargs['id']
        # Asegúrate de filtrar el artículo por ID
        return Article.objects.filter(id=id)

class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'  # Usamos 'id' en lugar de 'pk' para el filtro

    def get_queryset(self):
        # Filtramos por el 'id' pasado en la URL
        id = self.kwargs['id']
        return Article.objects.filter(id=id)


