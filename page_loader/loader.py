from pathlib import Path
from .exceptions import NetworkError, FileSystemError
from .naming import generate_filename
import requests


def download(url: str, output_dir: str | Path = Path.cwd()):
    if isinstance(output_dir, str):
        output_dir = Path(output_dir)
    _validate_directory(output_dir)

    content = _get_page(url)
    filename = generate_filename(url)
    file_path = output_dir / filename
    _save_to_file(content, file_path)

    return str(file_path)


def _validate_directory(directory: Path) -> None:
    if not directory.is_dir():
        raise FileSystemError(f"Директория не существует: {directory}")


def _get_page(url: str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        raise NetworkError(f"Таймаут при загрузке {url}")
    except requests.exceptions.ConnectionError:
        raise NetworkError(f"Ошибка подключения к {url}")
    except requests.exceptions.HTTPError:
        raise NetworkError(f"HTTP ошибка для {url}")
    except requests.exceptions.RequestException:
        raise NetworkError(f"Ошибка при загрузке {url}")


def _save_to_file(content: str, file_path: Path):
    file_path.write_text(content)
    return None
