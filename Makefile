create_data:
	docker exec -it recruit-management-api python create_table.py

dbshell:
	docker exec -it recruit-management-db psql -U postgres

run_client:
	npm run -C client dev

install_node:
	npm install --frozen-lockfile -C client

run_docker:
	docker compose up -d

run_build:
	docker compose up -d --build

down:
	docker compose down

data_crear:
	docker volume rm recruit-management_pgdata

dalete_image:
	docker rmi recruit-management_api

reset:
	make down
	make dalete_image
	make data_crear

start:
	make run_build
	make install_node
	make create_data
	make run_client

restart:
	make reset
	make start

run:
	make run_docker
	make run_client
