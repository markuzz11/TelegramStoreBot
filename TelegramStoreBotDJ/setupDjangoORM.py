import django
from django.conf import settings
import TelegramStoreBotDJ.settings as sets
settings.configure(
    DATABASES=sets.DATABASES,
    INSTALLED_APPS=sets.INSTALLED_APPS
)
django.setup()
