import os
import sys
from pathlib import Path

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "myproject"

# -- Project setup -----------------------------------------------------
#

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".venv",
    ".vscode",
    "analysis_*",
    "dist",
    "excel",
    "myproject-notebooks",
    "*.md",
    "*.sh",
    "*.toml",
    "./**/__pycache__",
    "*.pyc",
    "docs",
]


def get_main_folder(assumed_folder_name: str) -> Path:
    """Get the full path of the main folder, given its assumed name."""
    cwd = Path(os.getcwd()).absolute()
    # Traverse up from the given path to the root
    for parent in cwd.parents:
        if parent.name == assumed_folder_name:
            return parent

    if cwd.name == assumed_folder_name:
        return cwd

    raise ValueError(
        f"Current working directory does not contain {assumed_folder_name} as a parent!"
    )


myproject_path = get_main_folder("sphinx-doc-test").joinpath("myproject")
print(f"{myproject_path=}")

source_folders = [myproject_path]
print(f"using source folders: {source_folders}")

for folder in source_folders:
    sys.path.insert(0, folder)


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]

autosummary_generate = True  # Turn on autosummary

autodoc_default_options = {
    "members": True,  # Include members in the documentation
    "undoc-members": True,  # Include undocumented members
    "private-members": False,  # Include private members (starting with _)
    "show-inheritance": True,  # Show base classes
}
autodoc_typehints = "both"

# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "polars": ("https://docs.pola.rs/api/python/stable", None),
}

# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
