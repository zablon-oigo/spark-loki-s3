

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