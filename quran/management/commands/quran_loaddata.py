from django.core.management.base import BaseCommand, CommandError
from quran.data import *

class Command(BaseCommand):
    help = "Load initial Quran data."

    def add_arguments(self, parser):
        # parser.add_argument("poll_ids", nargs="+", type=int)
        pass

    def handle(self, *args, **options):
        if Aya.objects.count() > 0:
            print('The quran database must be empty before running quran_loaddata. Running tests.')
            test_data(verbosity=options['verbosity'])
            return
        self.stdout.write(
                self.style.SUCCESS("----- importing quran data (Tanzil) -----")
            )
        
        import_quran()

        print("----- done importing quran data (Tanzil). starting translations -----")
        import_translations()

        print("----- done importing translations. starting morphology -----")
        import_morphology()

        print("----- done importing morphology. starting word by word translations -----")
        import_word_translations()

        print("----- done importing word by word translations. running tests -----")
        test_data(verbosity=options['verbosity'])



