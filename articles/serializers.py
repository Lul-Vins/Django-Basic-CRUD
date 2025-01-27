from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article  # Modelo al que está asociado
        fields = '__all__'  # Incluir todos los campos del modelo
