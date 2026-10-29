from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(request):
    """Simple status endpoint."""
    return Response({"status": "ok"})


@api_view(["GET"])
def greeting(request):
    """Greeting endpoint; you'll update this for your recorded change."""
    return Response({"message": "Hello from CSC 325!"})
