# Day 18: Packages
**Overview:**  
![xkcd: Python](https://imgs.xkcd.com/comics/python.png)  
Image Source: [xkcd](https://xkcd.com/353/)

Core python is extremely powerful on its own, but its greatest potential can be reached when the developer leverages the massive open-source community. Through importing packages, python can open the door for integration with other software, Internet of Things (IoT) devices, and even create advanced artificial intelligence.

**Instructions:**  
1. Open a new python file.
2. All of the modules and functions used to this point are part of the python [built-in functions](https://docs.python.org/3/library/functions). However, python is an open-source programming language, so incredibly smart people have created custom packages that do incredibly cool things. Python also includes the [standard library](https://docs.python.org/3/library/library) which contains a set of packages already installed. Packages can be used in scripts through using the `import` statement. The `dir()` function can be used to display all of the built-in functions.
    ```
    for func in dir(__builtins__):
        print(func)
    ```
3. The packages in the standard library add extended functionality without needing to install new packages. After importing the package, the functions of the package can be used. The name of the package needs to be called in order to access the embedded functions. According to the PEP 8 formatting standards, all import declarations should occur at the top of the python file.
    ```
    import random
    num = random.randint(0, 100)
    for i in range(0, 3):
       try:
           guess = int(input("Guess a number between 0 and 100: "))
       except:
           print("Please enter a valid integer between 0 and 100.")
           break
       if guess == num:
           print("{} is the correct value. You win.".format(guess))
       elif guess < num:
           print("{} is lower than the value. You have {} tries left.".format(guess, 2 - i))
       elif guess > num:
           print("{} is higher than the value. You have {} tries left.".format(guess, 2 - i))
       else:
           print("Something went wrong.")
    ```
4. The `turtle` package is a fun way to get kids into programming. The user can give commands to a virtual [turtle](https://docs.python.org/3/library/turtle.html) to instruct it to draw objects on screen.
    ```
    import turtle
    jonathan = turtle.Turtle()
    jonathan.shape("turtle")
    jonathan.forward(100)
    jonathan.right(90)
    jonathan.forward(100)
    jonathan.right(90)
    jonathan.forward(100)
    jonathan.right(90)
    jonathan.forward(100)
    turtle.done()
    ```
5. The `webbrowser` package allows interaction with an external web browser by using python. The system default browser will be used to launch the content first, but a specific browser can be specified for the task. Additionally, the built-in `help()` function can be used to print the documentation of the package specified in the terminal window.
    ```
    import webbrowser
    webbrowser.open("https://docs.python.org/3/library/webbrowser.html")
    chrome = webbrowser.get(using='google-chrome')
    chrome.open_new("https://www.youtube.com/watch?v=CMNry4PE93Y")
    help(webbrowser)
    ```
6. The `time` package is extremely useful for most software development. When doing performance testing, this package can provide insights on the bottlenecks of the script.
    ```
    import time
    start = time.time()
    print("Program Start")
    time.sleep(5)
    print("Program End. The total execution time was {} sec.".format(time.time() - start))
    ```
7. The `datetime` package is more advanced than the `time` package because it adds the additional ability to manipulate dates as well as times. The `time` package is best used for performance testing, but the `datetime` [package]((https://docs.python.org/3.7/library/datetime.html)) is best used for timezone and calendar based manipulations.
    ```
    from datetime import datetime
    print(datetime.today())
    print("Day: {}\nMonth: {}\nYear: {}".format(datetime.today().day, datetime.today().month, datetime.today().year))
    if datetime.today() > datetime(datetime.today().year, 7, 4):
        days_until = (datetime(datetime.today().year + 1, 7, 4) - datetime.today()).days
        age = (datetime.today().year + 1) - 1776
    else:
        days_until = (datetime(datetime.today().year, 7, 4) - datetime.today()).days
        age = datetime.today().year - 1776
    print("There are {} days left until MURICA's birthday. MURICA will be {} years old.".format(days_until, age))
    ```
8. The `os` package is a method of accessing the operating system in an efficient manner. This [package](https://docs.python.org/3.7/library/os.html) will be leveraged more on [Day 19](../Module2/Day19) along with the core `open()` function. This package contains functions for migrating the operating system, retrieving system information, interacting with files, and more.
    ```
    import os
    print(os.getcwd())
    print(os.cpu_count())
    print(os.getlogin())
    ```
9. If a desired package isn't installed, the `pip` command can be used in the terminal to add it to the environment. Depending on the IDE being used, there are efficient ways to install new packages. For instance, in PyCharm, the user can access the terminal directly from the IDE, but the user can also add or upgrade packages by going to `Settings > Project > Project Interpreter`. When the `pip install` command is executed, the appropriate package and any applicable dependencies are pulled and installed from [PyPi](https://pypi.org/). The `pip install` command also excepts specific URLs and git locations. To install a package from GitHub, simply use the command `pip install --upgrade git+git://github.com/<GitHub URL>.git` 
    ```
    Usage:
    pip <command> [options]

    Commands:
      install                        Install packages.
      download                       Download packages.
      uninstall                      Uninstall packages.
      freeze                         Output installed packages in requirements format.
      list                           List installed packages.
      show                           Show information about installed packages.
      check                          Verify installed packages have compatible dependencies.
      config                         Manage local and global configuration.
      search                         Search PyPI for packages.
      wheel                          Build wheels from your requirements.
      hash                           Compute hashes of package archives.
      completion                     A helper command used for command completion.
      help                           Show help for commands.

    General Options:
      -h, --help                     Show help.
      --isolated                     Run pip in an isolated mode, ignoring environment variables and user configuration.
      -v, --verbose                  Give more output. Option is additive, and can be used up to 3 times.
      -V, --version                  Show version and exit.
      -q, --quiet                    Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging levels).
      --log <path>                   Path to a verbose appending log.
      --proxy <proxy>                Specify a proxy in the form [user:passwd@]proxy.server:port.
      --retries <retries>            Maximum number of retries each connection should attempt (default 5 times).
      --timeout <sec>                Set the socket timeout (default 15 seconds).
      --exists-action <action>       Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
      --trusted-host <hostname>      Mark this host as trusted, even though it does not have valid or any HTTPS.
      --cert <path>                  Path to alternate CA bundle.
      --client-cert <path>           Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
      --cache-dir <dir>              Store the cache data in <dir>.
      --no-cache-dir                 Disable the cache.
      --disable-pip-version-check    Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
      --no-color                     Suppress colored output

    ```
10. Update the [log file](../../log.md) with what you have learned today.
