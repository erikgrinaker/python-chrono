# -*- coding: utf-8 -*-

import sys
import os
import os.path

sys.path.insert(0, os.path.abspath("../../"))

import chrono

# metadata
project = "python-chrono"
copyright = "2010 Erik Grinaker"
version = ".".join(chrono.__version_info__[:2])
release = chrono.__version__

# paths
templates_path = [
    "templates",
]

# extensions
extensions = [
    "sphinx.ext.autodoc",
]

# document info
source_suffix = ".rst"
master_doc = "index"

# theme
pygments_style = "sphinx"
html_theme = "default"
html_show_sourcelink = False
