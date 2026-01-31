import argparse
from .loader import download
import sys


def main():
    try:
        parser = argparse.ArgumentParser(description="Скачиваем веб-страницы")
        parser.add_argument('url', help="URL для скачивания")
        parser.add_argument('-o', '--output', default='.', help='Директория для сохранения')

        args = parser.parse_args()

        result = download(args.url, args.output)

        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
