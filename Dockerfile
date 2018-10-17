FROM python:3-alpine
LABEL maintainer="don@agilicus.com"

COPY . /elastic-prune
WORKDIR /elastic-prune

RUN pip install -r /elastic-prune/requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "./elastic-prune.py"]


