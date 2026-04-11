import logging

# -- Simple logging ---
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# -- Logging in file --
logging.basicConfig(
    level=logging.DEBUG,
    filename=r"C:\Users\Abhishek\Desktop\Docker Learning\Basic Docker Fastapi\app.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("This is the debug message")
logging.warning("This is the warning message")
logging.info("This is the info message")
logging.error("This is the error message")
logging.critical("This is the critical message")

# -------------------------------------------------------------------------------------
# creating multiple logger

import logging

logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger("module2")
logger2.setLevel(logging.WARNING)

logging.basicConfig(
    level=logging.DEBUG,
    filename=r"C:\Users\Abhishek\Desktop\Docker Learning\Basic Docker Fastapi\multiple_logger.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger1.debug("This is the debug message")
logger1.warning("This is the warning message")

logger2.info("This is the info message")
logger2.error("This is the error message")
logger2.critical("This is the critical message")
