FROM python:3.6

RUN python3.6 --version && pip3 --version

RUN mkdir /simplereq
COPY requirements.txt /simplereq
WORKDIR /simplereq

RUN pip install -r requirements.txt

COPY main.py /simplereq
COPY entrypoint.sh /simplereq
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
CMD ["hi"]
