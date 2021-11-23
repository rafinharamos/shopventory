# Shopventory Challenge

Application to Shopventory challenge.

## Requirements

* Python 3

## Installation and run

In the linux terminal, run the commands:

$ python -m venv .schedule

$ source .schedule/bin/activate

$ pip install -r requirements.txt

$ python schedule.py

## Run unnit tests

$ python -m unittest schedule.py


### About the project
The idea of ​​the project was to meet all the prerequisites, however, one question remained:

In the case of days and hours, how would each schedule be distributed?

I started from the point that it works the same as scheduling minutes.

The idea of ​​improvement would be to put this in the docker or in a lambda for execution.