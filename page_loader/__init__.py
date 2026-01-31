"""Page loader package"""
from .loader import download
from .exceptions import PageLoaderError

__version__ = "0.1.0"
__all__ = (
    "download",
    "PageLoaderError"
)
