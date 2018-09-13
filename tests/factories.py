import factory

from critical.models import Critical


class CriticalFactory(factory.DjangoModelFactory):
    url = factory.Faker('url')
    path = factory.Faker('uri_path')
    css = factory.Faker('text')

    class Meta:
        model = Critical
