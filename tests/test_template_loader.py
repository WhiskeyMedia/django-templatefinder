from django.template import TemplateDoesNotExist, Context
from django.template.loader import get_template

from nose import tools

loader = None

def setup():
    "make sure that template loaders are loaded."
    global loader
    tools.assert_raises(TemplateDoesNotExist, get_template, 'non-existent-template.html')
    from django.template.loader import template_source_loaders
    loader = template_source_loaders[0]

def test_existing_template_is_found():
    t = get_template('existing.html')
    tools.assert_equals('I exist, therefore I am!\n', t.render(Context({})))

def test_loader_found_all_templates():
    tools.assert_equals(set(['existing.html', 'app_existing.html', 'a/b/c/tpl.html']), loader.existing_templates)

def test_undiscovered_template_will_cannot_be_found():
    tools.assert_raises(TemplateDoesNotExist, get_template, 'existing.html')

test_undiscovered_template_will_cannot_be_found.setup = lambda: loader.existing_templates.remove('existing.html')
test_undiscovered_template_will_cannot_be_found.teardown =  lambda: loader.existing_templates.add('existing.html')


