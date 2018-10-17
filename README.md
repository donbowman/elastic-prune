## elastic-prune

This script cleans older logstash indexes from Elasticsearch,
and restores the indices to read-write (in case it had run out
of disk space).

## Usage

```
elastic-prune -e elastic-url [-d days]
```
