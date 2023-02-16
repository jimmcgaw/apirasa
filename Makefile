
build:
	docker compose build

buildup:
	docker compose up -d --build

logs:
	docker compose logs app -f

start:
	docker compose up -d

stop:
	docker compose down

restart:
	docker compose restart

# boot up actions server in container on port 5055.
actions:
	docker compose exec rasachat rasa run actions

rasash:
	docker compose exec rasachat rasa shell

train:
	docker compose exec rasachat rasa train