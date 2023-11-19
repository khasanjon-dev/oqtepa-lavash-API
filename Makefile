del:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete
make:
	python3 manage.py makemigrations
mig:
	python3 manage.py migrate
clean:
	isort .
add:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
