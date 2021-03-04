# A Weather App

## What does it do?
This web-based weather application built with Django allows users to search weather information based on a specific city.

Users go to the web page where there's a search bar and type in any city's name which they are interested in. After
clicking "Add", the system will automatically display new weather information on the web page based on the city
they searched previously.

Existing weather information can also be deleted from the page by the user clicking on the "X" above which city's weather
they wish no longer to see.

## Why is it useful?
It makes weather forecasting more easily available and essential weather information succinct.

## How to install
1. Open the ```final_project``` folder. It should contain
    * 3 folders, ```final_project```, ```weather_app```, and ```venv```
    * 1 python file named ```manage.py```
    * 1 database file name ```db.sqlite3```
    * any system-generated files which can be ignored
2. Open Terminal and direct to the path of the directory using the ```cd``` command.
3. In the command line, type ```source venv/bin/activate``` to activate virtual environment.
    * This will result in having ```(venv)``` at the beginning of your command line.
    * To exit virtual environment, simply run command ```deactivate```.
4. Before running the program, we have to make sure that necessary modules such as **Django** and **requests** are 
installed now that we're in virtual environment.
    * To do so, simply run ```pip install -r requirements.txt```
5. Now we can start the program by running ```./manage.py runserver```.
    * The running message will provide a local URL that might look like ```http://127.0.0.1:8000/```. Copy and paste it
    to a Chrome browser or any browser of your choosing.
    * Go to the link and you should be able to see the working application.
6. To terminate the program in your terminal, tap ```Control + C```. 

## How to test
1. Same directory, in the command line, run command ```./manage.py test weather_app```.
    * Running message prints ```OK``` indicating all 3 tests passed.