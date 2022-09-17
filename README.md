# ignite-solution-machine-test

## Setup
```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt


```

## Run project
```shell
python manage.py runserver 
```

### Get all record
```shell
localhost:8000/api/v1/books/
```

### Get record using filtration

```shell
http://localhost:8000/api/v1/books/?book_id=1342&lang=en&author=bur&title=the%20south&mime_type=application%2Fx-mobipocket-ebook&topic=Manufactures
```