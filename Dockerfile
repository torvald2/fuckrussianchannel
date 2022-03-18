FROM python:buster

COPY . . 

ENV RUN_IN_DOCKER=true

RUN pip install -r requirements.txt

CMD  ["bash"]
