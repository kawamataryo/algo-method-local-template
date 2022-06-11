TASK = 1

up:
	docker-compose up -d

run_test:
	docker-compose run --rm python python tasks/${TASK}/test.py

generate_task:
	docker-compose run --rm python python scripts/generate_task.py ${TASK}