# Fun
Crawlers, bots and robots.

### Dependencies:
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Postgresql](http://www.postgresql.org.pl/)
* [SQLAlchemy](http://www.sqlalchemy.org/)
* [Docker](https://www.docker.com/)
* [Docker-compose](https://docs.docker.com/compose/)
* [GoogleSeach](https://pypi.python.org/pypi/googlesearch/0.7.0)
* [Scrapy](http://doc.scrapy.org/en/latest/index.html)

## Project 1:

### Description:

Half-automatic system for crawl interestiong results from google search engine.

* User is able to enter phrases for search
* User is able to tag which result is interesting (or is not)
* User is able to check results which are only interesting (or not interesting)
* User is able to dump database to file
* System is creating query and saving it to database
* System displays collected results for user

## Project 2

### Description

Searcher for robots.txt files.

* System is able to download many polish websites
* Searching and sorting by robots.txt fields
* Finding interesting stuff in files

### Instalation:
```$ pip install docker-compose```

Run dev environment:

```$ docker-compose up -d```

Display running containers:

```$ docker ps```

Enter docker container:

```$ docker exec -it <CONTAINER_ID> bash```

Run application:

```$ python main.py ```

## Console scripts


| Script name        | Description                                          | Project |
| ------------------ |:----------------------------------------------------:| -------:|
| `search_engine`    | Terminal client                                      |     1   |
| `crawl_links`      | Crawl polish links                                   |     2   |
| `crawl_robots`     | Crawl robots.txt files for links (if they exists)    |     2   |
| `find_interesting` | Finding interesting stuff in robots.txt              |     2   |