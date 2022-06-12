TASK = 1

up:
	docker-compose up -d

run_test:
	docker-compose run --rm python python scripts/run_test/run_test.py ${TASK}

generate_task:
	docker-compose run --rm python python scripts/generate_task/generate_task.py ${TASK}