HOSTVOL=$(realpath ./app)
RUNCMD=docker run -p 8000:8000 -v $(HOSTVOL):/app -it --rm django-app

build:
	docker build -t django-app .

interactive:
	$(RUNCMD) /bin/bash

run:
	$(RUNCMD) ./run.sh

deploy: build run
