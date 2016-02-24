dndtools
==========

An open source Django-based wiki-like web application for DnD.

This is a fork of https://github.com/antoinealb/dndtools

I have modified the configuration to meet my needs. I have also edited the templates slightlty.

There is no database included in the repo. This version is setup to run MySql instead of Sqlite.


Installation
------------
We will install the project in a virtual environment.
Virtualenvs allow to easily isolate the project dependencies from your system install.

The following instruction were tested on Linux, but should work on OSX and Windows as well.
The only requirements are Python 2.7 and Virtualenv.

To install DnDTools, run the following commands:

```sh
# Install MySql and python libraries
apt-get install git mysql-server python-dev python-mysqldb

# Setup MySql database
mysql -u root -pdndtools -e "create database dndtools;"
mysql -u root -pdndtools -e "grant all on dndtools.* to 'dndtools'@'localhost' identified by 'dndtools';"

# Import any dndtools MySql database that you like 

# Clone the repository (my fork of DndTools)
git clone https://github.com/gregpechiro/dndtools.git
cd dndtools/

# Create a Python Virtual environment in env/ and enables it
virtualenv --python=python2.7 env
source env/bin/activate

# First we have to install an old version of django-reversion, which is not in PyPI
pip install https://github.com/etianen/django-reversion/archive/release-1.3.3.zip

# Then install all the requirements from the PyPI
pip install -r requirements.txt

# install MySqldb for python
pip install MySQL-python

# Copy the default settings for development
cd dndtools/
cp local.py.sample local.py

# Finally, run the development server.
python manage.py runserver 0.0.0.0:8000

# Your own version of DnDTools is now available at http://127.0.0.1:8000
```
