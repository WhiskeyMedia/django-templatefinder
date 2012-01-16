#!/usr/bin/env python
import sys
from os.path import dirname, join, abspath

from django.conf import settings

import nose

def run_all(argv=None):
    settings.configure(
        INSTALLED_APPS=('tests.test_app', ),
        TEMPLATE_DIRS=(abspath(join(dirname(__file__), 'templates')), ),
        TEMPLATE_LOADERS=(
            ('templatefinder.Loader', (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            )),
        )
    )

    if argv is None:
        argv = [
            'nosetests',
            '--with-coverage', '--cover-package=templatefinder', '--cover-erase',
            '--nocapture', '--nologcapture',
            '--verbose',
        ]

    nose.run_exit(
        argv=argv,
        defaultTest=abspath(dirname(__file__)),
    )

if __name__ == '__main__':
    run_all(sys.argv)


