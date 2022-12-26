lint: black flake8 isort mypy

mypy:
	docker exec -it api poetry run mypy .

flake8:
	docker exec -it api poetry run pflake8 .

black:
	docker exec -it api poetry run black .

isort:
	docker exec -it api poetry run isort .

test:
	docker exec -it api pytest --cov=. --cov-report=xml	${ARG}