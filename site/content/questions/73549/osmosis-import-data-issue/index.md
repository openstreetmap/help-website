+++
type = "question"
title = "osmosis import data issue"
description = '''I imported a geofabrik extract of a small area (Liechtenstein) into my local osm website database to test if it works, the imported data appeared in iD editor, I can edit it and everything went fine as shown in the following copy&amp;amp;paste of terminal. But when I tried with a bigger dataset (southea...'''
date = "2020-03-16T18:56:00Z"
lastmod = "2020-03-18T23:24:00Z"
weight = 73549
keywords = [ "openstreetmap" ]
aliases = [ "/questions/73549" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmosis import data issue](/questions/73549/osmosis-import-data-issue)

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
<span id="post-73549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73549-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I imported a geofabrik extract of a small area (Liechtenstein) into my local osm website database to test if it works, the imported data appeared in iD editor, I can edit it and everything went fine as shown in the following copy&amp;paste of terminal.</p>
<p>But when I tried with a bigger dataset (southeast of Brazil) it toke all night long and gave me the following error. I think the data has not been imported because nothing appeared in iD editor.</p>
<p>I'm using ubuntu 18.04 my specs are: 500 GB SSD 16 GB RAM i7-8550U</p>
<pre><code>cadu@cadu-Inspiron-7773:~/Downloads/osmosis-0.47.1/bin$ ./osmosis --read-pbf /home/cadu/Downloads/liechtenstein-latest.osm.pbf   --write-apidb host=&quot;localhost&quot; database=&quot;openstreetmap&quot;   user=&quot;openstreetmap&quot; password=&quot;openstreetmap&quot; validateSchemaVersion=&quot;no&quot;
mar 15, 2020 6:56:16 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.47.1-1-g80be2971
mar 15, 2020 6:56:16 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
mar 15, 2020 6:56:16 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
mar 15, 2020 6:56:16 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
mar 15, 2020 6:57:20 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline complete.
mar 15, 2020 6:57:20 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Total execution time: 64617 milliseconds.
cadu@cadu-Inspiron-7773:~/Downloads/osmosis-0.47.1/bin$ ./osmosis --read-pbf /home/cadu/Downloads/sudeste-latest.osm.pbf   --write-apidb host=&quot;localhost&quot; database=&quot;openstreetmap&quot;   user=&quot;openstreetmap&quot; password=&quot;openstreetmap&quot; validateSchemaVersion=&quot;no&quot;
mar 15, 2020 7:00:08 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.47.1-1-g80be2971
mar 15, 2020 7:00:08 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
mar 15, 2020 7:00:08 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
mar 15, 2020 7:00:08 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
mar 16, 2020 12:42:07 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-pbf failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to load current nodes.
at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentNodes(ApidbWriter.java:1006)
at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentTables(ApidbWriter.java:1107)
at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.complete(ApidbWriter.java:1141)
at crosby.binary.osmosis.OsmosisBinaryParser.complete(OsmosisBinaryParser.java:35)
at org.openstreetmap.osmosis.osmbinary.file.BlockInputStream.process(BlockInputStream.java:37)
at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:45)
at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.postgresql.util.PSQLException: ERROR: duplicate key value violates unique constraint &quot;current_nodes_pkey1&quot;
  Detail: Key (id)=(15755281) already exists.
at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2440)
at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:2183)
at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:308)
at org.postgresql.jdbc.PgStatement.executeInternal(PgStatement.java:441)
at org.postgresql.jdbc.PgStatement.execute(PgStatement.java:365)
at org.postgresql.jdbc.PgPreparedStatement.executeWithFlags(PgPreparedStatement.java:143)
at org.postgresql.jdbc.PgPreparedStatement.execute(PgPreparedStatement.java:132)
at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentNodes(ApidbWriter.java:1003)
... 6 more
&#10;mar 16, 2020 12:42:07 AM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
at java.base/java.lang.reflect.Method.invoke(Method.java:566)
at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330)
at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415)
at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356)
at org.codehaus.classworlds.Launcher.main(Launcher.java:47)
&#10;cadu@cadu-Inspiron-7773:~/Downloads/osmosis-0.47.1/bin$</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '20, 18:56</strong></p>
<img src="https://secure.gravatar.com/avatar/5f1f061e7e81f0e885227d27d95752f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlosguedes&#39;s gravatar image" />
<p><span>carlosguedes</span><br />
<span class="score" title="91 reputation points">91</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlosguedes has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Mar '20, 19:51</strong> </span></p>
</div>
</div>
<div id="comments-container-73549" class="comments-container">
&#10;</div>
<div id="comment-tools-73549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73549-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="73550"></span>

<div id="answer-container-73550" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73550-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The node that the database complains about (15755281) is near Bludenz, in Austria, and not in Brazil. This node may be part of your Liechtenstein import due to its membership in the "Rätikon" multipolygon, however it is unclear to me why a Brazil import should trigger a duplicate key error here. Make sure to clear your database and re-try.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '20, 19:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-73550" class="comments-container">
<span id="73553"></span>
<div id="comment-73553" class="comment">
<div id="post-73553-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you.I truncated the database with osmosis and now I'm re-importing Brazil southeast again. When it ends I come with the results.</p>
</div>
<div id="comment-73553-info" class="comment-info">
<span class="comment-age">(16 Mar '20, 22:01)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
<span id="73579"></span>
<div id="comment-73579" class="comment">
<div id="post-73579-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, the southeast Brazil data has been imported, I could see and edit it through iD and manually added some points in the map. But then I imported the Liechtenstein pbf and now seems like another node is complaining.<img src="https://i.imgur.com/0BaDQg9.png" alt="alt text" /></p>
</div>
<div id="comment-73579-info" class="comment-info">
<span class="comment-age">(17 Mar '20, 16:53)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
<span id="73615"></span>
<div id="comment-73615" class="comment">
<div id="post-73615-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suspect these 2 datasets have an common node key.</p>
</div>
<div id="comment-73615-info" class="comment-info">
<span class="comment-age">(18 Mar '20, 23:24)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
</div>
<div id="comment-tools-73550" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73550-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

