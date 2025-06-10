+++
type = "question"
title = "Reset Osmosis update process after failure following server shutdown"
description = '''I have a tile server set up, and was using osmosis to update the database. However, the process stopped working, and when I analyzed the logs, it appears that when I shut down the server (in order to move to a new timezone), the update process stopped working. Here is the relevant portion of the log...'''
date = "2018-07-22T03:48:00Z"
lastmod = "2018-07-22T12:54:00Z"
weight = 64848
keywords = [ "timestamps", "osmosis", "expiry" ]
aliases = [ "/questions/64848" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Reset Osmosis update process after failure following server shutdown](/questions/64848/reset-osmosis-update-process-after-failure-following-server-shutdown)

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
<span id="post-64848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64848-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a tile server set up, and was using osmosis to update the database. However, the process stopped working, and when I analyzed the logs, it appears that when I shut down the server (in order to move to a new timezone), the update process stopped working.</p>
<p>Here is the relevant portion of the log file:</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screen_Shot_2018-07-21_at_20.04.45.png" alt="alt text" /></p>
<p>A current osmosis.log shows this:</p>
<pre><code>Jul 21, 2018 7:15:01 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.46 Jul 21, 2018 7:15:02 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. Jul 21, 2018 7:15:02 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Launching pipeline execution. Jul 21, 2018 7:15:02 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline executing, waiting for completion. Jul 21, 2018 7:15:03 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion SEVERE: Thread for task 1-read-replication-interval failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: The replication state doesn&#39;t contain a timestamp property.
    at org.openstreetmap.osmosis.replication.common.ReplicationState.loadProperty(ReplicationState.java:65)
    at org.openstreetmap.osmosis.replication.common.ReplicationState.load(ReplicationState.java:78)
    at org.openstreetmap.osmosis.replication.common.ReplicationState.&lt;init&gt;(ReplicationState.java:59)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.runImpl(BaseReplicationDownloader.java:268)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.run(BaseReplicationDownloader.java:350)
    at java.base/java.lang.Thread.run(Thread.java:844)
&#10;Jul 21, 2018 7:15:03 PM org.openstreetmap.osmosis.core.Osmosis main SEVERE: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.base/java.lang.reflect.Method.invoke(Method.java:564)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
<p>Admittedly, I had not changed the timezone on the server, so I'm not thinking it would have known I moved. Instead, I'm guessing something didn't shut down cleanly which is why osmosis.log shows a problem with the timestamp of the replication state. Assuming I'm correct, how can I reset osmosis expire stamp?</p>
<p>Can I simply run <code>openstreetmap-tiles-update-expire</code> with a timestamp of the last successful expiration? In this case: 2018-07-08T14:15:10Z?</p>
<p>In my searching, I've found some directions on how to get the current timestamp of a file, but not how to determine the current timestamp of the database. I apologize up front if I'm missing something easy or obvious.</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-expiry" rel="tag" title="see questions tagged &#39;expiry&#39;">expiry</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '18, 03:48</strong></p>
<img src="https://secure.gravatar.com/avatar/9d2fa479c7f7984fd8fd435b2badbc4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tim_rohrer&#39;s gravatar image" />
<p><span>tim_rohrer</span><br />
<span class="score" title="81 reputation points">81</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tim_rohrer has one accepted answer">100%</span></p>
</img>
</div>
</div>
<div id="comments-container-64848" class="comments-container">
&#10;</div>
<div id="comment-tools-64848" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64848-form-container" class="comment-form-container">
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

<span id="64853"></span>

<div id="answer-container-64853" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64853-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tim_rohrer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally, how to re-sync after failure:</p>
<p>First, find the highest node ID in your database. If you are not using flatnodes, then</p>
<pre><code>select max(id) from planet_osm_nodes;</code></pre>
<p>else</p>
<pre><code>select max(osm_id) from planet_osm_point;</code></pre>
<p>Then, find the replication status file ("state.txt") that contains this ID; you can either do this by guesswork based on the node's creation date, or use the whichdiff utility (<a href="https://svn.openstreetmap.org/applications/utils/whichdiff/)">https://svn.openstreetmap.org/applications/utils/whichdiff/)</a> which you invoke with the node ID you found.</p>
<p>Install the replication status file in the correct directory (same where your configuration.txt lives) and you should be ready to go.</p>
<p>Having said all that: Your screenshot says the last successfully applied diff was #3047966. The replication directory is organised by groups of thousands, so this number translates to 003/047/966, or <a href="https://planet.openstreetmap.org/replication/minute/003/047/966.state.txt">https://planet.openstreetmap.org/replication/minute/003/047/966.state.txt</a> - you could use the above procedure to double check, but it should lead you to approximately the same file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '18, 10:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jul '18, 10:06</strong> </span></p>
</div>
</div>
<div id="comments-container-64853" class="comments-container">
<span id="64856"></span>
<div id="comment-64856" class="comment">
<div id="post-64856-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik. This makes sense because I want the time stamp of the latest diff applied, not the time stamp of the latest time osmosis CHECKED to see if an update was necessary.</p>
<p>To confirm, I then will run <code>openstreetmap-tiles-update-expire</code> with the timestamp of that last diff successfully applied, after deleting the .osmosis file?</p>
</div>
<div id="comment-64856-info" class="comment-info">
<span class="comment-age">(22 Jul '18, 12:54)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
</div>
<div id="comment-tools-64853" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64853-form-container" class="comment-form-container">
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

