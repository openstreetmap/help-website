+++
type = "question"
title = "Extract Individual Trajectories from GPS trace"
description = '''Hi How can I extract GPS traces from Open Street Map as individual trajectories of a particular area (Bounding Box). Right now when I get the gpx (GPS trace file) file of a particular area selected by Bounding Box I get a set of points, but they are not organised based on which points belong to whic...'''
date = "2018-08-01T13:24:00Z"
lastmod = "2018-08-01T16:04:00Z"
weight = 65059
keywords = [ "trajectory", "traces", "gps" ]
aliases = [ "/questions/65059" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract Individual Trajectories from GPS trace](/questions/65059/extract-individual-trajectories-from-gps-trace)

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
<span id="post-65059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65059-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>How can I extract GPS traces from Open Street Map as individual trajectories of a particular area (Bounding Box). Right now when I get the gpx (GPS trace file) file of a particular area selected by Bounding Box I get a set of points, but they are not organised based on which points belong to which particular trajectory. The reason I am doing this is to collect all the complete trajectories and not some set of GPS points of a particular area.</p>
<p>Please feel free comment if the question is not clear.....</p>
<p>Thanks in advance.....</p>
<p>Best Regards, Saptarshi</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-trajectory" rel="tag" title="see questions tagged &#39;trajectory&#39;">trajectory</span> <span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '18, 13:24</strong></p>
<img src="https://secure.gravatar.com/avatar/1383bbb9acf6eac817efcef854388a5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saptarshi%20Mukherjee&#39;s gravatar image" />
<p><span>Saptarshi Mu...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saptarshi Mukherjee has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65059" class="comments-container">
&#10;</div>
<div id="comment-tools-65059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65059-form-container" class="comment-form-container">
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

<span id="65060"></span>

<div id="answer-container-65060" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65060-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a feature not a bug.</p>
<p>Traces can be uploaded to OSM with various degrees of privacy. The raw trace download is of a point cloud of all traces within a given area. Public traces which are the ones which will enable you to view the trajectory are associated with individuals have unique identifiers (<a href="https://www.openstreetmap.org/user/SK53/traces/2716880">this</a> is a recent one of mine).</p>
<p>I don't believe that there is an <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#GPS_traces">API call</a> which allows downloading all such traces in an area. Rather traces can be retrieved by id or by user, or by keyword for a given user.</p>
<p>These limitations are at least partly influenced by the need to offer a basic level of privacy protection to people submitting traces, whilst making them useful for mapping.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '18, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-65060" class="comments-container">
&#10;</div>
<div id="comment-tools-65060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65060-form-container" class="comment-form-container">
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

