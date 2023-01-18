.PHONY: push-all
push-all:
	@docker push gleif/vlei --all-tags

.PHONY: build-vlei
build-vlei:
	@docker buildx build --platform=linux/amd64 --no-cache -f container/Dockerfile --tag gleif/vlei:latest --tag gleif/vlei:0.1.0 .


.PHONY: run-dev
run-dev:
	docker compose up -d
	mvn spring-boot:run -Dspring-boot.run.profiles=dev

#### Added by Wahid
.PHONY: build-image
build-image:
	docker build --file container/Dockerfile . \
		--tag provenant-dev/vlei \
		--tag ghcr.io/provenant-dev/vlei

.PHONY: push-tag
push-tag:
	docker push ghcr.io/provenant-dev/vlei
