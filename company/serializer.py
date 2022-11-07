from django.db.migrations import serializer

from .models import Company


class CompanySerializer(serializer.Serializer):

    class Meta:
        model = Company
