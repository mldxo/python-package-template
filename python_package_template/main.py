"""Main module for python package template application"""

from .version import __version__ as version
from .src.classname import Classname

def main():
    """Executes main function"""
    print(f"Python package template version {version}")
    app = Classname()
    app.run()
    return

if __name__ == "__main__":
    main()
