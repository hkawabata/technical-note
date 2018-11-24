---
title: トラブルシューティング
---

# コレクションのリカバリー失敗

SolrCloud において

- leader.server.jp：リーダーノード
- replica.server.jp：リーダーではないレプリカを持つノード
- samplecollection：コレクション名

リーダーノードでこんな感じのエラーログ

```
ERROR	DistributedUpdateProcessor	Setting up to try to start recovery on replica http://replica.server.jp:8983/solr/samplecollection_shard1_replica3/

WARN	LeaderInitiatedRecoveryThread	Leader is publishing core=samplecollection_shard1_replica3 coreNodeName =core_node10 state=down on behalf of un-reachable replica http://replica.server.jp:8983/solr/samplecollection_shard1_replica3/

ERROR	StreamingSolrClients	error

ERROR	RequestHandlerBase	org.apache.solr.common.SolrException: I was asked to wait on state recovering for shard1 in samplecollection on replica.server.jp:8983_solr but I still do not see the requested state. I see state: down live:true leader from ZK: http://leader.server.jp:8983/solr/samplecollection_shard1_replica9/
```


