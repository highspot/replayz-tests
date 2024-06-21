CURRENT_DIR := $(shell pwd)

run:
	docker build -t replayziq-tests .
	docker run -v "$(CURRENT_DIR)/output:/app/output" replayziq-tests
