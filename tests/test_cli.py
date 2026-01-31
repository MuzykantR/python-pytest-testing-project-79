import sys
import pytest
from page_loader.cli import main
from pathlib import Path


def test_cli_shows_help(capsys):
    sys.argv = ['page-loader', '--help']
    try:
        main()
    except SystemExit:
        pass

    output = capsys.readouterr().out
    assert 'usage' in output.lower()
    assert 'url' in output


def test_cli_parses_arguments(mocker):
    mock_download = mocker.patch('page_loader.cli.download')

    # Тест 1: Только URL (output по умолчанию)
    sys.argv = ['page-loader', 'https://example.com']
    main()
    mock_download.assert_called_with('https://example.com', '.')

    # Тест 2: URL + output
    mock_download.reset_mock()
    sys.argv = ['page-loader', 'https://example.com', '-o', '/tmp']
    main()
    mock_download.assert_called_with('https://example.com', '/tmp')


def test_cli_integration(tmp_path, requests_mock, capsys):
    test_html = "<html>Test</html>"
    excepted_path = str(tmp_path / "example-com.html")

    requests_mock.get("https://example.com", text=test_html)
    sys.argv = ['page-loader', 'https://example.com', '--output', str(tmp_path)]

    main()

    output = capsys.readouterr().out.strip()
    assert output == excepted_path
    assert Path(output).exists()
    assert Path(output).read_text() == test_html


def test_cli_handles_errors(mocker, capsys):
    mock_download = mocker.patch('page_loader.cli.download')
    mock_download.side_effect = Exception

    sys.argv = ['page-loader', 'https://example.com']

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1

    output = capsys.readouterr().err
    assert 'error' in output.lower()
