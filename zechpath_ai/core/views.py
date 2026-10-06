from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Job, User
from .serializers import JobSerializer, UserSerializer


def home(request):
    """Return the basic Zecpath backend welcome message."""
    return JsonResponse({
        "message": "Hello Zecpath Backend"
    })


class JobListAPI(APIView):
    """API for retrieving all jobs."""

    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class JobCreateAPI(APIView):
    """API for creating a new job."""

    def post(self, request):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UserTestAPI(APIView):
    """API for retrieving all users."""

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )