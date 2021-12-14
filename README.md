
# Description

It's app based on DRF + Celery created for working with big csv files.
## Installation

For working with this project we will need couple of libraries.

This version of app isn't ready for deploy and it's uses only for local testing and experiments.

### Docker Installation

The most simplest way to start and working with this library will be docker.

To combine all clusters of this app we need to do following:
```bash
  docker compose up --build -d
```

### Separate installation

First of all we need redis to manage our processes 
```bash
  # installation of redis
  wget http://download.redis.io/redis-stable.tar.gz
  tar xvzf redis-stable.tar.gz
  cd redis-stable
  make
```
That enough for working but we also can install redis in different ways.

```bash
  # ubuntu
  sudo apt install redis
  # arch 
  sudo pacman -Syu redis
  # snap installation
  sudo snap isntall redis 
```

To start this redis server type:
```bash
  redis-server
```

Also we will need python libraries

```bash
  cd project
  poetry install
```
That operations will install all required python libraries that have place in project.

Execute every block of this to start all models of project
```bash
  cd project
  poetry shell
  # start celery
  celery -A core worker --loglevel=INFO
  # start flower
  celery -A core flower --loglevel=INFO
  poetry shell
  # start our web server
  python manage.py runserver
```
## Usage

For sending request to calculate value you can send  request to ulr
```bash
http://localhost:8000/async_csv/files?file=data.csv
```

For watching statistics about all celery operations go to 
```bash
http://localhost:5555
```
To get all operations you can watch
```bash
http://localhost:8000/tasks/
```
To watch statistic about specific operation go to with task_id given from your request
```bash
http://localhost:8000/tasks/<task_id>/
```
To create dop files 
```bash
  python utils.py > files/your_file_name.csv
```
You can change SIZE in utils.py to change size of creation csv-file.