FROM python:3.7.4

# Create app directory
RUN mkdir -p /usr/src/app

# Install app dependencies
COPY doit.sh stable-req.txt /
RUN sh doit.sh init

# Bundle app source
ADD . /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"
ENV PUBSUB_PROJECT_ID "stock-news-summarizer"
ENV PUBSUB_VERIFICATION_TOKEN "stocknewsummarizertoken"

EXPOSE 8002

ENTRYPOINT [ "python3", "index.py" ]
