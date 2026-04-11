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


