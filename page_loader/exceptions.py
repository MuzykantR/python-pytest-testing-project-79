class PageLoaderError(Exception):
    """Базовое исключение для всех ошибок page_loader."""
    pass


class NetworkError(PageLoaderError):
    """Ошибка сети при загрузке страницы."""
    pass


class FileSystemError(PageLoaderError):
    """Ошибка файловой системы при сохранении."""
    pass
