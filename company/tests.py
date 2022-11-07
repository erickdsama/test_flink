# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from company.models import Company


class CompanyTestCase(TestCase):

    def test_create_company(self):

        client = APIClient()

        test_company = {
            'name': 'CompanyTest',
            'description': 'CompanyTest with ID',
            'symbol': 'APPL',
            "market_values": [
                "823759106014.600",
                "754092828224.000",
                "120859375664.000",
                "61082258614.200",
                "64336768145.605"
            ],
        }

        response = client.post(
            '/company/',
            test_company,
            format='json'
        )

        result = json.loads(response.content)

