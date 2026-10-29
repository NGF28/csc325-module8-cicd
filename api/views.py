from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(request):
    """Simple status endpoint."""
    return Response({"status": "ok"})


@api_view(["GET"])
def greeting(request):
    return Response({
        "message": "Hello from CSC 325!",
        "version": "2"
    })


