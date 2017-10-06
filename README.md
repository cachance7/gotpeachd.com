# gotpeachd.com

A silly site that farts at you and renders unfurlable content based on subdomain

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).

```sh
$ git clone git@github.com:cachance7/gotpeachd.com.git
$ cd gotpeachd.com

$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic

$ python manage.py runserver
```

Your app should now be running locally on port 8000.

Put this in `/etc/hosts` to test:

```sh
# gotpeachd subdomain test
test.gotpeachd.com 127.0.0.1
```

Open this in a browser to see:

`http://test.gotpeachd.com:8000`

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
