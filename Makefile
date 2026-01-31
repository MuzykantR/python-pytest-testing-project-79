.PHONY: install test lint build package-install help

help:
	@echo "Доступные команды:"
	@echo "  test          - Запустить тесты"
	@echo "  lint          - Проверить код линтером"
	@echo "  build         - Собрать пакет"
	@echo "  package-install - Установить пакет как утилиту"
	@echo "  clean         - Очистить временные файлы"

install:
	uv sync --dev

test:
	uv run pytest -v

lint:
	uv run flake8 page_loader tests

build:
	uv build

package-install: build
	uv tool install dist/*.whl

	