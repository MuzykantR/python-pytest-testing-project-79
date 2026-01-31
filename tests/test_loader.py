import pytest
from pathlib import Path
from page_loader.loader import download
from page_loader.exceptions import FileSystemError, NetworkError
from requests.exceptions import Timeout, ConnectionError, HTTPError, RequestException
import requests_mock


def read_fixture(name: str):
    fixtures_dir = Path(__file__).parent / "fixtures"
    file_path = fixtures_dir / name

    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def test_download_correct_content(tmp_path):
    url = "https://simple-page.com"
    expected_content = read_fixture('simple_page_com.html')

    with requests_mock.Mocker() as m:
        m.get(url, text=expected_content)

        file_path = download(url, tmp_path)

        assert Path(file_path).exists()
        assert Path(file_path).read_text() == expected_content
        assert file_path.endswith(".html")


def test_download_default_directory(tmp_path):
    assert download.__defaults__[0] == Path.cwd()  # type: ignore


def test_download_with_non_exist_directory():
    url = "https://simple-page.com"
    directory = Path("/tmp/nonexist_directory_12345")

    with pytest.raises(FileSystemError):
        download(url, directory)


def test_download_timeout_error(tmp_path):
    url = "https://simple-page.com"

    with requests_mock.Mocker() as m:
        m.get(url, exc=Timeout)

        with pytest.raises(NetworkError, match=f"Таймаут при загрузке {url}"):
            download(url, tmp_path)


def test_download_connection_error(tmp_path):
    url = "https://simple-page.com"

    with requests_mock.Mocker() as m:
        m.get(url, exc=ConnectionError)

        with pytest.raises(NetworkError, match=f"Ошибка подключения к {url}"):
            download(url, tmp_path)


def test_download_http_error(tmp_path):
    url = "https://simple-page.com"

    with requests_mock.Mocker() as m:
        m.get(url, exc=HTTPError)

        with pytest.raises(NetworkError, match=f"HTTP ошибка для {url}"):
            download(url, tmp_path)


def test_download_requests_error(tmp_path):
    url = "https://simple-page.com"

    with requests_mock.Mocker() as m:
        m.get(url, exc=RequestException)

        with pytest.raises(NetworkError, match=f"Ошибка при загрузке {url}"):
            download(url, tmp_path)
