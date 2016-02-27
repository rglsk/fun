# Fun
Crawlers, bots and robots.

### Dependencies:
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Postgresql](http://www.postgresql.org.pl/)
* [SQLAlchemy](http://www.sqlalchemy.org/)
* [Docker](https://www.docker.com/)
* [Docker-compose](https://docs.docker.com/compose/)
* [GoogleSeach](https://pypi.python.org/pypi/googlesearch/0.7.0)

### Instalation:
```$ pip install docker-compose```

#### Run dev environment:

```$ docker-compose up -d```

#### Display running containers:

```$ docker ps```

#### Enter docker container:

```$ docker exec -it <CONTAINER_ID> bash```

####Run application:

```$ python main.py ```


## Project 1:

### Description:

Half-automatic system for crawling interestiong results from google search engine.

* User is able to enter phrases for search
* User is able to tag which result is interesting (or is not)
* User is able to check results which are only interesting (or not interesting)
* User is able to dump database to file
* System is creating query and saving it to database
* System displays collected results for user

