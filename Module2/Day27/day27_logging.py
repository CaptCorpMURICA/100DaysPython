#the logging module is utilized to record the progress of the application and any problems that occur
import logging
import os

# os.chdir(".\\Module2\\Day27")

logging.basicConfig(filename="day27_logging.log")
logger = logging.getLogger() #used to create the logger object
logger.info("This is a custom info message.")
logger.warning("This is a custom warning message.")

#while the file was created, the .info() message was not recorded 
#the level method will provide the numerical representation of the level created in basicConfig()
#The logger will only print messages that have a level greater than or equal to the level set when creating the logger. 

print(logger.level)
log_level = [("NOTSET", 0), ("DEBUG", 10), ("INFO", 20), ("WARNING", 30), ("ERROR", 40), ("CRITICAL", 50)]

#the logger can be created with a specific designation
logger.level = "DEBUG"
logger.info("This is a custom info message.")
logger.warning("This is a custom warning message.")

import logging
import os

# os.chdir(".\\Module2\\Day27")

log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename="module2_day27_logging.log",
                    level=logging.DEBUG,
                    format=log_formatter)
logger = logging.getLogger()
logger.info("This is a custom info message.")
logger.warning("This is a custom warning message.")

#the format option is used to customize the default setting of the log message

import logging 
import os

# os.chdir(".\\Module2\\Day27")

log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename="module2_day27_logging.log",
                    level = logging.DEBUG,
                    format=log_formatter)
logger = logging.getLogger()
logger.info("This is a custom info message.")
logger.warning("This is a custom warning message.")

#through using exception handling along with a robust logger, common errors can be explicitly written to the log file for review
import logging
import os

# os.chdir(".\\Module2\\Day27")

log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename="module2_day27_logging.log",
                    level=logging.DEBUG,
                    format=log_formatter,
                    filemode="w")
logger = logging.getLogger()


def quadratic_formula(a: float, b: float, c: float) -> (float, float):
    """
    Solve for x in the quadratic formula.
        ax^2 + bx + c = 0
    :param a: float
    :param b: float
    :param c: float
    :return: Solve for x, Return the positive and negative roots as float in a tuple
    """
    logger.info(f"Quadratic Formula Solver: {a}x^2 + {b}x + {c} = 0")

    # Calculate the discriminant
    logger.debug(f"Calculate the discriminant: {b}^2 - 4*{a}*{c}")
    discrim = (b ** 2) - (4 * a * c)
    logger.debug(f"Discriminant: {discrim}")

    # Calculate the positive and negative roots
    logger.debug(f"Calculate the pos/neg roots: (-{b} +/- sqrt({discrim})) / (2*{a})")
    try:
        pos_root = (-b + (discrim ** 0.5)) / (2 * a)
        neg_root = (-b - (discrim ** 0.5)) / (2 * a)
        logger.debug(f"Positive Root: {pos_root}, Negative Root: {neg_root}")
        return pos_root, neg_root
    except ZeroDivisionError as err:
        logger.error(f"{a} cannot be equal to zero.\n{err}")
        raise
    except TypeError as err:
        logger.error(f"Invalid type.\n{err}")
        raise
    except ValueError as err:
        logger.error(f"Invalid value.\n{err}")
        raise
    finally:
        logger.debug("Function Complete")


roots = quadratic_formula(3, 4, 5)
print(roots)