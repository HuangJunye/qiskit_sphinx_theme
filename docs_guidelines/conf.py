# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Qiskit Documentation Guidelines'
copyright = '2022, Qiskit Development Team'
author = 'Junye Huang, Guillermo Mijares Vilariño'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['jupyter_sphinx', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx', 'sphinx_toolbox.confval']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'qiskit_sphinx_theme'

# -- Intersphinx configuration ------------------------------------------------

intersphinx_mapping = {
    "qiskit": ("https://qiskit.org/documentation/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None)
}