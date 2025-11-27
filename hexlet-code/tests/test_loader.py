import pytest
from page_loader.loader import download

def test_download_exists():
    """Тест что функция существует"""
    assert callable(download)

def test_download_returns_none():  # Или что она сейчас возвращает
    result = download("https://example.com", "/tmp")
    assert result is None  # Если твоя функция пока возвращает None