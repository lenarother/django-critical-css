from django.core.management.base import BaseCommand

from critical.models import Critical


class Command(BaseCommand):
    help = 'Removes all critical css data from db.'

    def get_qs(self):
        return Critical.objects.all()

    def handle(self, *args, **options):
        qs = self.get_qs()
        qs_count = qs.count()
        qs.delete()
        self.stdout.write(
            self.style.SUCCESS('Successfully deleted {0} critical objects'.format(qs_count))
        )
