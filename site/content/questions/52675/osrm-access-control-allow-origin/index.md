+++
type = "question"
title = "OSRM Access-Control-Allow-Origin"
description = '''Hello, I have been playing around with an instance OSRM old api version 4.0 with an instance of the open street map website.  I have setup OSRM with a small extract and it serves perfectly fine returning directions if requested through the browser. When I try to send the request through my open stre...'''
date = "2016-10-25T13:45:00Z"
lastmod = "2016-10-25T16:07:00Z"
weight = 52675
keywords = [ "access", "osrm", "control", "routing" ]
aliases = [ "/questions/52675" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSRM Access-Control-Allow-Origin](/questions/52675/osrm-access-control-allow-origin)

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
<span id="post-52675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52675-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have been playing around with an instance OSRM old api version 4.0 with an instance of the open street map website.</p>
<p>I have setup OSRM with a small extract and it serves perfectly fine returning directions if requested through the browser.</p>
<p>When I try to send the request through my open street map website I get a 200 ok with the following error (In firefox and chrome):</p>
<p>XMLHttpRequest cannot load <a href="http://osrmURL/viaroute?z=14&amp;output=json&amp;instructions=true&amp;loc=39.0704%2C-76.5452&amp;loc=38.9786%2C-76.4928.">http://osrmURL/viaroute?z=14&amp;output=json&amp;instructions=true&amp;loc=39.0704%2C-76.5452&amp;loc=38.9786%2C-76.4928.</a> No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://osmwebsiteURL' is therefore not allowed access.</p>
<p>I must be missing something, but can't seem to find the issue.</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-control" rel="tag" title="see questions tagged &#39;control&#39;">control</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '16, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/943c484e8c04680902357de8f080dcc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cellington&#39;s gravatar image" />
<p><span>Cellington</span><br />
<span class="score" title="216 reputation points">216</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cellington has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52675" class="comments-container">
&#10;</div>
<div id="comment-tools-52675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52675-form-container" class="comment-form-container">
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

<span id="52683"></span>

<div id="answer-container-52683" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52683-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I upgraded to osrm version 4.6 (with CORS support) and now everything works great.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '16, 16:07</strong></p>
<img src="https://secure.gravatar.com/avatar/943c484e8c04680902357de8f080dcc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cellington&#39;s gravatar image" />
<p><span>Cellington</span><br />
<span class="score" title="216 reputation points">216</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cellington has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52683" class="comments-container">
&#10;</div>
<div id="comment-tools-52683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52683-form-container" class="comment-form-container">
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

