from django.urls import path
from . import views

urlpatterns = [
    # --- Category URLs ---
    path('categories/', views.ListCategories.as_view(), name='category-list'),
    path('categories/create/', views.CreateCategories.as_view(), name='category-create'),
    path('categories/<int:pk>/', views.RetrieveCategories.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', views.UpdateCategories.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.DeleteCategories.as_view(), name='category-delete'),

    # --- Product URLs ---
    path('products/', views.ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]