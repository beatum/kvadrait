# TEST CASE / FOR KVADRA-IT

This project is scaffolded by Ivan Semernyakov <direct@beatum-group.ru>

## Architecture

Tested on:

* Ubuntu 14.04
* Python 3.6.3
* PostgreSQL 9.6.1
* Django 2.0
* Django Rest Framework 3.7.3
* Bootstrap 4.0.0-alpha.6 from CDN
* jQuery 3.2.1 from CDN

## Usage

#### Clone project:
```
$ mkdir test_project && cd $_
$ git clone https://github.com/beatum/kvadrait.git
```

#### Initialize ```virtualenv``` if needed! Different ways:
```
$ virtualenv -p python3.6 {path}
$ virtualenv -p /usr/bin/python3.6 {path}
$ python3.6 -m venv /path/to/new/virtual/environment
```

#### Activate ```virtualenv```:
```
$ source {virtualenv_path}/bin/activate
```

#### Install ```pip``` dependencies using ```./requirements.txt``` they are not already installed:
```
$ cd kvadrait
$ pip install -r requirements.txt
```

#### Verify ```pip``` dependencies installed correctly under ```virtualenv```:
```
$ which django-admin.py
```

#### Configure PostgreSQL if needed:
```
$ sudo su postgres
$ createuser -P username
$ createdb --owner username dbname
$ exit
```

Check up settings.py !

#### Apply initial migration:
```
$ ./manage.py migrate
```

#### Create admin user:
```
$ ./manage.py createsuperuser
```

#### Test environment
```
$ ./manage.py runserver
```

Now you can go to the localhost:8000 and you should see "Hello, World!" - page.

### That's all! Good luck!

## License

This software is released under the [MIT License](http://opensource.org/licenses/MIT).

