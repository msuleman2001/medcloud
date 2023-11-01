from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Manager
from .serializers import ManagerSerializer


@api_view(['POST'])
def add_manager(request):
    if request.method == 'POST':
        data = request.data

        # Add additional validation
        if Manager.objects.filter(phone=data['phone']).exists():
            return Response({'error': 'Phone number must be unique'}, status=status.HTTP_400_BAD_REQUEST)
        if Manager.objects.filter(cnic_number=data['cnic_number']).exists():
            return Response({'error': 'CNIC number must be unique'}, status=status.HTTP_400_BAD_REQUEST)
        if len(data['password']) < 8:
            return Response({'error': 'Password must be at least 8 characters long'}, status=status.HTTP_400_BAD_REQUEST)

        # Set the username to the phone number
        data['username'] = data['phone']

        # Hash the password
        data['password'] = make_password(data['password'])

        serializer = ManagerSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Manager added successfully', 'new_manager_id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_managers(request):
    managers = Manager.objects.all()

    # Add pagination
    paginator = PageNumberPagination()
    paginated_managers = paginator.paginate_queryset(managers, request)

    serializer = ManagerSerializer(paginated_managers, many=True)
    return Response({'managers': serializer.data})


@api_view(['GET'])
def search_manager(request, manager_id):
    try:
        manager = Manager.objects.get(id=manager_id)
    except Manager.DoesNotExist:
        return Response({'error': 'Manager not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ManagerSerializer(manager)
    return Response({'manager': serializer.data})


@api_view(['PUT'])
def update_manager(request, manager_id):
    try:
        manager = Manager.objects.get(id=manager_id)
    except Manager.DoesNotExist:
        return Response({'error': 'Manager not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ManagerSerializer(manager, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'message': 'Manager updated successfully'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
