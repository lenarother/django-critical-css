import pytest
from django.core.management import call_command

from critical.models import Critical

from .factories import CriticalFactory


@pytest.mark.django_db
def test_empty_critical_css():
    CriticalFactory.create_batch(size=5)
    assert Critical.objects.count() == 5

    call_command('empty_critical_css')

    assert Critical.objects.count() == 0
