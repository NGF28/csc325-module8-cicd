from django.test import TestCase
from rest_framework.test import APIClient


class ApiEndpointTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_endpoint_returns_ok(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "ok")

    def test_greeting_endpoint_returns_message(self):
        response = self.client.get("/api/greeting/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Hello from CSC 325!")

    def test_greeting_includes_version(self):
        response = self.client.get("/api/greeting/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["version"], "2")


    def test_greeting_includes_course(self):
        response = self.client.get("/api/greeting/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["course"], "CSC 325")

    def test_greeting_includes_assignment(self):
        response = self.client.get("/api/greeting/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["assignment"], "Module 8")