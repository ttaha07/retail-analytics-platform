.PHONY: install test docker-build docker-test pipeline

install:
	pip install -r requirements.txt

test:
	pytest tests/data_quality_checks.py -v -p no:cacheprovider

docker-build:
	docker build -t retail-analytics-pipeline .

docker-test:
	docker run --env-file .env retail-analytics-pipeline pytest tests/data_quality_checks.py -v -p no:cacheprovider

pipeline:
	python orchestration/pipeline.py