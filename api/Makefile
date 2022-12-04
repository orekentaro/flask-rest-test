lint: black flake8 isort mypy

mypy:
	poetry run mypy .

flake8:
	poetry run pflake8 .

black:
	poetry run black .

isort:
	poetry run isort .

test:
	docker exec -it api pytest --cov=. --cov-report=xml	${ARG}