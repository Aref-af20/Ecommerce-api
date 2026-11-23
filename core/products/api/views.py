from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from products.models import Product, Category
from .serializers import CategorySerializer , ProductSerializer





class ListCategories(ListAPIView):
    """List all of Category """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateCategories(generics.GenericAPIView):
    """Add and Create Category just with AdminUser."""

    serializer_class = CategorySerializer
    

    def post(self, request, *args, **kwargs):

        if not request.user.is_staff:
            return Response(
                {'message': 'Only admin user can create categories'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class RetrieveCategories(RetrieveAPIView):
    """Show one Item with primary key"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class UpdateCategories(generics.UpdateAPIView):
    """Edit and Update Categories just with AdminUser"""

    permission_classes = [IsAdminUser]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else: 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        


class DeleteCategories(DestroyAPIView):
    """Delete item only by AdminUser"""

    permission_classes = [IsAdminUser]

    queryset = Category.objects.all()


class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    