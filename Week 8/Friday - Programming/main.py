import logging
try:
    import colouredlogs
except Exception:
    class _ColouredLogsStub:
        @staticmethod
        def install(*args, **kwargs):
            return None
    colouredlogs = _ColouredLogsStub()
from pathlib import Path

def setup_logging():
    logging_dir = Path(__file__).parent
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=logging_dir / 'entry.log',
        filemode='a',
        force=True
    )
    log = logging.getLogger(__name__)

    return log

def test_logging(log):
    log.debug("This is a debug message")
    log.info("This is an info message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    log.critical("This is a critical message")

def age_check(age, log):
    if age < 0:
        log.warning("Age cannot be negative.")
        return False
    elif age < 18:
        log.info("User is a minor.")
        return False
    else:
        log.info("User is an adult.")
        return True

def divide_by_zero_test(log):
    try:
        result = 10 / 0
        return result
    except ZeroDivisionError as e:
        log.error("Attempted to divide by zero.", exc_info=True)

def test_coloured_logging(log):
    colouredlogs.install(level='DEBUG', logger=log)
    # Write a function that prints your first name and last name using coloured Logging.
    log.warning("First Name: John")
    log.debug("Last Name: Doe")
def main():
    log = setup_logging()
    test_logging(log)
    age = 25
    age_check(age, log)
    divide_by_zero_test(log)
    test_coloured_logging(log)

if __name__ == "__main__":
    main()