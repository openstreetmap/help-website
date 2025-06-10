+++
type = "question"
title = "osmosis failing"
description = '''Please suggest why process is failing Sep 07, 2020 3:41:10 AM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.47.4 Sep 07, 2020 3:41:11 AM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. Sep 07, 2020 3:41:11 AM org.openstreetmap.osmosis.core.Osmosis run INFO: ...'''
date = "2020-09-07T13:06:00Z"
lastmod = "2020-09-11T09:09:00Z"
weight = 76484
keywords = [ "osmosis" ]
aliases = [ "/questions/76484" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmosis failing](/questions/76484/osmosis-failing)

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
<span id="post-76484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76484-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Please suggest why process is failing</p>
<p>Sep 07, 2020 3:41:10 AM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.47.4 Sep 07, 2020 3:41:11 AM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. Sep 07, 2020 3:41:11 AM org.openstreetmap.osmosis.core.Osmosis run INFO: Launching pipeline execution. Sep 07, 2020 3:41:11 AM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline executing, waiting for completion. Sep 07, 2020 4:23:43 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion SEVERE: Thread for task 1-read-replication-interval failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to read the changeset file 004/182/814.osc.gz from the server. at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.downloadReplicationFile(BaseReplicationDownloader.java:119) at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.download(BaseReplicationDownloader.java:232) at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.runImpl(BaseReplicationDownloader.java:271) at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.run(BaseReplicationDownloader.java:350) at java.lang.Thread.run(Thread.java:748) Caused by: java.net.SocketTimeoutException: Read timed out at java.net.SocketInputStream.socketRead0(Native Method) at java.net.SocketInputStream.socketRead(SocketInputStream.java:116) at java.net.SocketInputStream.read(SocketInputStream.java:171) at java.net.SocketInputStream.read(SocketInputStream.java:141) at sun.security.ssl.InputRecord.readFully(InputRecord.java:465) at sun.security.ssl.InputRecord.read(InputRecord.java:503) at sun.security.ssl.SSLSocketImpl.readRecord(SSLSocketImpl.java:975) at sun.security.ssl.SSLSocketImpl.performInitialHandshake(SSLSocketImpl.java:1367) at sun.security.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:1395) at sun.security.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:1379) at sun.net.www.protocol.https.HttpsClient.afterConnect(HttpsClient.java:559) at sun.net.www.protocol.https.AbstractDelegateHttpsURLConnection.connect(AbstractDelegateHttpsURLConnection.java:185) at sun.net.www.protocol.http.HttpURLConnection.getInputStream0(HttpURLConnection.java:1564) at sun.net.www.protocol.http.HttpURLConnection.getInputStream(HttpURLConnection.java:1492) at sun.net.www.protocol.https.HttpsURLConnectionImpl.getInputStream(HttpsURLConnectionImpl.java:263) at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.downloadReplicationFile(BaseReplicationDownloader.java:102) ... 4 more</p>
<p>Sep 07, 2020 4:23:43 AM org.openstreetmap.osmosis.core.Osmosis main SEVERE: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed. at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146) at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92) at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37) at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) at java.lang.reflect.Method.invoke(Method.java:498) at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330) at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238) at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415) at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356) at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '20, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/df8704d2a10bf36fc9c5b79301fbd118?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustusj&#39;s gravatar image" />
<p><span>augustusj</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustusj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '20, 13:09</strong> </span></p>
</div>
</div>
<div id="comments-container-76484" class="comments-container">
<span id="76485"></span>
<div id="comment-76485" class="comment">
<div id="post-76485-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Without any useful information about how you have set replication up, any answers here will be guesswork (like "is it using https").</p>
<p>Please explain exactly what have you done to get to this point. What set of instructions were you following?</p>
</div>
<div id="comment-76485-info" class="comment-info">
<span class="comment-age">(07 Sep '20, 13:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="76486"></span>
<div id="comment-76486" class="comment">
<div id="post-76486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>we already have this Tile server running since more than a year but today the daily update suddenly failed ... let me get more details</p>
</div>
<div id="comment-76486-info" class="comment-info">
<span class="comment-age">(07 Sep '20, 13:21)</span> <span class="comment-user userinfo">augustusj</span>
</div>
</div>
<span id="76488"></span>
<div id="comment-76488" class="comment">
<div id="post-76488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For info, I'm running osmosis for updates (based on OSM minutely diffs every 5 minutes), haven't changed anything locally and have not seen any problems recently.</p>
</div>
<div id="comment-76488-info" class="comment-info">
<span class="comment-age">(07 Sep '20, 14:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-76484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76484-form-container" class="comment-form-container">
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

<span id="76513"></span>

<div id="answer-container-76513" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76513-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>seems like it was an intermittent issue because today it starting working as usual.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '20, 13:14</strong></p>
<img src="https://secure.gravatar.com/avatar/df8704d2a10bf36fc9c5b79301fbd118?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustusj&#39;s gravatar image" />
<p><span>augustusj</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustusj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76513" class="comments-container">
<span id="76554"></span>
<div id="comment-76554" class="comment">
<div id="post-76554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you look through the stack trace you will see that the issue was simply the network connection timing out, with other words the issue was due to a network issue.</p>
</div>
<div id="comment-76554-info" class="comment-info">
<span class="comment-age">(11 Sep '20, 09:09)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-76513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76513-form-container" class="comment-form-container">
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

