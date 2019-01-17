Author: EgbieAndersonUku1
Written in Python 3.64

Technologies used:

1) Behave
2) Selenium
3) Chrome


Program Goal
-------------

This an automation program I wrote in Python to perform the following task in Amazon. 

The goal of the program is to perform the scenario listed below:

Navigate to www.amazon.com and add the following books to your Amazon basket

1. 'Experiences of Test Automation: Case Studies of Software Test Automation'
2. 'Agile Testing: A Practical Guide for Testers and Agile Teams'
3. 'Selenium WebDriver 3 Practical Guide: End-to-end automation testing for web and mobile browsers
    with Selenium WebDriver, 2nd Edition'

4) Select the 'Save For Later' option for 'Experiences of Test Automation'
5) Select the 'Delete' option for 'Agile Testing'
6) Increase the quantity in your basket for 'Selenium WebDriver 3 Practical Guide' to 3 copies
7) Mark the order as a 'Gift'
8) Remove all copies of 'Selenium WebDriver 3 Practical Guide' from your basket

End the test


About the program/framework
-----------------

In certain places within the program I have scattered the 'sleep' method instead of the standard 
implicitly_wait method from the driver. This is to slow down the execution of methods when run in
succession and not to poll the dom.

I needed to slow down the execution of the function to give it the human delay and had 
used the implicitly_wait/Explicit_waits method to slow down the function execution,
but for every test that passed there were lot of others that were met with StaleException, 
which is an exception that is shown when an element is not yet rendered. The sleep method has 
only been used when executing a series of functions in a row to slow that executing of the function/method.

During testing...

I ran the program thirty times using implicitly_wait, twelve returned a StaleEXception 
stopping the execution of program. 

But when I used the sleep to replace the implicitly_wait to slow down the execution of function 
when executed one after the other I got only one exception. In fact I ran the program 
thirty times and out of that thirty I only got one StaleException. I have ran the program
additional times and there hasn't been anymore StaleException or TimeErrors.

In this case it happens while the program is running and the framework stop working. Just delete 
the basket and start again and it should be fine. The reason for deleting the basket is that I have
added checks that check the condition of the basket, if those conditions are not met an error will
be thrown.

I have tested the program on Windows and it works perfectly.


Running the program
-----------------------

To run the program you need to do the following things.

1) Run the requirement.txt file. This contains everything needed to run the program. 
   You can run it on its own or you can run inside a virtual environment. 
   To run the file enter the command 
   
   'pip -r requirement.txt'
    
    Note this command must be run in directory contain the requirement file


2) Download 'Chromedriver' unzip and add the path to line 26 in the 'chrome_driver_address'. 
   If you have not move the chromedriver from the download folder then the path way should be. 
   
   The chromedriver can be found here "http://chromedriver.chromium.org/downloads"
   
   Windows
   ---------
   
   
3) Open the add.py enter your 'username' and 'password' in variables for line 29 and 30. Enter the path for 
   the Chromedriver in which downloaded in step 1 in the 'chrome_driver_address' variable. 
   This should be the downloaded folder if you have not moved it. 
   
   In windows 10 the path should be:
   
   "chrome_driver_address ="C:\\Users\\<your username>\\Downloads\\chromedriver_win32\\chromedriver.exe"

4) Hit save to save the changes made
5) Navigate to the step folder and enter 'behave' in the command line.
