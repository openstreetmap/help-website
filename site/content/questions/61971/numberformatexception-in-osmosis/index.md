+++
type = "question"
title = "NumberFormatException in Osmosis"
description = '''Hello I get java.lang.NumberFormatException: null when trying to read replication interval with Osmosis against geofabrik. My system is Ubuntu 17.10, Osmosis version 0.45 installed from apt, openjdk version &quot;1.8.0_151&quot;. In the working directory I have this files: $ cat ~/osm/planet/spain/configurati...'''
date = "2018-02-05T21:29:00Z"
lastmod = "2018-02-18T21:53:00Z"
weight = 61971
keywords = [ "osmosis" ]
aliases = [ "/questions/61971" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [NumberFormatException in Osmosis](/questions/61971/numberformatexception-in-osmosis)

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
<span id="post-61971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61971-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I get java.lang.NumberFormatException: null when trying to read replication interval with Osmosis against geofabrik. My system is Ubuntu 17.10, Osmosis version 0.45 installed from apt, openjdk version "1.8.0_151". In the working directory I have this files:</p>
<pre><code>$ cat ~/osm/planet/spain/configuration.txt 
baseUrl=http://download.geofabrik.de/europe/spain-updates
$ cat ~/osm/planet/spain/state.txt 
# original OSM minutely replication sequence number 2815550
timestamp=2018-01-26T21\:43\:02Z
sequenceNumber=1774</code></pre>
<p>The command I run is:</p>
<pre><code>$ osmosis --read-replication-interval workingDirectory=/home/javier/osm/planet/spain --simplify-change --write-xml-change -
feb 05, 2018 9:02:37 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMACIÓN: Osmosis Version 0.45
feb 05, 2018 9:02:38 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMACIÓN: Preparing pipeline.
feb 05, 2018 9:02:38 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMACIÓN: Launching pipeline execution.
feb 05, 2018 9:02:38 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMACIÓN: Pipeline executing, waiting for completion.
feb 05, 2018 9:02:38 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
GRAVE: Thread for task 1-read-replication-interval failed
java.lang.NumberFormatException: null
    at java.lang.Integer.parseInt(Integer.java:542)
    at java.lang.Integer.parseInt(Integer.java:615)
    at org.openstreetmap.osmosis.replication.v0_6.impl.ReplicationDownloaderConfiguration.getMaxInterval(ReplicationDownloaderConfiguration.java:66)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.calculateMaximumTimestamp(BaseReplicationDownloader.java:197)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.download(BaseReplicationDownloader.java:223)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.runImpl(BaseReplicationDownloader.java:304)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.run(BaseReplicationDownloader.java:383)
    at java.lang.Thread.run(Thread.java:748)
&#10;feb 05, 2018 9:02:38 PM org.openstreetmap.osmosis.core.Osmosis main
GRAVE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
    at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
    at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
    at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:498)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415)
    at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356)
    at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '18, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/c294cf339bcc2cf16329290040bded0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Javier%20Sanchez&#39;s gravatar image" />
<p><span>Javier Sanchez</span><br />
<span class="score" title="70 reputation points">70</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Javier Sanchez has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61971" class="comments-container">
&#10;</div>
<div id="comment-tools-61971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61971-form-container" class="comment-form-container">
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

<span id="62137"></span>

<div id="answer-container-62137" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62137-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>maxInterval is missing in configuration.txt, Try adding maxInterval=3600 after "baseUrl=<a href="http://download.geofabrik.de/europe/spain-updates">http://download.geofabrik.de/europe/spain-updates"</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '18, 07:34</strong></p>
<img src="https://secure.gravatar.com/avatar/2a0e874ad2031ad7af66abe17ee079c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ircama&#39;s gravatar image" />
<p><span>Ircama</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ircama has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62137" class="comments-container">
<span id="62188"></span>
<div id="comment-62188" class="comment">
<div id="post-62188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That is! Thank you very much.</p>
</div>
<div id="comment-62188-info" class="comment-info">
<span class="comment-age">(18 Feb '18, 21:53)</span> <span class="comment-user userinfo">Javier Sanchez</span>
</div>
</div>
</div>
<div id="comment-tools-62137" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62137-form-container" class="comment-form-container">
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

