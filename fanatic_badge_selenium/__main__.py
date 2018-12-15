from datetime import datetime

from .fanatic_badge import FanaticBadge
from .logger import logger


def main():
    fb = FanaticBadge()
    fb.navigate_to_user_page()


if __name__ == '__main__':
    logger.info("Session started at {}".format(datetime.now()))
    main()
    logger.info("Session ended at {}".format(datetime.now()))
