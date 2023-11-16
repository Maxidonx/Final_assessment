from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Booking, Menu
from .serializers import UserSerializer, BookingSerializer
from .forms import BookingForm
from datetime import datetime
from django.shortcuts import render
import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework import viewsets
from rest_framework import generics, status




class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def register(request):
    """
    Register a new user.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(request, user_id):
    """
    Retrieve user details.
    """
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, user_id):
    """
    Update user details.
    """
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # Ensure that the authenticated user is updating their own details
    if request.user != user:
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, user_id):
    """
    Delete user account.
    """
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Ensure that the authenticated user is deleting their own account
    if request.user != user:
        return Response(status=status.HTTP_403_FORBIDDEN)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# def reservations(request):
#     date = request.GET.get('date', datetime.today().date())
#     bookings = Booking.objects.filter(BookingDate=date)
#     # booking_json = serializers.serialize('json', bookings)
#     # # bookings = Booking.objects.filter(BookingDate=date)
#     serializer = BookingSerializer(bookings, many=True)
#     serialized_data = serializer.data
#     return render(request, 'bookings.html',{"bookings":serialized_data})
def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()(BookingDate=date)
    serializer = BookingSerializer(bookings, many=True)
    serialized_data = serializer.data
    return render(request, 'bookings.html', {"bookings": serialized_data})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 


@api_view(['POST'])
@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        exist = Booking.objects.filter(
            reservation_date=data['reservation_date'],
            reservation_slot=data['reservation_slot']
        ).exists()

        if not exist:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
            return JsonResponse({'success': True}, status=201)
        else:
            return JsonResponse({'error': 1}, status=400)

    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return JsonResponse({'bookings': booking_json}, status=200)
# def bookings(request):
#     if request.method == 'POST':
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return JsonResponse({}, status=400)


