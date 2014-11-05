#!/usr/bin/env python
import os

from elasticsearch import Elasticsearch
es = Elasticsearch(os.environ["BOOT2DOCKER_IP"])

res = es.search(index="doc-index", body={
    "query": {
        "query_string": {
            "query": {
                "query_string": {
                    "query": "*zlib*"
                }
                }
        }
    }
})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print(hit["_source"])
