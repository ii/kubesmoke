FROM python:alpine
MAINTAINER Eugene Zilman <ezilman@gmail.com>

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY tests /tests

EXPOSE 8000
CMD ["python"]
ARG ["/tests/incr.py"]
