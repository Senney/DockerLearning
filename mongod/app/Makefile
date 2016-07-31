build:
	docker build -t mongo-app .

run:
	docker run --rm -it --link mongodb:mongo mongo-app

deploy: build run
