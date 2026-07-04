DC = docker compose
MONGO = docker_compose/mongo.yaml
MONGO_EXPRESS = docker_compose/mongo-express.yaml
ENV = --env-file .env

ruff-lint:
	ruff check .

ruff-fix-lint:
	ruff check --fix .

ruff-format:
	ruff format .

mongo-up:
	${DC} -f ${MONGO} -f ${MONGO_EXPRESS} ${ENV} up --build -d

mongo-down:
	${DC} -f ${MONGO} -f ${MONGO_EXPRESS} ${ENV} down
