import logging
import sys

from datetime import datetime

FMT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format=FMT,
    datefmt="%Y-%m-%d %H:%M:%S",
)


def main():
    log = logging.getLogger(__name__)
    log.info(f"{datetime.now()} | This message is different")


if __name__ == "__main__":
    main()
