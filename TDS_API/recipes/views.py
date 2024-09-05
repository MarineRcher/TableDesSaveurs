from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Recipes
from .serializers import RecipesSerializer

class CreateRecipeView(generics.CreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        # Here you can perform additional logic if needed, like associating the current user
        serializer.save(user=self.request.user)
