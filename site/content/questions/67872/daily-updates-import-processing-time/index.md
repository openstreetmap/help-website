+++
type = "question"
title = "Daily updates import processing time"
description = '''Hi,  I&#x27;m trying to figure out how often to have Osmosis update the whole planet on an OSM server I&#x27;m provisioning. Does anyone have typical import times for importing a daily updates in 1 hour chunks and 1 day chunks on their server? I will probably be able to allocate a good amount of memory (~16GB...'''
date = "2019-02-05T00:34:00Z"
lastmod = "2019-02-06T00:19:00Z"
weight = 67872
keywords = [ "osm2pgsql", "osmosis" ]
aliases = [ "/questions/67872" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Daily updates import processing time](/questions/67872/daily-updates-import-processing-time)

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
<span id="post-67872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67872-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to figure out how often to have Osmosis update the whole planet on an OSM server I'm provisioning. Does anyone have typical import times for importing a daily updates in 1 hour chunks and 1 day chunks on their server? I will probably be able to allocate a good amount of memory (~16GB) and processors (~6-8 CPUs) on my server. Thanks in advance for any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '19, 00:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7594614ba848fdde8ac9feb3d91253f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coderunner&#39;s gravatar image" />
<p><span>coderunner</span><br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coderunner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67872" class="comments-container">
&#10;</div>
<div id="comment-tools-67872" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67872-form-container" class="comment-form-container">
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

<span id="67875"></span>

<div id="answer-container-67875" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67875-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="coderunner has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This heavily depends on your disks. With non-SSD disks, or with disks mounted over network, applying an hourly update can take longer than one hour. With good SSD/NVMe disks you should be able to process an hourly diff in about 15 minutes and a daily diff in about 3-4 hours. Of course this is not constant; there can be exceptionally busy days or hours where your update takes longer, and also if your server does a lot of rendering in parallel things will be slowed down. Having 64 GB of RAM would likely bring these import times down to under 10 minutes for an hourly and 2-3 hours for a daily diff. CPU cores are less important, having just four would likely not make a difference. YMMV.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '19, 08:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-67875" class="comments-container">
<span id="67897"></span>
<div id="comment-67897" class="comment">
<div id="post-67897-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a> thanks for the answer. That helps a lot. I am running on SSD/NVMe disks. Sounds like hourly is a better fit for my use case because I would prefer the server's rendering performance not be impacted for too long a duration. It sounds like rendering can be done in parallel with updating and Postgresql will prevent things from being corrupted?</p>
</div>
<div id="comment-67897-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 21:13)</span> <span class="comment-user userinfo">coderunner</span>
</div>
</div>
<span id="67899"></span>
<div id="comment-67899" class="comment">
<div id="post-67899-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, sure, rendering and updating can run in parallel. Rendering is read-only anyway, and transaction isolation on the database will ensure that you're only seeing one thing or the other and not some halfway thing.</p>
</div>
<div id="comment-67899-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 23:59)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="67900"></span>
<div id="comment-67900" class="comment">
<div id="post-67900-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, thanks for your help!</p>
</div>
<div id="comment-67900-info" class="comment-info">
<span class="comment-age">(06 Feb '19, 00:19)</span> <span class="comment-user userinfo">coderunner</span>
</div>
</div>
</div>
<div id="comment-tools-67875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67875-form-container" class="comment-form-container">
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

