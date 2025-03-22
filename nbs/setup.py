#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import pathlib 

THIS_FILE_PATH = pathlib.Path(__file__).resolve()  #file path of this file i.e __file__
NBS_DIR = THIS_FILE_PATH.parent    # Directory path of Notebook will be parent of this file i.e 
REPO_DIR = NBS_DIR.parent           # Similariy Director of repo will be the parent of NBS Directory which is our main workspace
DJANGO_ROOT_DIR = REPO_DIR / "src"
DJANGO_PROJECT_SETTINGS_NAME = "core"

def init_django():
    """Run administrative tasks."""
    os.chdir(DJANGO_ROOT_DIR)
    sys.path.insert(0, str(DJANGO_ROOT_DIR))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    import django 
    django.setup()

