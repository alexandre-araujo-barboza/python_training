from setup.models import SiteSetup


def context_example(request):
    return {
        'example': 'Veio do context processor (example)'
    }


def setup(request):
    setup = SiteSetup.objects.order_by('-id').first()

    return {
        'setup': setup,
    }