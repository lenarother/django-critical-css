import pytest

from testing.factories.critical import CriticalFactory


@pytest.mark.django_db
class TestCritical:

    def test_str(self):
        critical = CriticalFactory.create(url='www.mysite.com')

        assert str(critical) == 'www.mysite.com'
