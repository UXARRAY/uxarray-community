"""Sphinx configuration for the UXarray Community site.

Entry pages are generated from entries/ at build time (see generate.py). Notebooks are
never executed: most entries need data that only exists on HPC systems, so the outputs
committed by their authors are what gets rendered.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate  # noqa: E402

generate.main()

project = "UXarray Community"
author = "UXarray developers and community"
copyright = "UXarray developers"

extensions = ["myst_nb", "sphinx_copybutton"]

# README content is folded into each entry's generated index.md.
exclude_patterns = ["_build", "**.ipynb_checkpoints", "entries/*/README.md"]

# Render committed outputs as-is; never run notebooks during the build.
nb_execution_mode = "off"

myst_enable_extensions = ["colon_fence", "dollarmath", "amsmath"]
myst_heading_anchors = 3

# Contributor notebooks often skip heading levels, and HoloViews adds helper outputs
# (application/vnd.holoviews_*) next to the HTML/JS that actually renders the plot.
suppress_warnings = ["myst.header", "mystnb.unknown_mime_type"]

html_theme = "sphinx_book_theme"
html_title = "UXarray Community"
html_theme_options = {
    "repository_url": "https://github.com/UXARRAY/uxarray-community",
    "use_repository_button": True,
    "use_issues_button": True,
    "home_page_in_toc": True,
}
