import sphinx_rtd_theme

project = 'VNEngine'
copyright = '2024, Lucas Veit'
author = 'Lucas Veit'
release = '0.1'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
