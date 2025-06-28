"""WRD (WRonai Development) - A powerful workflow automation tool for developers."""

from .__version__ import __version__, __author__, __email__
from .cli import WRDShell
from .template_manager import TemplateManager, get_template_manager

__all__ = [
    '__version__',
    '__author__',
    '__email__',
    'WRDShell',
    'TemplateManager',
    'get_template_manager',
]

__author__ = "Tom Sapletta <info@softreck.dev>"
__license__ = "Apache-2.0"