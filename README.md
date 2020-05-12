# Parleto recruitment task
Web application written with Python 3.8 and Django, a recruitment task

## Table of contents
1. [Required features](#required-features)
2. [Installation](#installation)
3. [Database](#database)
4. [Tests and lint](#tests-and-lint)
5. [Author](#author)
6. [License](#license)

## Required features
List of features required for finishing this task:
   1. Allow searching by date range in `expenses.ExpenseList`.
   2. Allow searching by multiple categories in `expenses.ExpenseList`.
   3. In `expenses.ExpenseList` add sorting by category and date (ascending and descending)
   4. In `expenses.ExpenseList` add grouping by category name (ascending and descending)
   5. In `expenses.ExpenseList` add total amount spent.

   6. Add list view for `expenses.Category`.
   7. Add number of expenses per category per row in `expenses.CategoryList`.

   8. Add create view for `expenses.Category`.
   9. Add update view for `expenses.Category`.
   10. Add message for create/update in `expenses.Category` if name already exists

   11. Add delete view for `expenses.Category`.
   12. In `expenses.CategoryDelete` add total count of expenses that will be deleted.

   13. Add detail view for `expenses.Category` with total summary per year-month.

   14. Add option to change perPage items on list views.
   15. Add total items to `_pagination.html`

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

## Database
These steps will help you prepare the demo data used in the app

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

**Note**: Using the above command will create a new docker container with each run. It can provide some memory issues when development process is still running and the software is often tested. You can clear them all after some time with:
```
./remove_test_containers.sh
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