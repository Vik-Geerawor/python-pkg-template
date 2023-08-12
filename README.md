# python-pkg-template

`python-pkg-template` is a [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) template for creating a fully-featured Python package using [`setuptools`](https://setuptools.pypa.io).

# Under Construction

## Objective

Develop a package template which has the src layout and which uses the following tools for the purpose(s) described:

- `virtualenv`: for creating a virtual environment
- `pdm`: for package dependency management
- `setuptools`: for building the `sdist` and `wheel`
- `mkdocs`: for automatic doc generation
- `Python Semantic Release`: for automatic version bumping and updating changelog.
- set up CI/CD pipeline using GitHub Actions for automated build process

## Plan

- Define the structure of the package.
- Define an initial `pyproject.toml` with what is known.
- Populate `pyproject.toml` using `cookiecutter.json`.
- Add a test function to package and test. Test after adding each new item henceforth.
- Add standard non-code files, like `README`, `LICENSE`, etc. as far as comfortable.
