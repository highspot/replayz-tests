CURRENT_DIR := $(shell pwd)

run:
	docker build -t tests .
	docker run -v "$(CURRENT_DIR)/output:/app/output" tests
