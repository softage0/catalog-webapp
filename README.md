# Catalog App

Catalog Webapp project to practice Python, Flask and Oauth 2.0


## Quick start

Several quick start options are available:

* Download [the latest Vagrant](https://www.vagrantup.com/downloads.html) and install.
* Clone the repo: `git clone https://github.com/softage0/catalog-webapp.git`.
* Run the following code on the cloned repo:
```
$ vagrant up (It would take several minutes to install and setup the relevant environment.)
```
* Run the following code to setup the initial database:
```
$ vagrant ssh
vagrant$ cd /vagrant
vagrant$ python /catalog/database_setup.py
vagrant$ python /catalog/dummy_db_generator.py
```
* Run runserver.py
```
/vagrant/catalog$ python runserver.py
```
