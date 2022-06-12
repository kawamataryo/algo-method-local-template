No = 1

up:
	docker-compose up -d

run_test:
	docker-compose run --rm python python scripts/run_test/run_test.py ${No}

get_question:
	docker-compose run --rm python python scripts/get_question/get_question.py ${No}