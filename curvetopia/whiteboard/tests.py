# tests.py
from django.test import TestCase, Client
from django.urls import reverse
import json

class ProcessDrawingTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('process_drawing')
        self.valid_payload = {
            'csv': '10,10,RECTANGLE\n20,20,CIRCLE'
        }

    def test_process_drawing_valid(self):
        response = self.client.post(self.url, json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('csv', response.json())
        self.assertIn('image', response.json())