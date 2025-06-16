+++
type = "question"
title = "Import into MySQL - &quot;Unable to create resultset&quot;"
description = '''I&#x27;m trying to import OSM data into MySQL and get stuck at this error. Below is the full output. This is a Windows 7 x64 machine with a fresh MySQL install. I just created a database named osm and nothing more. Then, I executed this command: osmosis --read-pbf D:&#92;osm&#92;germany.osm.pbf --write-apidb dbT...'''
date = "2012-10-09T21:18:00Z"
lastmod = "2012-10-17T23:45:00Z"
weight = 16770
keywords = [ "import", "mysql" ]
aliases = [ "/questions/16770" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Import into MySQL - "Unable to create resultset"](/questions/16770/import-into-mysql-unable-to-create-resultset)

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
<span id="post-16770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16770-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to import OSM data into MySQL and get stuck at this error. Below is the full output. This is a Windows 7 x64 machine with a fresh MySQL install. I just created a database named <code>osm</code> and nothing more. Then, I executed this command:</p>
<pre><code>osmosis --read-pbf D:\osm\germany.osm.pbf --write-apidb dbType=mysql host=localhost database=osm user=root password=xxx</code></pre>
<p>And I get the following output:</p>
<pre><code>okt 09, 2012 10:13:44 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.41
okt 09, 2012 10:13:44 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
okt 09, 2012 10:13:44 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
okt 09, 2012 10:13:44 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
okt 09, 2012 10:13:44 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-pbf failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to create resultset.
        at org.openstreetmap.osmosis.apidb.common.DatabaseContext.executeQuery(DatabaseContext.java:429)
        at org.openstreetmap.osmosis.apidb.v0_6.impl.SchemaVersionValidator.validateDBVersion(SchemaVersionValidator.java:82)
        at org.openstreetmap.osmosis.apidb.v0_6.impl.SchemaVersionValidator.validateVersion(SchemaVersionValidator.java:55)
        at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.initialize(ApidbWriter.java:324)
        at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.process(ApidbWriter.java:1089)
        at crosby.binary.osmosis.OsmosisBinaryParser.parse(OsmosisBinaryParser.java:247)
        at crosby.binary.BinaryParser.handleBlock(BinaryParser.java:64)
        at crosby.binary.file.FileBlock.process(FileBlock.java:135)
        at crosby.binary.file.BlockInputStream.process(BlockInputStream.java:34)
        at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:45)
        at java.lang.Thread.run(Unknown Source)
Caused by: com.mysql.jdbc.exceptions.jdbc4.MySQLSyntaxErrorException: Table &#39;osm.schema_migrations&#39; doesn&#39;t exist
        at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
        at sun.reflect.NativeConstructorAccessorImpl.newInstance(Unknown Source)
        at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(Unknown Source)
        at java.lang.reflect.Constructor.newInstance(Unknown Source)
        at com.mysql.jdbc.Util.handleNewInstance(Util.java:411)
        at com.mysql.jdbc.Util.getInstance(Util.java:386)
        at com.mysql.jdbc.SQLError.createSQLException(SQLError.java:1052)
        at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:3609)
        at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:3541)
        at com.mysql.jdbc.MysqlIO.sendCommand(MysqlIO.java:2002)
        at com.mysql.jdbc.MysqlIO.sqlQueryDirect(MysqlIO.java:2163)
        at com.mysql.jdbc.ConnectionImpl.execSQL(ConnectionImpl.java:2618)
        at com.mysql.jdbc.ConnectionImpl.execSQL(ConnectionImpl.java:2568)
        at com.mysql.jdbc.StatementImpl.executeQuery(StatementImpl.java:1557)
        at org.openstreetmap.osmosis.apidb.common.DatabaseContext.executeQuery(DatabaseContext.java:424)
        ... 10 more
&#10;okt 09, 2012 10:13:44 PM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.lang.reflect.Method.invoke(Unknown Source)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:329)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:239)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:409)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:352)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
<p>What did I do wrong, and what should I do?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '12, 21:18</strong></p>
<img src="https://secure.gravatar.com/avatar/eaec145585ef24a947b9e2fed5d6c4ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thany&#39;s gravatar image" />
<p><span>thany</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thany has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16770" class="comments-container">
&#10;</div>
<div id="comment-tools-16770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16770-form-container" class="comment-form-container">
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

<span id="16980"></span>

<div id="answer-container-16980" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16980-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I believe you need to populate the database with a schema before doing the import i.e. create appropriate tables containing appropriate fields</p>
<p>It looks like support for MySQL may go away at some point as Openstreetmaps is moving to PostgreSQL, so you may be better off starting with PostgreSQL anyhow.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '12, 21:16</strong></p>
<img src="https://secure.gravatar.com/avatar/7408fce5260e98922355385680be0179?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="porjo&#39;s gravatar image" />
<p><span>porjo</span><br />
<span class="score" title="183 reputation points">183</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="porjo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16980" class="comments-container">
<span id="16985"></span>
<div id="comment-16985" class="comment">
<div id="post-16985-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The thing is, Postgres doesn't do very well on Windows, but Windows is the most used OS out there (whether we like it or not). I do have a linux box that I can try it on, but it's not nearly as powerful as my windows box.</p>
<p>Even for Portgres, the documentation is not clear on how to populate the database initially. I'm not sure what exactly to do at that point. Partly because I'm not familiar at all with Postgres (I have literally never used it), and partly because it's just not very clear to me what needs to be done exactly.</p>
</div>
<div id="comment-16985-info" class="comment-info">
<span class="comment-age">(17 Oct '12, 23:11)</span> <span class="comment-user userinfo">thany</span>
</div>
</div>
<span id="16988"></span>
<div id="comment-16988" class="comment">
<div id="post-16988-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Never used it myself, but a bit of poking on the wiki revealed that there should be something to generate the database structure in a directory named "script/contrib" with your osmosis download.</p>
<p>See: <a href="https://wiki.openstreetmap.org/wiki/Osmosis#DB_Schema">https://wiki.openstreetmap.org/wiki/Osmosis#DB_Schema</a></p>
</div>
<div id="comment-16988-info" class="comment-info">
<span class="comment-age">(17 Oct '12, 23:45)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-16980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16980-form-container" class="comment-form-container">
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

