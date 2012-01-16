import logging
from os import walk, path

from django.template.base import TemplateDoesNotExist
from django.template.loaders import cached, app_directories
from django.conf import settings

def find_templates_in_dirs(dir_list):
    out = set()
    for d in dir_list:
        for root, dirs, files in walk(d):
            # strip base dir
            root = root[len(d) + 1:]
            for f in files:
                out.add(path.join(root, f))

    return out


TEMPLATE_FINDERS = {
    'django.template.loaders.app_directories.Loader': lambda: find_templates_in_dirs(app_directories.app_template_dirs),
    'django.template.loaders.filesystem.Loader': lambda: find_templates_in_dirs(settings.TEMPLATE_DIRS),
}

class Loader(cached.Loader):
    def __init__(self, loaders):
        self.find_templates(loaders)
        super(Loader, self).__init__(loaders)

    def find_templates(self, loaders):
        """
        Find all templates for all loader we will be caching today.
        """
        self.existing_templates = set()
        for l in loaders:
            if l not in TEMPLATE_FINDERS:
                # unknown loader, we have no clue how to find all templates
                logging.error('Unknown template loader %s, unable to find all templates. Disabling.', l)
                self.existing_templates = None
                return
            self.existing_templates = self.existing_templates.union(TEMPLATE_FINDERS[l]())
        logging.info('Found %d templates.', len(self.existing_templates))

    def load_template(self, template_name, template_dirs=None):
        if self.existing_templates is not None and template_name not in self.existing_templates:
            raise TemplateDoesNotExist('Template not found upon startup, giving up.')

        return super(Loader, self).load_template(template_name, template_dirs)
