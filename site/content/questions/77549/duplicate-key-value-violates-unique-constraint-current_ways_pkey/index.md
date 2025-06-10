+++
type = "question"
title = "duplicate key value violates unique constraint &quot;current_ways_pkey&quot;"
description = '''Hi im getting this error when i try to insert my osm data into my postgres database. SEVERE: Thread for task 1-read-xml failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to load current ways.  and ERROR: duplicate key value violates unique constraint &quot;current_ways_pkey&quot;  Detail: ...'''
date = "2020-11-14T20:09:00Z"
lastmod = "2020-11-16T10:37:00Z"
weight = 77549
keywords = [ "postgresql", "osmosis" ]
aliases = [ "/questions/77549" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [duplicate key value violates unique constraint "current_ways_pkey"](/questions/77549/duplicate-key-value-violates-unique-constraint-current_ways_pkey)

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
<span id="post-77549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77549-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi im getting this error when i try to insert my osm data into my postgres database.</p>
<pre><code>SEVERE: Thread for task 1-read-xml failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to load current ways.</code></pre>
<p>and</p>
<pre><code>ERROR: duplicate key value violates unique constraint &quot;current_ways_pkey&quot;
  Detail: Key (id)=(197) already exists.</code></pre>
<p>The command im using is:</p>
<pre><code>osmosis --read-xml file=&quot;/home/ubuntu/osmosis/bin/mergedeuroad.osm&quot; --write-apidb host=&quot;localhost&quot; database=&quot;openstreetmap&quot; user=&quot;xxx&quot; password=&quot;xxx&quot; validateSchemaVersion=&quot;no&quot;</code></pre>
<p>any solutions to solve this?</p>
<p>ERROR LOG:</p>
<pre><code>INFO: Pipeline executing, waiting for completion.
Nov 14, 2020 7:46:41 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-xml failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to load current ways.
        at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentWays(ApidbWriter.java:1035)
        at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentTables(ApidbWriter.java:1108)
        at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.complete(ApidbWriter.java:1141)
        at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:92)
        at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.postgresql.util.PSQLException: ERROR: duplicate key value violates unique constraint &quot;current_ways_pkey&quot;
  Detail: Key (id)=(197) already exists.
        at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2510)
        at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:2245)
        at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:311)
        at org.postgresql.jdbc.PgStatement.executeInternal(PgStatement.java:447)
        at org.postgresql.jdbc.PgStatement.execute(PgStatement.java:368)
        at org.postgresql.jdbc.PgPreparedStatement.executeWithFlags(PgPreparedStatement.java:159)
        at org.postgresql.jdbc.PgPreparedStatement.execute(PgPreparedStatement.java:148)
        at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentWays(ApidbWriter.java:1032)
        ... 4 more
&#10;Nov 14, 2020 7:46:41 PM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.base/java.lang.reflect.Method.invoke(Method.java:566)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:321)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:234)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:406)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:347)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '20, 20:09</strong></p>
<img src="https://secure.gravatar.com/avatar/87f23f2f0056b2d7d6ed1760463ea1c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shafi-as&#39;s gravatar image" />
<p><span>shafi-as</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shafi-as has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '20, 10:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-77549" class="comments-container">
<span id="77550"></span>
<div id="comment-77550" class="comment">
<div id="post-77550-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ol>
<li>Please explain how the file "mergedeuroad.osm" has been created, or upload it to a place where we can see.</li>
<li>Are you really, really sure that you want to create a database in the API DB format? Because if you just want to be able to run queries on the road network, osm2pgsql would be a much better choice for importing than osmosis.</li>
</ol>
</div>
<div id="comment-77550-info" class="comment-info">
<span class="comment-age">(14 Nov '20, 21:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="77551"></span>
<div id="comment-77551" class="comment">
<div id="post-77551-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>1) the merged osm was created, using osmfilter, it was originally a geofabrik Europe file. i filtered it to only to have highways, once filtered it was merged with a file containing rails and seaways for certain countries in Europe created on josm.</p>
<p>2) i chose APIDB as it was on the guide i was following to create a private osm server. im trying to view that road rail and seaway data on josm. will osm2pgql work the same for intupting data into josm? also im more familiar with the osmosis commands.</p>
</div>
<div id="comment-77551-info" class="comment-info">
<span class="comment-age">(14 Nov '20, 22:54)</span> <span class="comment-user userinfo">shafi-as</span>
</div>
</div>
<span id="77552"></span>
<div id="comment-77552" class="comment">
<div id="post-77552-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want to set up your own OSM server then APIDB is indeed what you need. If you have created new objects with OSM then these will likely have negative IDs and therefore cannot be loaded into an APIDB. If you have created the objects with JOSM by downloading data from OSM, you have likely created duplicates accidentally. Note that a way can have a highway and a railway tag at the same time: <a href="https://www.openstreetmap.org/way/281583600">https://www.openstreetmap.org/way/281583600</a></p>
</div>
<div id="comment-77552-info" class="comment-info">
<span class="comment-age">(15 Nov '20, 01:39)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="77558"></span>
<div id="comment-77558" class="comment">
<div id="post-77558-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ive loaded both files in separately before the merge in to the database successfully. but when they are emerged its when the duplicate key error im getting. so i think i can rule out the negative IDs being an issue. is there any osmosis command to filter out or view duplicates. or any ways to go around the duplicate error</p>
</div>
<div id="comment-77558-info" class="comment-info">
<span class="comment-age">(15 Nov '20, 15:38)</span> <span class="comment-user userinfo">shafi-as</span>
</div>
</div>
</div>
<div id="comment-tools-77549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77549-form-container" class="comment-form-container">
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

<span id="77568"></span>

<div id="answer-container-77568" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77568-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As fredrerik mentioned it may be that two tags such as railway and highway have the same ID, as one one my osm was custom made this was the case for me. To over come this, i opened the file on notepad++ and searched for the the duplicate id and gave it and unrealistic number that wouldn't be used again. this will work for ways. if it is a duplicate node node problem, once you change the node you then make sure you search for the references of that duplicate node and change them aswell. this is a wacky fix but it worked for me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '20, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/87f23f2f0056b2d7d6ed1760463ea1c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shafi-as&#39;s gravatar image" />
<p><span>shafi-as</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shafi-as has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77568" class="comments-container">
&#10;</div>
<div id="comment-tools-77568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77568-form-container" class="comment-form-container">
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

