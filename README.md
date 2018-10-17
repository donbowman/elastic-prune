## elastic-prune

This script cleans older logstash indexes from Elasticsearch,
and restores the indices to read-write (in case it had run out
of disk space).

## Usage

```
elastic-prune -e elastic-url [-d days]
```

You may wish to install the Kubernetes CronJob:

```
kubectl -n logging apply -f cron.yaml
```

You can use the image from [Dockerhub](https://hub.docker.com/r/donbowman/elastic-prune/)
instead of the internal cr.agilicus.com on, in which case you might
remove the imagePullSecrets: line in the cron.

Public image is donbowman/elastic-prune
