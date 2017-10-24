agggregator
------------

The aggregator API is a backend application that is used to aggregate content from community sites.
It is built on the backbone of [Django](djangoproject.com), [GraphQL](graphql.org) and [PostgreSQL](https://www.postgresql.org/)

The default container (for development) is shipped with docker-compose.

## Set up developer enviroment

Run `docker-compose up`
And that's it. You can now access the instance at [http://localhost:8000](http://localhost:8000)

### Run initial migrations

You can run the migrations with `docker-compose run python3 manage.py migrate`

### Run unit tests

Unit tests can be run with `docker-compose run python3 manage.py test`

### Documentation

The documentation is self-contained via [GraphiQL](https://github.com/graphql/graphiql) and served at the index of the application.

### Changing the default external port
You can set `EXTERNAL_PORT=80` as an environment variable to change the default port.

## Set up a productive environment without Docker

This application can be as well set up without Docker quiet easily.
It requires you to have the following prerequisites:

- a ready PostgreSQL server
- Python3.5 or higher

Follow these steps:

```
virtualenv -p /usr/local/bin/python3 venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Deployment is done [via uWSGI](https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/uwsgi/)
