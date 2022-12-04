create_data:
	docker exec -it api python create_table.py

db_shell:
	docker exec -it db psql -U postgres

run_client:
	npm run -C client dev

install_node:
	npm install --frozen-lockfile -C client

run_docker:
	docker compose up

run_build:
	docker compose up -d --build

down:
	docker compose down

data_crear:
	docker volume rm recruit-management_pgdata

dalete_image:
	docker rmi recruit-management-api

del:
	make down
	make dalete_image
	make data_crear

reset:
	make del
	make init

run_init: run_build install_node create_data

init:
	make run_init
	make down
	make run

run:
	make -j start

start: run_client run_docker

lint:
	docker exec -it api make -j lint
