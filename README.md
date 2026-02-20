## Logs Aggregation Pipeline

This project demonstrates how to build a scalable log aggregation and processing pipeline. It collects raw logs, stores them in Amazon S3, processes them using Apache Spark, and transforms them into optimized Parquet format for analytics and team insights.

The pipeline enables efficient log storage, querying, and downstream analysis for engineering, DevOps, and analytics teams.

#### Architecture Diagram

```sh
# step 1 loki
loki -config.file=loki-config.yaml -config.expand-env=true

# step 2: promtail
promtail -config.file=promtail-config.yaml

```

Verify logs
```sh
curl "http://localhost:3100/loki/api/v1/labels"
```
Check labels
```sh
curl "http://localhost:3100/loki/api/v1/labels"
```