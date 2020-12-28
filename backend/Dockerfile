FROM python:3.7.4

# Create app directory
RUN mkdir -p /usr/src/app

# Install app dependencies
COPY doit.sh stable-req.txt /
RUN sh doit.sh init

# Bundle app source
WORKDIR /usr/src/app
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"


EXPOSE 8002

ENTRYPOINT [ "python3", "index.py" ]
