+++
type = "question"
title = "Osmosis fails on WIndows 7x64"
description = '''Hello, I downloaded the latest version of osmosis today (10/24/2014). Unzipped it and typed osmosis.exe and it looked correct. I got all the everything&#x27;s ok messages. Now I go to load a small pbf file, and I get this: &amp;gt; C:&#92;osmosis-latest&#92;bin&amp;gt;osmosis -v --read-pbf file=C:&#92;temp&#92;osm&#92;sample.pbf --...'''
date = "2014-10-24T16:19:00Z"
lastmod = "2014-10-24T17:09:00Z"
weight = 37926
keywords = [ "postgresql", "osmosis" ]
aliases = [ "/questions/37926" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis fails on WIndows 7x64](/questions/37926/osmosis-fails-on-windows-7x64)

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
<span id="post-37926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37926-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I downloaded the latest version of osmosis today (10/24/2014). Unzipped it and typed osmosis.exe and it looked correct. I got all the everything's ok messages.</p>
<p>Now I go to load a small pbf file, and I get this:</p>
<pre><code>&gt; C:\osmosis-latest\bin&gt;osmosis -v --read-pbf file=C:\temp\osm\sample.pbf --buffer
 bufferCapacity=100000 --log-progress --write-apidb host=localhost database=test
osm user=&lt;username&gt; password=&lt;password&gt;
Oct 24, 2014 11:10:07 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.43.1
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.TaskRegistrar loadJPFPlu
gins
FINE: Searching for JPF plugins.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.TaskRegistrar loadJPFPlu
gins
FINE: Registering the core plugin.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.TaskRegistrar loadJPFPlu
gins
FINE: Registering the extension plugins.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.Pipeline
 prepare
FINE: Building tasks.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.Pipeline
 buildTasks
FINE: Created task &quot;1-read-pbf&quot;
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.Pipeline
 buildTasks
FINE: Created task &quot;2-buffer&quot;
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.Pipeline
 buildTasks
FINE: Created task &quot;3-log-progress&quot;
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.Pipeline
 buildTasks
FINE: Created task &quot;4-write-apidb&quot;
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.Pipeline
 prepare
FINE: Connecting tasks.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.PipeTask
s putTask
FINE: Task &quot;1-read-pbf&quot; produced unnamed pipe stored at level 1 in the default p
ipe stack.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.Pipeline
 connectTasks
FINE: Connected task &quot;1-read-pbf&quot;
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.PipeTask
s retrieveTask
FINE: Task &quot;2-buffer&quot; consumed unnamed pipe stored at level 1 in the default pip
e stack.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.PipeTask
s putTask
FINE: Task &quot;2-buffer&quot; produced unnamed pipe stored at level 1 in the default pip
e stack.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.Pipeline
 connectTasks
FINE: Connected task &quot;2-buffer&quot;
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.PipeTask
s retrieveTask
FINE: Task &quot;3-log-progress&quot; consumed unnamed pipe stored at level 1 in the defau
lt pipe stack.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.PipeTask
s putTask
FINE: Task &quot;3-log-progress&quot; produced unnamed pipe stored at level 1 in the defau
lt pipe stack.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.Pipeline
 connectTasks
FINE: Connected task &quot;3-log-progress&quot;
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.PipeTask
s retrieveTask
FINE: Task &quot;4-write-apidb&quot; consumed unnamed pipe stored at level 1 in the defaul
t pipe stack.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.Pipeline
 connectTasks
FINE: Connected task &quot;4-write-apidb&quot;
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTa
skManager execute
FINE: Launching task 1-read-pbf in a new thread.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTa
skManager execute
FINE: Launching task 2-buffer in a new thread.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.PassiveT
askManager execute
FINE: Task 3-log-progress is passive, no execution required.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.PassiveT
askManager execute
FINE: Task 4-write-apidb is passive, no execution required.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
Oct 24, 2014 11:10:08 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTa
skManager waitForCompletion
FINE: Waiting for task 1-read-pbf to complete.
Oct 24, 2014 11:10:09 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTa
skManager waitForCompletion
SEVERE: Thread for task 1-read-pbf failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: An output error has occu
rred, aborting.
        at org.openstreetmap.osmosis.core.store.DataPostbox.checkForOutputErrors
(DataPostbox.java:160)
        at org.openstreetmap.osmosis.core.store.DataPostbox.populateCentralQueue
(DataPostbox.java:216)
        at org.openstreetmap.osmosis.core.store.DataPostbox.put(DataPostbox.java
:303)
        at org.openstreetmap.osmosis.core.buffer.v0_6.EntityBuffer.process(Entit
yBuffer.java:48)
        at crosby.binary.osmosis.OsmosisBinaryParser.parseDense(OsmosisBinaryPar
ser.java:138)
        at org.openstreetmap.osmosis.osmbinary.BinaryParser.parse(BinaryParser.j
ava:124)
        at org.openstreetmap.osmosis.osmbinary.BinaryParser.handleBlock(BinaryPa
rser.java:68)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlock.process(FileBlock.
java:135)
        at org.openstreetmap.osmosis.osmbinary.file.BlockInputStream.process(Blo
ckInputStream.java:34)
        at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:45)
        at java.lang.Thread.run(Unknown Source)
&#10;Oct 24, 2014 11:10:09 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTa
skManager waitForCompletion
FINE: Waiting for task 2-buffer to complete.
Oct 24, 2014 11:10:09 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTa
skManager waitForCompletion
SEVERE: Thread for task 2-buffer failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to create results
et.
        at org.openstreetmap.osmosis.apidb.common.DatabaseContext.executeQuery(D
atabaseContext.java:429)
        at org.openstreetmap.osmosis.apidb.v0_6.impl.SchemaVersionValidator.vali
dateDBVersion(SchemaVersionValidator.java:82)
        at org.openstreetmap.osmosis.apidb.v0_6.impl.SchemaVersionValidator.vali
dateVersion(SchemaVersionValidator.java:55)
        at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.initialize(ApidbWrit
er.java:324)
        at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.process(ApidbWriter.
java:1089)
        at org.openstreetmap.osmosis.core.progress.v0_6.EntityProgressLogger.pro
cess(EntityProgressLogger.java:71)
        at org.openstreetmap.osmosis.core.buffer.v0_6.EntityBuffer.run(EntityBuf
fer.java:84)
        at java.lang.Thread.run(Unknown Source)
Caused by: org.postgresql.util.PSQLException: ERROR: relation &quot;schema_migrations
&quot; does not exist
  Position: 21
        at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryEx
ecutorImpl.java:2103)
        at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutor
Impl.java:1836)
        at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.ja
va:257)
        at org.postgresql.jdbc2.AbstractJdbc2Statement.execute(AbstractJdbc2Stat
ement.java:512)
        at org.postgresql.jdbc2.AbstractJdbc2Statement.executeWithFlags(Abstract
Jdbc2Statement.java:374)
        at org.postgresql.jdbc2.AbstractJdbc2Statement.executeQuery(AbstractJdbc
2Statement.java:254)
        at org.openstreetmap.osmosis.apidb.common.DatabaseContext.executeQuery(D
atabaseContext.java:424)
        ... 7 more
&#10;Oct 24, 2014 11:10:09 AM org.openstreetmap.osmosis.core.pipeline.common.PassiveT
askManager waitForCompletion
FINE: Task 3-log-progress is passive, no completion wait required.
Oct 24, 2014 11:10:09 AM org.openstreetmap.osmosis.core.pipeline.common.PassiveT
askManager waitForCompletion
FINE: Task 4-write-apidb is passive, no completion wait required.
Oct 24, 2014 11:10:09 AM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed
.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForComple
tion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.lang.reflect.Method.invoke(Unknown Source)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Laun
cher.java:329)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.jav
a:239)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(La
uncher.java:409)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:
352)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
<p>Not pretty at all I know, but I don't know where to start to debug this issue. Can anyone provide some insight into this issue?</p>
<p>Thanks A</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '14, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/728321acc3469682288102302efc6341?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajc2014&#39;s gravatar image" />
<p><span>ajc2014</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajc2014 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '14, 16:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-37926" class="comments-container">
<span id="37927"></span>
<div id="comment-37927" class="comment">
<div id="post-37927-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am starting with a clean database, postgresql 9.2 x64, postgis 2.0, I ran the create schema scripts before trying to run osmosis as well.</p>
</div>
<div id="comment-37927-info" class="comment-info">
<span class="comment-age">(24 Oct '14, 16:22)</span> <span class="comment-user userinfo">ajc2014</span>
</div>
</div>
<span id="37928"></span>
<div id="comment-37928" class="comment">
<div id="post-37928-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you already check whether the PBF file is broken?</p>
</div>
<div id="comment-37928-info" class="comment-info">
<span class="comment-age">(24 Oct '14, 16:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="37929"></span>
<div id="comment-37929" class="comment">
<div id="post-37929-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can load the pbf using osm2pgsql, but not using osmosis. I wanted to change from osm2pgsql to osmosis, because I want to load the whole planet and osm2pgsql crashes whereas it has been reported that osmosis will load the whole planet on a windows box.</p>
</div>
<div id="comment-37929-info" class="comment-info">
<span class="comment-age">(24 Oct '14, 16:37)</span> <span class="comment-user userinfo">ajc2014</span>
</div>
</div>
<span id="37930"></span>
<div id="comment-37930" class="comment">
<div id="post-37930-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are there environmental parameters I need to set outside of the batch file?</p>
</div>
<div id="comment-37930-info" class="comment-info">
<span class="comment-age">(24 Oct '14, 16:38)</span> <span class="comment-user userinfo">ajc2014</span>
</div>
</div>
<span id="37932"></span>
<div id="comment-37932" class="comment">
<div id="post-37932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/8708/mmd">@mmd</a> does this allow you to update the database?</p>
</div>
<div id="comment-37932-info" class="comment-info">
<span class="comment-age">(24 Oct '14, 17:09)</span> <span class="comment-user userinfo">ajc2014</span>
</div>
</div>
</div>
<div id="comment-tools-37926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37926-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

