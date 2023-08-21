import os, sys


def create_venv(version):
    """Function which creates a virtual environment.

    This function creates a virtual environment inside the root directory
    of the project. A directory named 'venv' will be create where the Python
    interpreter will be installed. All dependencies will be installed inside
    this virtual environment.

    Parameter
    ---------
    version : str
        Python version number as a string

    Returns
    ------
    int
        Return code
    """
    # check if python with the expected version is installed
    return_code = os.system(f"python{version} --version")

    # if not, return error code
    if return_code != 0:
        print(f"python{version} is not installed on your system.")
        return return_code

    # otherwise, create venv and return 0
    os.system(f"python{version} -m venv venv")
    return 0


def main():
    """The main function for all the pre-hook functions.

    All the pre-hooks need to be define in a separate function
    and added to the main() function which is called by cookiecutter.
    """
    python_version = {{cookiecutter.python_version}}

    # check if venv created
    x = create_venv(python_version)

    if x != 0:
        sys.exit(-1)

    print(f"pre gen completed successfully.")
    return 0


main()
