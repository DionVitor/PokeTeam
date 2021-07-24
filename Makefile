PURPLE := $(shell tput -Txterm setaf 5)
RESET := $(shell tput -Txterm sgr0)

start:
	$(info ${PURPLE}Starting containers.${RESET})
	@docker-compose up -d

build:
	$(info ${PURPLE}Building.${RESET})
	@docker-compose up -d --build

stop:
	$(info ${PURPLE}Stopping containers.${RESET})
	@docker-compose stop

restart:
	$(info ${PURPLE}Restarting containers.${RESET})
	@docker-compose stop
	@docker-compose up -d
