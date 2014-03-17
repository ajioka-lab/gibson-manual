Gibson Manual
=============

### Installation Requirements


1. Python 2.7 with virtualenv
2. That's about it

### Installation Process

1. Create a virtual environment

        $ virtualenv VENV

2. Enter the virtual environment


        $ source VENV/bin/activate

3. Install python requirements

        (VENV)$ pip install -r /path/to/gibson-manual/py_requirements.txt

4. Create a node.js virtual environment and install node.js requirements (will take some time)

        (VENV)$ nodeenv -p -r /path/to/gibson-manual/node_requirements.txt

### Generating files

1. In the directory containing `make.py` run:

        (VENV)$ ./make.py

2. Output is in `_build/`
