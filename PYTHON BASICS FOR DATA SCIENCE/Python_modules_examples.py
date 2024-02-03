{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1e8c3b42",
   "metadata": {},
   "source": [
    "<div align=\"center\" style=\" font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "<img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/master/Python-Notebook-Banners/Examples.png\"  style=\"display: block; margin-left: auto; margin-right: auto;\";/>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f662d169",
   "metadata": {},
   "source": [
    "# Examples: Python modules\n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26af890c",
   "metadata": {},
   "source": [
    "This notebook accompanies the walk-through video on Python modules and packages, and also contains a few additional examples on how we can use modules. \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e7ee70a",
   "metadata": {},
   "source": [
    "## Learning Objectives\n",
    "In this train we will learn how to:\n",
    "- Write a module and import all or specific objects from a module. \n",
    "- Import modules using an alias name and explore the use of built-in modules.\n",
    "\n",
    "\n",
    "## Outline\n",
    "To do this, we will:\n",
    "- Define the importance of modules and packages in programming.\n",
    "- Review the syntax and conventions for importing modules. \n",
    "- Consider the use of built-in Python modules."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3562c909",
   "metadata": {},
   "source": [
    "## Introduction\n",
    "Modular programming is a style of programming that promotes code reusability; allowing us to generate single pieces of code which can be used in multiple parts of a project - thus saving time and resources. The resulting code can be simpler to understand and maintain since components can be considered in isolation. In Python, **modularisation** is implemented using functions, modules and packages.\n",
    "\n",
    "A **module** is a file consisting of Python code. A module can define functions, classes, variables and runnable code. These modules can be imported and referenced from other Python code. A **Python package** (also referred to as a library) is a collection of hierarchically structured directories of Python code consisting of sub-packages and modules.\n",
    "\n",
    "Modules and packages are two mechanisms that facilitate modular programming. \n",
    "\n",
    "## Why modularisation? \n",
    "\n",
    "* **Reusability**: Eliminates the need to write new code, as functionality defined in a single module can be easily reused.\n",
    "\n",
    "\n",
    "* **Simplicity**: Modules generally tend to focus on a selected area of the problem which is usually small, rather than focusing on the entire problem at hand. Integrating the use of selected modules will result in systematically dealing with each small problem in the code, making development easier and less error-prone.\n",
    "\n",
    "\n",
    "* **Maintainability**: Modules in Python are often designed to be self-supporting. In this sense, one module does not depend entirely upon other modules to work. Therefore it is unlikely that modifying a single module of a program will affect other parts of the program. This allows a team of many programmers or data scientists to work collaboratively on a large application."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7c61c07",
   "metadata": {},
   "source": [
    "## Working with modules  \n",
    "\n",
    "### Creating modules\n",
    "Creating a module is as simply as saving a Python script with functions, classes, variables and running code. The file name is the module name with the suffix `.py` appended.\n",
    "\n",
    "### Importing modules \n",
    "We can access this module and its elements from a different Python file by using the `import` statement. \n",
    "* We can import a single module/package:\n",
    "\n",
    "    ```python\n",
    "    import <module_name>\n",
    "    ```\n",
    "\n",
    "* import multiple modules using individual import statements:\n",
    "\n",
    "    ```python\n",
    "    import <module_1_name>\n",
    "    import <module_2_name>\n",
    "    import <module_3_name>\n",
    "    ...```\n",
    "    \n",
    "    \n",
    "                      \n",
    "The same rules apply when dealing with packages. We can import specific modules within a package by using dot notation. For this to work, we have to structure packages and modules in a way that reflects the hierarchy in the package directory.\n",
    "\n",
    "   ```python\n",
    "    import <package_name>.<sub_package_name>.<module_name>.<...>\n",
    "   ```\n",
    "\n",
    "Let's go ahead and create our own module, with the following 3 types of elements:\n",
    "\n",
    "*   A variable `s`\n",
    "*   A function `say_hi()`\n",
    "*   A class `Greet`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e87285b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Contents of the module we are creating \n",
    "content = \"\"\"\n",
    "s = 'Hello ' \n",
    "\n",
    "def say_hi(name):\n",
    "    print(s + name)\n",
    "\n",
    "class Greet:\n",
    "    pass\n",
    "\"\"\"\n",
    "\n",
    "# Write the above text to a file called my_module.py\n",
    "# within our current working directory. \n",
    "with open('./my_module.py', 'w') as fp:\n",
    "    fp.write(content)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ede20263",
   "metadata": {},
   "source": [
    "This command writes (or saves) our module into our working directory, so that we can use it again."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b34febe7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import the module we've just made! \n",
    "import my_module "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d623b036",
   "metadata": {},
   "source": [
    "Even though we've imported our module, note that its contents (the variables and functions we've defined within the module) are not directly accessible to us. As such, attempting to access these elements will result in (namespace) errors being thrown. We can safely see such errors using a `try-except` block:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "86288085",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variable 's' does not exist!\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    # Try to print the variable s\n",
    "    print(s)\n",
    "except NameError:\n",
    "    # We've caught a NameError exception (error!)\n",
    "    # We inform the programmer (you) that the variable does not exist\n",
    "    print(\"Variable 's' does not exist!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9b8b6b2e",
   "metadata": {},
   "source": [
    "Learning from this experience, it is important to know that objects in a module are only accessible when prefixed with via dot notation, as illustrated below. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e920ba1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello '"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Accessing the variable s in my_module\n",
    "my_module.s "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "af5bf12c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Nelson\n"
     ]
    }
   ],
   "source": [
    "# Accessing the say_hi function in my_module\n",
    "my_module.say_hi('Nelson')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32b5b877",
   "metadata": {},
   "source": [
    "### Example: Importing modules using an alias\n",
    "The `import` statement in Python also allows for the use of aliases when referencing a module. Using the `as` keyword, we can save ourselves from having to type otherwise long package names each time we need to access an object from a given module/ package. This usually follows the following syntax:\n",
    "\n",
    "```python\n",
    "import <module_name> as <new_model_name>\n",
    "```\n",
    "or \n",
    "\n",
    "```python \n",
    "from <package_name> import <module_name> as <new_model_name>\n",
    "```\n",
    "\n",
    "for example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a2253207",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Alias for my_module\n",
    "import my_module as md"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "94a12604",
   "metadata": {},
   "source": [
    "We can thus treat the alias as the new name for the module. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "01824c3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello '"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Accessing the variable s using an alias\n",
    "md.s\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "34b57906",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Jabulani\n"
     ]
    }
   ],
   "source": [
    "# Accessing the say_hi function using an alias for my_module\n",
    "md.say_hi('Jabulani')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b5535f78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "my_module.Greet"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Accessing the empty class, Greet\n",
    "md.Greet"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c700f86",
   "metadata": {},
   "source": [
    "### Example: Importing modules directly\n",
    "Another way to access specific objects in a module is to use the `from` keyword and import them directly:\n",
    "\n",
    "```python \n",
    "from <module_name> import <x, y, z>\n",
    "``` "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fe38039e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from my_module import s, say_hi, Greet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52f51d01",
   "metadata": {},
   "outputs": [],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d45550ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Jabulani\n"
     ]
    }
   ],
   "source": [
    "say_hi('Jabulani')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6f53499c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "my_module.Greet"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Greet"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e5472586",
   "metadata": {},
   "source": [
    "We can see that using the `from xx import yy` structure provides access to the individual elements in the module without having to use dot notation. However, using aliases is the recommended way of importing modules and packages, as this prevents potential confusion when different modules contain functions or classes with the same name.\n",
    "\n",
    "To select all objects from a module we can use the following command, where the asterisk **( * )** *signifies all* :\n",
    "\n",
    "```python\n",
    "from <module_name> import*\n",
    "```\n",
    "Let's see this in practice one more time: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d4083840",
   "metadata": {},
   "outputs": [],
   "source": [
    "from my_module import * "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c3b09505",
   "metadata": {},
   "source": [
    "Now we have access to all our module contents"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "bb7c4281",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Joanne\n"
     ]
    }
   ],
   "source": [
    "say_hi('Joanne')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "712a1bb4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "my_module.Greet"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Greet"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "650b646a",
   "metadata": {},
   "source": [
    "## Built-in modules \n",
    "Python contains a large number of what are known as 'built-in' modules. These modules can be accessed in Python programs by simply importing them using their name preceded by the keyword `import`. \n",
    "\n",
    "Each built-in module contains resources for certain system-specific functionalities such as Operating System management, disk Input-Output, etc. Python scripts(with the **.py** extension) containing useful utilities are embedded within the standard library. \n",
    "\n",
    "To **display a list of all available modules**, use the following command:\n",
    "\n",
    "`help('modules')`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "82f12084",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Please wait a moment while I gather a list of all available modules...\n",
      "\n",
      "IPython             ast                 matplotlib_inline   tarfile\n",
      "Raisin_Data_set_Analysis_Model asttokens           mimetypes           telnetlib\n",
      "__future__          asyncio             mmap                tempfile\n",
      "__hello__           atexit              mmapfile            test\n",
      "__phello__          audioop             mmsystem            textwrap\n",
      "_abc                base64              modulefinder        this\n",
      "_aix_support        bdb                 msilib              threading\n",
      "_ast                binascii            msvcrt              time\n",
      "_asyncio            bisect              multiprocessing     timeit\n",
      "_bisect             builtins            my_module           timer\n",
      "_blake2             bz2                 nest_asyncio        tkinter\n",
      "_bz2                cProfile            netbios             token\n",
      "_codecs             calendar            netrc               tokenize\n",
      "_codecs_cn          cgi                 nntplib             tomllib\n",
      "_codecs_hk          cgitb               nt                  tornado\n",
      "_codecs_iso2022     chunk               ntpath              trace\n",
      "_codecs_jp          cmath               ntsecuritycon       traceback\n",
      "_codecs_kr          cmd                 nturl2path          tracemalloc\n",
      "_codecs_tw          code                numbers             traitlets\n",
      "_collections        codecs              odbc                tty\n",
      "_collections_abc    codeop              opcode              turtle\n",
      "_compat_pickle      collections         operator            turtledemo\n",
      "_compression        colorama            optparse            types\n",
      "_contextvars        colorsys            os                  typing\n",
      "_csv                comm                packaging           typing_extensions\n",
      "_ctypes             commctrl            parso               unicodedata\n",
      "_ctypes_test        compileall          pathlib             unittest\n",
      "_datetime           concurrent          pdb                 urllib\n",
      "_decimal            configparser        perfmon             uu\n",
      "_distutils_hack     contextlib          pickle              uuid\n",
      "_elementtree        contextvars         pickleshare         venv\n",
      "_functools          copy                pickletools         warnings\n",
      "_hashlib            copyreg             pip                 wave\n",
      "_heapq              crypt               pipes               wcwidth\n",
      "_imp                csv                 pkg_resources       weakref\n",
      "_io                 ctypes              pkgutil             webbrowser\n",
      "_json               curses              platform            wheel\n",
      "_locale             dataclasses         platformdirs        win2kras\n",
      "_lsprof             datetime            plistlib            win32api\n",
      "_lzma               dateutil            poplib              win32clipboard\n",
      "_markupbase         dbi                 posixpath           win32com\n",
      "_md5                dbm                 pprint              win32con\n",
      "_msi                dde                 profile             win32console\n",
      "_multibytecodec     debugpy             prompt_toolkit      win32cred\n",
      "_multiprocessing    decimal             pstats              win32crypt\n",
      "_opcode             decorator           psutil              win32cryptcon\n",
      "_operator           difflib             pty                 win32event\n",
      "_osx_support        dis                 pure_eval           win32evtlog\n",
      "_overlapped         doctest             py_compile          win32evtlogutil\n",
      "_pickle             email               pyclbr              win32file\n",
      "_py_abc             encodings           pydoc               win32gui\n",
      "_pydatetime         ensurepip           pydoc_data          win32gui_struct\n",
      "_pydecimal          enum                pyexpat             win32help\n",
      "_pyio               errno               pygments            win32inet\n",
      "_pylong             exceptiongroup      pythoncom           win32inetcon\n",
      "_queue              executing           pywin               win32job\n",
      "_random             faulthandler        pywin32_bootstrap   win32lz\n",
      "_sha1               filecmp             pywin32_testutil    win32net\n",
      "_sha2               fileinput           pywintypes          win32netcon\n",
      "_sha3               fnmatch             queue               win32pdh\n",
      "_signal             fractions           quopri              win32pdhquery\n",
      "_sitebuiltins       ftplib              random              win32pdhutil\n",
      "_socket             functools           rasutil             win32pipe\n",
      "_sqlite3            gc                  re                  win32print\n",
      "_sre                genericpath         regcheck            win32process\n",
      "_ssl                getopt              regutil             win32profile\n",
      "_stat               getpass             reprlib             win32ras\n",
      "_statistics         gettext             rlcompleter         win32rcparser\n",
      "_string             glob                runpy               win32security\n",
      "_strptime           graphlib            sched               win32service\n",
      "_struct             gzip                secrets             win32serviceutil\n",
      "_symtable           hashlib             select              win32timezone\n",
      "_testbuffer         heapq               selectors           win32trace\n",
      "_testcapi           hmac                servicemanager      win32traceutil\n",
      "_testclinic         html                setuptools          win32transaction\n",
      "_testconsole        http                shelve              win32ts\n",
      "_testimportmultiple idlelib             shlex               win32ui\n",
      "_testinternalcapi   imaplib             shutil              win32uiole\n",
      "_testmultiphase     imghdr              signal              win32verstamp\n",
      "_testsinglephase    importlib           site                win32wnet\n",
      "_thread             importlib_metadata  six                 winerror\n",
      "_threading_local    inspect             smtplib             winioctlcon\n",
      "_tkinter            io                  sndhdr              winnt\n",
      "_tokenize           ipaddress           socket              winperf\n",
      "_tracemalloc        ipykernel           socketserver        winreg\n",
      "_typing             ipykernel_launcher  sqlite3             winsound\n",
      "_uuid               isapi               sre_compile         winxpgui\n",
      "_warnings           itertools           sre_constants       winxptheme\n",
      "_weakref            jedi                sre_parse           wsgiref\n",
      "_weakrefset         json                ssl                 xdrlib\n",
      "_win32sysloader     jupyter             sspi                xml\n",
      "_winapi             jupyter_client      sspicon             xmlrpc\n",
      "_winxptheme         jupyter_core        stack_data          xxlimited\n",
      "_wmi                keyword             stat                xxlimited_35\n",
      "_xxinterpchannels   lib2to3             statistics          xxsubtype\n",
      "_xxsubinterpreters  linecache           string              zipapp\n",
      "_zoneinfo           locale              stringprep          zipfile\n",
      "abc                 logging             struct              zipimport\n",
      "adodbapi            lzma                subprocess          zipp\n",
      "afxres              mailbox             sunau               zlib\n",
      "aifc                mailcap             symtable            zmq\n",
      "antigravity         main                sys                 zoneinfo\n",
      "argparse            marshal             sysconfig           \n",
      "array               math                tabnanny            \n",
      "\n",
      "Enter any module name to get more help.  Or, type \"modules spam\" to search\n",
      "for modules whose name or summary contain the string \"spam\".\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help('modules') # this might take a while"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e7ff785",
   "metadata": {},
   "source": [
    "Alternatively, the `dir()` function is a built-in function that can be used to **list all the function names (or variable names) in a module**:\n",
    "\n",
    "`dir(module_name)`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1d2326d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The square root of 81 is equal to 9.0\n",
      "Functions in the math module: ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']\n"
     ]
    }
   ],
   "source": [
    "# Import math module \n",
    "import math \n",
    "\n",
    "# Use the sqrt function in the math module\n",
    "x = math.sqrt(81)\n",
    "print('The square root of 81 is equal to {}'.format(x))\n",
    "\n",
    "# List all functions in math module \n",
    "list_all= dir(math)\n",
    "print('Functions in the math module: {}'.format(list_all))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9956efe",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Summary\n",
    "\n",
    "In this train, we learned how to create, import and use modules. We also explored the use of built-in modules in Python and how to determine what functions are present within modules. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26fd094b-0fee-46f1-a4b8-73766813c42b",
   "metadata": {
    "tags": []
   },
   "source": [
    "#  \n",
    "\n",
    "<div align=\"center\" style=\" font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "<img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/master/ExploreAI_logos/EAI_Blue_Dark.png\"  style=\"width:200px\";/>\n",
    "</div>"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
