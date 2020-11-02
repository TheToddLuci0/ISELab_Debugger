This project is designed to be easily deployed by those with no knowledge
of systems administration. To that goal, the following details the steps
to deploy this code.

## All steps assume you have cloned this code, and are in the directory you cloned it to

Run the following commands, one at a time.
```shell script
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

The above does the following:
1. Create a python virtual environment. This prevents conflicts with other python
  programs.
1. Activate the virtual environment. This tells your shell to use the new environment.
1. Install the project requirements.
1. Initialize the local SQLITE3 database.

To run the server, run 
```shell script
python manage.py runserver
```
Note that this runs a _development_ server. This is not really intended for
a traditional "production" deployment, nor would I recommend hosting this publicly.
If you wish to do so, the process is documented 
[here](https://docs.djangoproject.com/en/3.1/howto/deployment/).
