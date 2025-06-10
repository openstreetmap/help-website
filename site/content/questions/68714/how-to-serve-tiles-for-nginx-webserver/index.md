+++
type = "question"
title = "How to serve tiles for Nginx webserver?"
description = '''Dear OSM community,  Can mod_tile be configured with Nginx webserver? Is there any module for Nginx which does the same as mod_tile to Apache?   I have an application in Flask which is using Nginx and it needs to display maps. As OSM uses Apache2, how can I run the both servers? or Is there a better...'''
date = "2019-04-08T19:06:00Z"
lastmod = "2019-04-08T19:46:00Z"
weight = 68714
keywords = [ "nginx", "tiles", "rendering", "tile_server" ]
aliases = [ "/questions/68714" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to serve tiles for Nginx webserver?](/questions/68714/how-to-serve-tiles-for-nginx-webserver)

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
<span id="post-68714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68714-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear OSM community,</p>
<ol>
<li>Can mod_tile be configured with Nginx webserver?</li>
<li>Is there any module for Nginx which does the same as mod_tile to Apache?</li>
</ol>
<p>I have an application in Flask which is using Nginx and it needs to display maps. As OSM uses Apache2, how can I run the both servers? or Is there a better solution?</p>
<p>Thank you in advance :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nginx" rel="tag" title="see questions tagged &#39;nginx&#39;">nginx</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tile_server" rel="tag" title="see questions tagged &#39;tile_server&#39;">tile_server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '19, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/3a80bf37e74eeaaa27a8c472b6144a06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="komms&#39;s gravatar image" />
<p><span>komms</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="komms has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68714" class="comments-container">
&#10;</div>
<div id="comment-tools-68714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68714-form-container" class="comment-form-container">
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

<span id="68715"></span>

<div id="answer-container-68715" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68715-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-68715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To my knowledge there's nothing like mod_tile for nginx, but you could trivially run Apache on a different port, say port 81, and then configure your nginx to pass through (proxy) certain requests it receives to Apache.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '19, 19:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68715" class="comments-container">
<span id="68716"></span>
<div id="comment-68716" class="comment">
<div id="post-68716-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>will try and update here.</p>
</div>
<div id="comment-68716-info" class="comment-info">
<span class="comment-age">(08 Apr '19, 19:46)</span> <span class="comment-user userinfo">komms</span>
</div>
</div>
</div>
<div id="comment-tools-68715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68715-form-container" class="comment-form-container">
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

