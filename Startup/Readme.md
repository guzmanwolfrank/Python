# Startup 

Created a program that allows you to choose which files you do not want to open automatically when you start up your Windows OS Computer.


## Objective 
To minimize startup times on my laptop and computer.  I wanted to create a program which outlined the files being started up and then allowed me to delete them from the startup list. 

## Challenges 
I found it challenging to compose an if statement that itirated within the winreg module. 

## Solution
I was able to find [documentation](https://docs.python.org/3/library/winreg.html) which helped me form the if statement and necessary functions. 
These included functions to list and delete startup tasks and programs. 

## Deployment

1. To run this program, download the [file](https://github.com/guzmanwolfrank/Python/blob/main/Startup/startup_programs.py). Open command prompt and make sure you have python downloaded. You can do this by typing:

        python --version

You do not need to install winreg separately as it is included in your Python installation. 


2. Next, run the program by moving to the appropriate download folder in the command prompt. Use cd to change drives. Then type in the command prompt or terminal:



        Type:  python NameofFile.py


3. The program should run and open.


    When you run it on command prompt it should look like this:


![runprog](https://user-images.githubusercontent.com/29739578/229173025-95577ed1-678b-4e2f-9af2-c102852be1d1.jpg)






- Alternatively -
You can also copy and paste the code in the  [code file](https://github.com/guzmanwolfrank/Python/blob/main/Startup/startup_programs.py) after typing "python" and ENTER into a command prompt or Windows Powershell.

![carbon (5)](https://github.com/guzmanwolfrank/Python/assets/29739578/d2a042f3-386e-4b36-a51c-522a256a1d5b)



## Tech Stack

winreg==Windows10 </br>
python==3.11.3

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## License

[MIT](https://choosealicense.com/licenses/mit/)



   


