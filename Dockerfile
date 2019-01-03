FROM python:3-alpine as build
LABEL maintainer="don@agilicus.com"

COPY . /elastic-prune
WORKDIR /elastic-prune

RUN rm -rf .git && pip install --target=./ -r requirements.txt

FROM gcr.io/distroless/python3
COPY --from=build /elastic-prune /elastic-prune
WORKDIR /elastic-prune
ENTRYPOINT ["/usr/bin/python3", "./elastic-prune.py"]


