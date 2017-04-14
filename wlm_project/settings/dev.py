from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ymj=@err5qf5y4vyru1c*r4!vk=!5ot(v+6x@u1vii$w5e0#ei'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


try:
    from .local import *
except ImportError:
    pass
