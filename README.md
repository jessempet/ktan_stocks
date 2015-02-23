
#Configuring your environment

1.  Install Python 2.7.3 from the python.org website
2.  Edit your environmental variables path to allow for executing python from the command line. https://docs.python.org/2/using/windows.html will show you how.  This essentially allows you to type "python" in the command prompt and it will open an interactive shell
3.  Install pypy (pip) from https://pypi.python.org/pypi/pip.  Pip is an installation manager that will help you install third party python packages.  In the case of this project, you will need ystockquote.  Once PIP is installed, you can simply type "pip install ystockquote" in to a command prompt; this will install all needed dependencies to add this to the python lib.  After installing, open a python interactive shell (type "python" on the command prompt) and then type "import ystockquote".  If you do not get an error, then it has installed correctly
4.  Exit python (ctrl+d on linux, exit() on any playform and see below

#How to use
Windows:
1. Open stocks.py and change line 62's variabl spfile to the location of your file in quotes
2. Change sp500_avgs.csv to the desireable name (ending in .csv)
3. Save the python script
4. run cmd.exe
5. Try python stocks.py.  If your environmental variables are not set--> c:\Python27\python.exe stocks.py
6. Enter a start date in YYYY-MM-DD, hit enter
7. Enter an end date in YYYY-MM-DD, hit enter
8. Depending on how long your date range is, a csv will be compiled and stored in the directory that the code is running to

Linux:

1. Open stocks.py and change line 62's variabl spfile to the location of your file in quotes
2. Change sp500_avgs.csv to the desireable name (ending in .csv)
3. Save the python script
4. Type python stocks.py
6. Enter a start date in YYYY-MM-DD, hit enter
7. Enter an end date in YYYY-MM-DD, hit enter
8. Depending on how long your date range is, a csv will be compiled and stored in the directory that the code is running to


  
