import os
import base64
from time import sleep
import json
from google.cloud import pubsub_v1
from flask import Flask, current_app, escape, request, jsonify
from flask_cors import CORS, cross_origin
from ML.models.stockNewsRating import getStockNewsTitleRating


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['PUBSUB_VERIFICATION_TOKEN'] = os.environ['PUBSUB_VERIFICATION_TOKEN']
cors = CORS(app)
app.config['MESSAGES'] = []


@app.route('/hello', methods=['GET'])
@cross_origin()
def hello():
    return {
        'result': f'Hello, {escape(app.config["MESSAGES"])}!'
    }


@app.route('/generate-stock-news-rating', methods=['POST'])
def generateStockNewsRating():
    envelope = json.loads(request.data.decode('utf-8'))
    article = base64.b64decode(envelope['message']['data']).decode("utf-8")
    article = json.loads(article)
    results = getStockNewsTitleRating(article)
    app.logger.info(f"{results['rate']}: {results['title']}")

    return "OK", 200


@app.route('/create-stock-news-title-subscription', methods=['GET'])
def createStockNewsTitleSubscription():
    projectId = request.args.get("projectId", "stock-news-summarizer")
    topicId = request.args.get("topicId", "stockNewsTitle")
    subscriptionId = request.args.get("subscriptionId", "stockNewsTitleSubscription")
    endpoint = "http://backend:8002/generate-stock-news-rating"
    timeout = 5.0

    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = publisher.topic_path(projectId, topicId)
    subscription_path = subscriber.subscription_path(projectId, subscriptionId)

    push_config = pubsub_v1.types.PushConfig(push_endpoint=endpoint)

    # Wrap the subscriber in a 'with' block to automatically call close() to
    # close the underlying gRPC channel when done.
    with subscriber:
        subscription = subscriber.create_subscription(
            request={
                "name": subscription_path,
                "topic": topic_path,
                "push_config": push_config,
            }
        )

    app.logger.info(f"Push subscription created: {subscription}.")
    app.logger.info(f"Endpoint for subscription is: {endpoint}")

    # Returning any 2xx status indicates successful receipt of the message.
    return 'OK', 200


@app.route('/post-stock-news-title', methods=['POST'])
def postStockNewsTitle():
    projectId = request.args.get("projectId", "stock-news-summarizer")
    topicId = request.args.get("topicId", "stockNewsTitle")

    publisher = pubsub_v1.PublisherClient()
    app.logger.info(publisher)
    topic_path = publisher.topic_path(projectId, topicId)
    app.logger.info(topic_path)
    try:
        publisher.create_topic(request={"name": topic_path})
    except Exception:
        app.logger.error('Couldnt create a topic')

    with open('/usr/src/app/ML/files/newfilterMock.json') as f:
        data = json.load(f)
    app.logger.info(data)
    for article in data['articles']:
        app.logger.info(article)
        future = publisher.publish(topic_path, data=json.dumps(article).encode('utf-8'))
        app.logger.info(future.result())
        sleep(5)
    return {
        'result': 'Success'
    }



if __name__ == '__main__':
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8002
    app.run(host="0.0.0.0", port=PORT, debug=True)

