# pipenv-tutorial

This is a basic Django project built to demonstrate the principles of [pipenv](https://docs.pipenv.org/).

## Requirements

- Python 3 - `brew install python3`
- Virtualenv - `pip install virtualenv`


## Local development

#### Installation

1.  Clone this repo.
2.  `virtualenv venv -p python3` to create a local environment.
3.  `source venv/bin/activate` to enter this environment.
4.  `pip install -r requirements-dev.txt`.


#### Configuration.

1.  `source venv/bin/activate` to enter our virtualenv (if not still set from earlier).
2.  `python manage.py migrate` to create the initial data tables.
3.  `python manage.py createsuperuser` to make an admin user.
4.  `python manage.py runserver` to run a development server


#### Switching to `pipenv`

1.  `brew install pipenv` to install.
2.  `export PIPENV_VENV_IN_PROJECT=1` to configure virtualenv placement.
3.  `pipenv install --three`

#### What's inside

-   `project/`: Project-wide settings and config.
-   `todos`: The specific app (for creating todo lists and items) we'll be running for the demo.
-   `manage.py`: Django's shell-executable file.
-   `requirements-dev.txt`: Specific dependencies needed to hack on this project.
-   `requirements.in`: The top-level list of pinned dependencies needed to run this project in any environment (production or development).
-   `requirements.txt`: The full (generated) list of pinned dependencies needed to run this project in any environment.

## Copyright

&copy;2018 The Dallas Morning News
