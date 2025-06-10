+++
type = "question"
title = "How to interpret this Java error?"
description = '''Hello, I have been attempting to import a north-america-latest.osm.pbf (from Geofabrik) into a Postgres database for some time. After reviewing the wiki detailed usage page thoroughly, I set the database to include all necessary tables (pgSnapshot) via the included sql scripts. I also made sure that...'''
date = "2018-07-19T22:49:00Z"
lastmod = "2018-07-19T22:49:00Z"
weight = 64808
keywords = [ "openstreetmap", "postgresql", "osmosis", "postgis" ]
aliases = [ "/questions/64808" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to interpret this Java error?](/questions/64808/how-to-interpret-this-java-error)

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
<span id="post-64808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64808-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have been attempting to import a north-america-latest.osm.pbf (from Geofabrik) into a Postgres database for some time. After reviewing the wiki detailed usage page thoroughly, I set the database to include all necessary tables (pgSnapshot) via the included sql scripts. I also made sure that osmosis was functioning as intended by running a smaller file (Antarctica) through, and I got the results I expected. However, when I attempt to do the same process with the north america file, I get an error that is dissimilar to others that have been reported on the web. I am trying to get this data onto a server, uploads to my local seem to be fine.</p>
<p>Here's my code (via command prompt) :</p>
<pre><code>C:\Users\eddie\Desktop&gt;osmosis --read-pbf-fast north-america-latest.osm.pbf --log-progress interval=3000 --write-pgsql nodeLocationStoreType=&quot;TempFile&quot; host=1*.8*.*.*0* database=osm postgresSchema=osm_updates user=eddie password=***</code></pre>
<p>This is the error I recieve:</p>
<pre><code>SEVERE: Thread for task 1-read-pbf-fast failed
org.springframework.dao.EmptyResultDataAccessException: Incorrect result 
size: expected 1, actual 0
at org.springframework.dao.support.DataAccessUtils.requiredSingleResult(DataAccessUtils.java:71)
at org.springframework.jdbc.core.JdbcTemplate.queryForObject(JdbcTemplate.java:495)
at org.springframework.jdbc.core.JdbcTemplate.queryForObject(JdbcTemplate.java:500)
at org.openstreetmap.osmosis.pgsnapshot.common.SchemaVersionValidator.validateDBVersion(SchemaVersionValidator.java:64)
at org.openstreetmap.osmosis.pgsnapshot.common.SchemaVersionValidator.validateVersion(SchemaVersionValidator.java:47)
at org.openstreetmap.osmosis.pgsnapshot.v0_6.impl.CopyFilesetLoader.run(CopyFilesetLoader.java:77)
at org.openstreetmap.osmosis.pgsnapshot.v0_6.PostgreSqlCopyWriter.complete(PostgreSqlCopyWriter.java:117)
at org.openstreetmap.osmosis.core.progress.v0_6.EntityProgressLogger.complete(EntityProgressLogger.java:82)
at org.openstreetmap.osmosis.pbf2.v0_6.PbfReader.run(PbfReader.java:96)
at java.lang.Thread.run(Unknown Source)
&#10;Jul 19, 2018 8:28:24 AM org.openstreetmap.osmosis.core.Osmosis main 
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
at java.lang.reflect.Method.invoke(Unknown Source)
at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330)
at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415)
at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356)
at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
<p>I am running osmosis .46, Postgres/PostGis 10/2.4 on Windows 10 with 12GB of RAM and 2 Intel 2.4GHz processors.</p>
<p>UPDATE: the error now occurs even when I run smaller files. Additionally, osmosis behaves as if it is processing a larger file (reaches node 4614331685 for Antarctica) as seen through the progress logger messages. Any help would be greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '18, 22:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0a1767df93ea1e4b0ee7d17b40f8645f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="egarnica&#39;s gravatar image" />
<p><span>egarnica</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="egarnica has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jul '18, 08:10</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-64808" class="comments-container">
&#10;</div>
<div id="comment-tools-64808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64808-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

