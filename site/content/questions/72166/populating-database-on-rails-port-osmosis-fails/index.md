+++
type = "question"
title = "Populating database on Rails Port - Osmosis fails"
description = '''Hi All, I have successfully installed the Rails Port e.g. I can see openstreetmap website from localhost. Now, I want to populate the database with my own map. To do so, I run the following comand: osmosis --read-pbf /mnt/share/entre_rios-latest.osm.pbf --write-apidb host=&quot;localhost&quot; database=&quot;opens...'''
date = "2019-12-19T16:26:00Z"
lastmod = "2019-12-19T20:01:00Z"
weight = 72166
keywords = [ "osmosis", "railsport" ]
aliases = [ "/questions/72166" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Populating database on Rails Port - Osmosis fails](/questions/72166/populating-database-on-rails-port-osmosis-fails)

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
<span id="post-72166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72166-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I have successfully installed the Rails Port e.g. I can see openstreetmap website from localhost. Now, I want to populate the database with my own map. To do so, I run the following comand:</p>
<pre><code>osmosis --read-pbf /mnt/share/entre_rios-latest.osm.pbf
--write-apidb host=&quot;localhost&quot; database=&quot;openstreetmap&quot; user=&quot;osmweb&quot; password=&quot;osmweb&quot; validateSchemaVersion=&quot;no&quot;</code></pre>
<p>However, command fails because Osmosis is unable to insert a user into the database. Moreover, it seems that a column is missing. Looking at tables "users", "relations", and similar names; results that none of them has a field "nearby".</p>
<p>Here is the log:</p>
<pre><code>Dec 19, 2019 3:39:22 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-pbf failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to insert user with id 678132 into the database.
    at org.openstreetmap.osmosis.apidb.v0_6.impl.UserManager.insertUser(UserManager.java:115)
    at org.openstreetmap.osmosis.apidb.v0_6.impl.UserManager.addOrUpdateUser(UserManager.java:163)
    at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.process(ApidbWriter.java:1169)
    at crosby.binary.osmosis.OsmosisBinaryParser.parseDense(OsmosisBinaryParser.java:138)
    at org.openstreetmap.osmosis.osmbinary.BinaryParser.parse(BinaryParser.java:124)
    at org.openstreetmap.osmosis.osmbinary.BinaryParser.handleBlock(BinaryParser.java:68)
    at org.openstreetmap.osmosis.osmbinary.file.FileBlock.process(FileBlock.java:135)
    at org.openstreetmap.osmosis.osmbinary.file.BlockInputStream.process(BlockInputStream.java:34)
    at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:45)
    at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.postgresql.util.PSQLException: ERROR: column &quot;nearby&quot; of relation &quot;users&quot; does not exist
  Position: 129
    at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2440)
    at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:2183)
    at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:308)
    at org.postgresql.jdbc.PgStatement.executeInternal(PgStatement.java:441)
    at org.postgresql.jdbc.PgStatement.execute(PgStatement.java:365)
    at org.postgresql.jdbc.PgPreparedStatement.executeWithFlags(PgPreparedStatement.java:143)
    at org.postgresql.jdbc.PgPreparedStatement.executeUpdate(PgPreparedStatement.java:120)
    at org.openstreetmap.osmosis.apidb.v0_6.impl.UserManager.insertUser(UserManager.java:112)
    ... 9 more
&#10;Dec 19, 2019 3:39:22 PM org.openstreetmap.osmosis.core.Osmosis main
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
    at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
<p>If database is created by the Ruby script, how could a column be missing? Is it possible that there is some mistake, or a missing step? Any help would be appreciated. Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '19, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/c5a0c6984a6c127cc7973b20b670e3bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoseBLJ&#39;s gravatar image" />
<p><span>JoseBLJ</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoseBLJ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '19, 19:19</strong> </span></p>
</div>
</div>
<div id="comments-container-72166" class="comments-container">
&#10;</div>
<div id="comment-tools-72166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72166-form-container" class="comment-form-container">
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

<span id="72171"></span>

<div id="answer-container-72171" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72171-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JoseBLJ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a known issue see <a href="https://github.com/openstreetmap/openstreetmap-website/issues/2449">https://github.com/openstreetmap/openstreetmap-website/issues/2449</a> in general you should be looking in the github repo first when you have issues installing.</p>
<p>BTW this should be trivial to fix if you can build osmosis yourself. The larger issue is that osmosis currently has no volunteer maintainer and nobody seems to be willing to pay somebody to do the job.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '19, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '19, 22:56</strong> </span></p>
</div>
</div>
<div id="comments-container-72171" class="comments-container">
&#10;</div>
<div id="comment-tools-72171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72171-form-container" class="comment-form-container">
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

