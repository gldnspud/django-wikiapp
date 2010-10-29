from django.conf import settings
from django.utils.translation import ugettext_lazy as _


WORD_RE = getattr(settings, 'WIKI_WORD_RE', r'(?:[A-Z]+[a-z]+){2,}')

MARKUP_CHOICES = getattr(settings, 'WIKI_MARKUP_CHOICES', (
    ('creole', _(u'Creole')),
    ('restructuredtext', _(u'reStructuredText')),
    ('textile', _(u'Textile')),
    ('markdown', _(u'Markdown')),
))

URL_RE = getattr(settings, 'WIKI_URL_RE', r'\w+')

REQUIRES_LOGIN = getattr(settings, 'WIKI_REQUIRES_LOGIN', False)

LOCK_DURATION = getattr(settings, 'WIKI_LOCK_DURATION', 15)
