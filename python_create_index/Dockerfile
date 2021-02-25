FROM python:3.6

WORKDIR /python_create_index

ADD . /python_create_index

RUN pip install elasticsearch 

ENTRYPOINT [ "python" ]
CMD [ "create_index.py" ]
