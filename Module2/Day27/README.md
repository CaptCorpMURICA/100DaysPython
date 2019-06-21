# Day 27: Logging
**Instructions:** 
1. Open a new python file.
2. Murphy's Law indicates that _"anything that can go wrong, will go wrong."_ While this extremely optimistic view inspires hope and exuberant joy, it's critical for effective and robust python programs. The `logging` module offers the ability to track the progress of the application and report on successes and failures. Implementing logging and unittests will not protect the program from breaking; this is inevitable. However, applications that leverage these tools will be harder to break; but when they do, enough information will be provided to fix it quickly.
3. The `logging ` module is utilized to record the progress of the application and any problems that occur. The module contains the standard levels of `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL', but custom levels can be created. The logger first needs to be created using the `.basicConfig()` function and the log file is passed as a parameter. Then, the `.getLogger()` method is used to create the logger object leveraged by the program.
    ```
    import logging
    import os

    os.chdir(".\\Module2\\Day27")

    logging.basicConfig(filename="module2_day27_logging.log")
    logger = logging.getLogger()
    logger.info("This is a custom info message.")
    logger.warning("This is a custom warning message.")
    ```
4. While the file was created, the `.info()` message was not recorded. The `.level` method. This will provide the numerical representation of the level created in the `.basicConfig()` function. A logger level of 30 represents the level "WARNING". The logger will only print messages that have a level greater than or equal to the level set when creating the logger. Therefore, since an `info()` message is being written and "INFO" is a lower level than "WARNING", the message is not recorded.
    ```
    print(logger.level)
    log_level = [("NOTSET", 0), ("DEBUG", 10), ("INFO", 20), ("WARNING", 30), ("ERROR", 40), ("CRITICAL", 50)]
    ```
5. The logger can be created with a specific level designation. The lower the level, the more verbose the logging. It is important ot note that overly verbose logs are often difficult to understand. Is it easier to gain spending insights by looking at the raw data in a table or can the insights be understood more efficiently if the data is presented in a time series chart? Just like deriving insights from data, the logs should be focused and direct.
    ```
    logger.level = "DEBUG"
    logger.info("This is a custom info message.")
    logger.warning("This is a custom warning message.")
    ```
6. The `format` option is used to customize the default settings of the [log message](https://docs.python.org/3.7/library/logging.html#logrecord-attributes). This additional functionality improves the readability and effectiveness of the log files. After a logger is created, there are only certain attributes that can be changed, like the logger level. Therefore, it's important to plan the needs of the logger before creating the object. If changes need to be made, the object must first be destroyed.
    ```
    import logging
    import os

    os.chdir(".\\Module2\\Day27")

    log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
    logging.basicConfig(filename="module2_day27_logging.log",
                        level=logging.DEBUG,
                        format=log_formatter)
    logger = logging.getLogger()
    logger.info("This is a custom info message.")
    logger.warning("This is a custom warning message.")
    ```
7. By default, the log file is created in append mode. This can be changed with the `filemode` option.
    ```
    import logging
    import os

    os.chdir(".\\Module2\\Day27")

    log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
    logging.basicConfig(filename="module2_day27_logging.log",
                        level=logging.DEBUG,
                        format=log_formatter,
                        filemode="w")
    logger = logging.getLogger()
    logger.debug("This is a custom debug message.")
    logger.info("This is a custom info message.")
    logger.warning("This is a custom warning message.")
    logger.error("This is a custom error message.")
    logger.critical("This is a custom critical message.")
    ```
8. Logging is critical for creating functions. Through using [exception handling](https://docs.python.org/3/library/exceptions.html) along with a robust logger, common errors can be explicitly written to the log file for review when the program breaks. The program executes the code within the `try` block first. If there are any errors, the `except` blocks are reviewed. Specific error messages are associated with each `except` block. If `True`, the code within the block is executed. The `else` block is only executed if the `try` block ran successfully without errors. The `finally` block is executed regardless of success or failure.
    ```
    import logging
    import os

    os.chdir(".\\Module2\\Day27")

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
    ```
9. Update the [log file](../../log.md) with what you have learned today.
