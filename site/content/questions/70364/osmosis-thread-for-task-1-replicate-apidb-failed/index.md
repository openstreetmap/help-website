+++
type = "question"
title = "Osmosis: Thread for task 1-replicate-apidb failed"
description = '''I am using Ubuntu 18.04 LTS. I have created local version of openstreetmap-website, by this guide. I have filled up database with initial script osmosis --read-pbf andorra-latest.osm.pbf --write-apidb host=&quot;localhost:5432&quot; database=&quot;openstreetmap&quot; user=&quot;postgres&quot; password=&quot;postgres&quot; validateSchemaVe...'''
date = "2019-08-12T12:46:00Z"
lastmod = "2019-08-12T12:46:00Z"
weight = 70364
keywords = [ "osmosis" ]
aliases = [ "/questions/70364" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis: Thread for task 1-replicate-apidb failed](/questions/70364/osmosis-thread-for-task-1-replicate-apidb-failed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70364-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using <code>Ubuntu 18.04 LTS</code>.</p>
<p>I have created local version of openstreetmap-website, by <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">this guide</a>.</p>
<p>I have filled up database with initial script <code>osmosis --read-pbf andorra-latest.osm.pbf --write-apidb host="localhost:5432" database="openstreetmap" user="postgres" password="postgres" validateSchemaVersion="no"</code>.</p>
<p>Now, it's time to get replica from DB.</p>
<p>Here's a command: <code>osmosis --replicate-apidb authFile=localBackendAuthFile.txt validateSchemaVersion=false --write-replication workingDirectory=~/osmosisworkdir</code></p>
<p>And the output:</p>
<blockquote>
<p>Aug 12, 2019 12:10:06 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.46 Aug 12, 2019 12:10:06 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. Aug 12, 2019 12:10:06 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Launching pipeline execution. Aug 12, 2019 12:10:06 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline executing, waiting for completion. WARNING: An illegal reflective access operation has occurred WARNING: Illegal reflective access by org.postgresql.jdbc.TimestampUtils (file:/usr/share/java/postgresql.jar) to field java.util.TimeZone.defaultTimeZone WARNING: Please consider reporting this to the maintainers of org.postgresql.jdbc.TimestampUtils WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations WARNING: All illegal access operations will be denied in a future release Aug 12, 2019 12:10:07 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion SEVERE: Thread for task 1-replicate-apidb failed java.lang.NumberFormatException: null at java.base/java.lang.Long.parseLong(Long.java:655) at java.base/java.lang.Long.parseLong(Long.java:817) at org.openstreetmap.osmosis.apidb.v0_6.impl.ReplicationState.load(ReplicationState.java:80) at org.openstreetmap.osmosis.replication.v0_6.ReplicationStateWriter.initialize(ReplicationStateWriter.java:74) at org.openstreetmap.osmosis.replication.v0_6.ReplicationWriter.initialize(ReplicationWriter.java:46) at org.openstreetmap.osmosis.apidb.v0_6.impl.Replicator.replicateImpl(Replicator.java:293) at org.openstreetmap.osmosis.apidb.v0_6.impl.Replicator.access$000(Replicator.java:20) at org.openstreetmap.osmosis.apidb.v0_6.impl.Replicator$1.run(Replicator.java:263) at org.openstreetmap.osmosis.apidb.v0_6.impl.TransactionDao$1.doInTransactionWithoutResult(TransactionDao.java:61) at org.springframework.transaction.support.TransactionCallbackWithoutResult.doInTransaction(TransactionCallbackWithoutResult.java:34) at org.springframework.transaction.support.TransactionTemplate.execute(TransactionTemplate.java:133) at org.openstreetmap.osmosis.apidb.common.DatabaseContext2.executeWithinTransaction(DatabaseContext2.java:94) at org.openstreetmap.osmosis.apidb.v0_6.impl.TransactionDao.executeWithinTransaction(TransactionDao.java:58) at org.openstreetmap.osmosis.apidb.v0_6.impl.Replicator.replicateLoop(Replicator.java:260) at org.openstreetmap.osmosis.apidb.v0_6.impl.Replicator.replicate(Replicator.java:242) at org.openstreetmap.osmosis.apidb.v0_6.ApidbFileReplicator.runImpl(ApidbFileReplicator.java:89) at org.openstreetmap.osmosis.apidb.v0_6.ApidbFileReplicator.run(ApidbFileReplicator.java:99) at java.base/java.lang.Thread.run(Thread.java:834) Aug 12, 2019 12:10:07 PM org.openstreetmap.osmosis.core.Osmosis main SEVERE: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed. at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146) at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92) at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) at java.base/java.lang.reflect.Method.invoke(Method.java:566) at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330) at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238) at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415) at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356) at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</p>
</blockquote>
<p>What is wrong and how can I fix it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '19, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/d77b49acd7cf6026b0c5bf860ee111c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YUNtee&#39;s gravatar image" />
<p><span>YUNtee</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YUNtee has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Aug '19, 12:48</strong> </span></p>
</div>
</div>
<div id="comments-container-70364" class="comments-container">
&#10;</div>
<div id="comment-tools-70364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70364-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

