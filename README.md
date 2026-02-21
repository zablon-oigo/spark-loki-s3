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


Add Required JARs

```sh
cd /opt/spark/jars/
wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.6/hadoop-aws-3.3.6.jar
wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.777/aws-java-sdk-bundle-1.12.777.jar
wget https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-4.0_2.13/1.10.1/iceberg-spark-runtime-4.0_2.13-1.10.1.jar \
-O /opt/spark/jars/iceberg-spark-runtime-4.0_2.13-1.10.1.jar

```
Spark Default Config

```sh
# Iceberg config
spark.sql.extensions    org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
spark.sql.catalog.spark_catalog    org.apache.iceberg.spark.SparkSessionCatalog
spark.sql.catalog.spark_catalog.type  hadoop
spark.sql.catalog.spark_catalog.warehouse file:///tmp/iceberg-warehouse 
spark.sql.defaultCatalog     spark_catalog

```

