# Catalog App

Catalog Webapp project to practice Python, Flask and Oauth 2.0

You can simply access [this Heroku server](https://cryptic-wave-60279.herokuapp.com/) and test it.

#### Login functionality only works on the Heroku server for security issues.

Please issue `client_secrets.json` for [Google](https://console.developers.google.com), and `APP_ID`, `APP_SECRET` for [Facebook](https://developers.facebook.com) if you want to test it on local machines.

Then replace `catalog/config/client_secrets.json` for Google, or modify `catalog/config/config.py` for Facebook login.


## Quick start

Several quick start options are available:

* Download [the latest Vagrant](https://www.vagrantup.com/downloads.html) and install.
* Clone the repo: `git clone https://github.com/softage0/catalog-webapp.git`.
* Run the following code on the cloned repo:
```
$ vagrant up (It would take several minutes to install and setup the relevant environment.)
$ vagrant ssh
```
* Run runserver.py
```
vagrant$ cd /vagrant
vagrant$ python runserver.py
```


## Run like Heroku Environment

When the changes are pushed into Github repository, it is automatically triggered to deploy such changes on Heroku server. 

On local machine, it can be tested just like Heroku environment by the following command:

```
vagrant$ cd /vagrant
vagrant$ foreman start web
```


## Setup Local Database for Offline Development

It uses Heroku Postgres database but it can be switched to local SQLite database to develop offline by the following command.

* Switch DB_URL on catalog/config/config.py:
> DB_URL="postgres://..." -> DB_URL="sqlite:///catalog/catalog.db" 

* Setup local dummy database
```
$ vagrant ssh
vagrant$ cd /vagrant
vagrant$ python /catalog/database_setup.py
vagrant$ python /catalog/dummy_db_generator.py
```
