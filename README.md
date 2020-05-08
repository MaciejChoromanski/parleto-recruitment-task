# Parleto recruitment task
Web application written with Python 3.8 and Django

## Table of contents
1. [Installation](#installation)
2. [Tests and lint](#tests-and-lint)
3. [Author](#author)
4. [License](#license)

## Installation
These steps will help you set up the project on your machine. They were written with UNIX/UNIX-like based systems in mind.

### With Docker
You'll need [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) to set up this project properly

Build the project:
```
docker-compose build
```

Run the project:
```
docker-compose up
```

### Without Docker
(Optional) Create virtual environment and activate it:
```
virtualenv venv && source venv/bin/activate
```
**Note**: If you're not using virtual environment make sure to use the proper version of [Python](https://www.python.org/)

Install requirements:
```
pip install -r requirements.txt
```

Run migrations:
```
python project/manage.py migrate
```

Load data:
```
python project/manage.py loaddata project/fixtures.json
```

Run the project:
```
python project/manage.py runserver
```

## Tests and lint

### With Docker
```
docker-compose run web sh -c "cd project && python manage.py test && flake8"
```

### Without Docker
Make sure to be in the /project/ directory
```
python manage.py test && flake8
```

## Author
* **Maciej Choromański** - GitHub: [MaciejChoromanski](https://github.com/MaciejChoromanski), LinkedIn: [mchoromanski](https://www.linkedin.com/in/mchoromanski/)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details