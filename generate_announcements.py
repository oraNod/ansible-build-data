import os
from jinja2 import Environment, FileSystemLoader

template_path = 'templates/major_release'
env = Environment(loader=FileSystemLoader(template_path))
template = env.get_template('discourse.md')

template_data = {
    'package_version': os.getenv('PACKAGE_VERSION'),
    'tarball_url': os.getenv('TARBALL_URL'),
    'tarball_sha': os.getenv('TARBALL_SHA'),
    'wheel_url': os.getenv('WHEEL_URL'),
    'wheel_sha': os.getenv('WHEEL_SHA'),
    'core_changelog': os.getenv('CORE_CHANGELOG'),
}

rendered_markdown = template.render(template_data)

with open('rendered_output.md', 'w') as f:
    f.write(rendered_markdown)

print('Generated release announcement for discourse.')
