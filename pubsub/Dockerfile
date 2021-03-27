FROM google/cloud-sdk:latest

EXPOSE 8085

VOLUME /data
CMD ["gcloud", "beta", "emulators", "pubsub", "env-init"]
ENTRYPOINT ["gcloud", "beta", "emulators", "pubsub"]
CMD ["start", "--project=stock-news-summarizer", "--host-port=0.0.0.0:8085", "--data-dir=/data"]