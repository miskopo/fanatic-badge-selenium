from logging import getLogger, FileHandler, DEBUG


logger = getLogger('fanatic_badge_selenium')
logger.setLevel(DEBUG)

file_handler = FileHandler("/var/log/fanatic_badge/debug.log")

logger.addHandler(file_handler)
