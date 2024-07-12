build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d --remove-orphans

down:
	docker compose down

down-v:
	docker compose down -v

makemigrations:
	docker compose run app python manage.py makemigrations

tox:
	docker compose run app tox

delete-agreements:
	docker compose run app python manage.py delete_requisitions

migrate:
	docker compose run app python manage.py migrate

collectstatic:
	docker compose run app python manage.py collectstatic --no-input --clear

superuser:
	docker compose run app python manage.py createsuperuser

startapp:
	docker compose run app python manage.py startapp $(filter-out $@,$(MAKECMDGOALS))

