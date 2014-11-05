#!/usr/bin/env python
import os
import json

from elasticsearch import Elasticsearch
es = Elasticsearch(os.environ["BOOT2DOCKER_IP"])

for item in json.load(open("/Users/chassing/workspace/instadoc/instadoc/main/fixtures/initial_data.json")):
    es.index(index="doc-index", doc_type='doc', id=item['pk'], body=item)

es.indices.refresh(index="doc-index")
