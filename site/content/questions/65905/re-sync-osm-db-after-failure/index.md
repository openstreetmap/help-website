+++
type = "question"
title = "Re-sync OSM DB After Failure"
description = '''I extract highways from OSM every day from a cron job and keep a postgis database up-to-date. Due to a database change, the syncing has stopped in December 2017. I am trying to re-sync with a sequence number from earlier than December 03 2018 (when the syncing failed), but, I get a org.openstreetmap...'''
date = "2018-09-14T21:16:00Z"
lastmod = "2018-11-07T19:15:00Z"
weight = 65905
keywords = [ "postgresql", "osm", "postgis", "osmosis" ]
aliases = [ "/questions/65905" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Re-sync OSM DB After Failure](/questions/65905/re-sync-osm-db-after-failure)

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
<span id="post-65905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65905-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I extract highways from OSM every day from a cron job and keep a postgis database up-to-date. Due to a database change, the syncing has stopped in December 2017. I am trying to re-sync with a sequence number from earlier than December 03 2018 (when the syncing failed), but, I get a</p>
<pre><code>org.openstreetmap.osmosis.core.OsmosisRuntimeException: The replication state doesn&#39;t contain a timestamp property.</code></pre>
<p>Error. How can I rectify the issue and make the database current? Below is the failure:</p>
<pre><code>-------------------Fri Sep 14 14:18:42 EDT 2018----------------------
&#10;Sep 14, 2018 2:18:42 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.45
Sep 14, 2018 2:18:42 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Sep 14, 2018 2:18:42 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Sep 14, 2018 2:18:42 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
Sep 14, 2018 2:18:43 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-replication-interval failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: The replication state doesn&#39;t contain a timestamp property.
    at org.openstreetmap.osmosis.replication.common.ReplicationState.loadProperty(ReplicationState.java:65)
    at org.openstreetmap.osmosis.replication.common.ReplicationState.load(ReplicationState.java:78)
    at org.openstreetmap.osmosis.replication.common.ReplicationState.&lt;init&gt;(ReplicationState.java:59)
    at org.openstreetmap.osmosis.replication.common.ServerStateReader.getServerState(ServerStateReader.java:108)
    at org.openstreetmap.osmosis.replication.common.ServerStateReader.getServerState(ServerStateReader.java:50)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.runImpl(BaseReplicationDownloader.java:290)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.run(BaseReplicationDownloader.java:383)
    at java.lang.Thread.run(Unknown Source)
&#10;Sep 14, 2018 2:18:43 PM org.openstreetmap.osmosis.core.Osmosis main
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
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '18, 21:16</strong></p>
<img src="https://secure.gravatar.com/avatar/3fa98831cef96f8b9fb7530160338da7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="picmate&#39;s gravatar image" />
<p><span>picmate</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="picmate has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-65905" class="comments-container">
<span id="65936"></span>
<div id="comment-65936" class="comment">
<div id="post-65936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/295991/re-sync-osm-db-after-failure">https://gis.stackexchange.com/questions/295991/re-sync-osm-db-after-failure</a></p>
</div>
<div id="comment-65936-info" class="comment-info">
<span class="comment-age">(17 Sep '18, 12:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65905-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="66715"></span>

<div id="answer-container-66715" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66715-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The issue was directly due to not using the secured endpoint for fetching the diffs. I wrote an answer detailing the solution on stack overflow:</p>
<p><a href="https://gis.stackexchange.com/questions/295991/re-sync-osm-db-after-failure/301589#301589">https://gis.stackexchange.com/questions/295991/re-sync-osm-db-after-failure/301589#301589</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '18, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/3fa98831cef96f8b9fb7530160338da7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="picmate&#39;s gravatar image" />
<p><span>picmate</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="picmate has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '18, 18:48</strong> </span></p>
</div>
</div>
<div id="comments-container-66715" class="comments-container">
<span id="66716"></span>
<div id="comment-66716" class="comment">
<div id="post-66716-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've accepted this as the answe; hope you don't mind.</p>
</div>
<div id="comment-66716-info" class="comment-info">
<span class="comment-age">(07 Nov '18, 19:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="66717"></span>
<div id="comment-66717" class="comment">
<div id="post-66717-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't, thanks for doing that. Considering what I went through to get it resolved, would be helpful for someone else if run into a similar issue.</p>
</div>
<div id="comment-66717-info" class="comment-info">
<span class="comment-age">(07 Nov '18, 19:15)</span> <span class="comment-user userinfo">picmate</span>
</div>
</div>
</div>
<div id="comment-tools-66715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66715-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65913"></span>

<div id="answer-container-65913" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65913-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would assume the error message to be correct, so "replication state doesn't contain a timestamp property." id likely your problem.</p>
<pre><code>#Sun Sep 16 09:25:02 CEST 2018
sequenceNumber=3149567
timestamp=2018-09-16T07\:24\:02Z</code></pre>
<p>is an example of what the state file should look like and your file probably doesn't.</p>
<p>The values from <a href="https://planet.openstreetmap.org/replication/minute/002/732/999.state.txt">https://planet.openstreetmap.org/replication/minute/002/732/999.state.txt</a> should restart replication from the end of Novemeber 2017.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '18, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '18, 08:43</strong> </span></p>
</div>
</div>
<div id="comments-container-65913" class="comments-container">
<span id="65920"></span>
<div id="comment-65920" class="comment">
<div id="post-65920-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, thanks for the reply. I tried that. But, still get the same message. Is this related to a problem with the security certificate and the diff url? I still use an http url opposed to https. Just read something indicating that the https version should be used now.</p>
</div>
<div id="comment-65920-info" class="comment-info">
<span class="comment-age">(16 Sep '18, 17:13)</span> <span class="comment-user userinfo">picmate</span>
</div>
</div>
<span id="65921"></span>
<div id="comment-65921" class="comment">
<div id="post-65921-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You do need to use https in your osmosis configuration file, however a failure to do so, shouldn't result in the error message you are seeing.</p>
</div>
<div id="comment-65921-info" class="comment-info">
<span class="comment-age">(16 Sep '18, 17:41)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65913" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65913-form-container" class="comment-form-container">
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

