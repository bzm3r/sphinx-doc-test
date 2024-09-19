# Running the test

I am using [`rye`](https://rye.astral.sh/) to easily set up the environment for the test, but the `pyproject.toml` should be compatible with other tools too.

## Installing Rye

**Note:** if you are on Windows, make sure to [enable developer mode](https://rye.astral.sh/guide/faq/#windows-developer-mode) before installing `rye`.

- Install [`rye`](https://rye.astral.sh/guide/installation/#installing-rye).
  - Choose `uv` as the preferred package installer
  - Choose `Run a Python installed and managed by Rye` for which Python should be used in a Rye managed project.
  - Choose the latest version of Python available
    - this project will always use the latest version available
- change directory to where this project is
- run `rye sync`
- **unnecessary unless you really need to**:
  - to activate the virtual environment created by `rye` manually (e.g. within a terminal), [follow the typical instructions for activating a virtual environment](https://docs.python.org/3/tutorial/venv.html); in this project's case, the virtual environment folder is called `.venv` (automatically created by `rye`), so you would run
    - (if on Linux): `source ./.venv/bin/activate`
    - (if on Windows): `./myproject-project/.venv/Scripts/activate`

## Running Sphinx

Once the environment is set up, you can run either `makedocs.sh` (bash) or `makedocs.ps1` (Windows, Powershell) as appropriate.
