import logging

from datetime import datetime
from pathlib import Path

LOG_FILE = Path.cwd() / "notify.log"
FMT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(
    filename=LOG_FILE.absolute(),
    level=logging.INFO,
    format=FMT,
    datefmt="%Y-%m-%d %H:%M:%S",
)


def main():
    log = logging.getLogger(__name__)
    log.info(f"{datetime.now()} | This message is different")


if __name__ == "__main__":
    main()
