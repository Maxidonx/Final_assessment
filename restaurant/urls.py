from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import (
    BookingViewSet,
    UserViewSet,
    UserListCreateView,
    UserDetailView,
    register,
    get_user,
    update_user,
    delete_user,
    home,
    about,
    reservations,
    book,
    menu,
    display_menu_item,
    bookings,
)

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'users', UserViewSet)
# router.register(r'users', UserListCreateView)
# router.register(r'users',  UserDetailView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', register, name='register_user'),
    path('api/get_user/<int:user_id>/', get_user, name='get_user'),
    path('api/update_user/<int:user_id>/', update_user, name='update_user'),
    path('api/delete_user/<int:user_id>/', delete_user, name='delete_user'),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reservations/', views.reservations, name='reservations'),
    path('book/', views.book, name='book'),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/',views.display_menu_item, name='display_menu_item'),
    path('bookings/', views.bookings, name='bookings'), 
]