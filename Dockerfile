FROM python:3.10.13-slim

RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
      g++ \
      gcc && \
    # clean up temporary files
    rm -rf /var/cache/*

RUN pip install --upgrade pip && \
    pip install poetry && \
    # clean up temporary files
    rm -rf /tmp/* && \
    rm -rf /root/.cache/*
