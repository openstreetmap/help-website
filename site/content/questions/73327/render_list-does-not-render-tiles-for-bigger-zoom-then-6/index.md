+++
type = "question"
title = "render_list does not render tiles for bigger zoom then 6"
description = '''render_list --all -n 5 --min-zoom=0 --max-zoom=9 render_list -a -Z 16 -n 5 Both give me  Rendering client Starting 5 rendering threads Rendering all tiles from zoom 0 to zoom 16 Rendering all tiles for zoom 0 from (0, 0) to (0, 0) Rendering all tiles for zoom 1 from (0, 0) to (1, 1) Rendering all ti...'''
date = "2020-03-03T12:23:00Z"
lastmod = "2020-03-03T13:34:00Z"
weight = 73327
keywords = [ "render_list", "zoom", "render" ]
aliases = [ "/questions/73327" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [render_list does not render tiles for bigger zoom then 6](/questions/73327/render_list-does-not-render-tiles-for-bigger-zoom-then-6)

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
<span id="post-73327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73327-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>render_list --all -n 5 --min-zoom=0 --max-zoom=9 render_list -a -Z 16 -n 5 Both give me</p>
<pre><code>Rendering client
Starting 5 rendering threads
Rendering all tiles from zoom 0 to zoom 16
Rendering all tiles for zoom 0 from (0, 0) to (0, 0)
Rendering all tiles for zoom 1 from (0, 0) to (1, 1)
Rendering all tiles for zoom 2 from (0, 0) to (3, 3)
Rendering all tiles for zoom 3 from (0, 0) to (7, 7)
Rendering all tiles for zoom 4 from (0, 0) to (15, 15)
Rendering all tiles for zoom 5 from (0, 0) to (31, 31)
Rendering all tiles for zoom 6 from (0, 0) to (63, 63)</code></pre>
<p>and then it just stops. Left it for a couple of hours - nothing changed. CPU is loaded by 20% with x-org and gnome-shell. What might be the problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-render_list" rel="tag" title="see questions tagged &#39;render_list&#39;">render_list</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '20, 12:23</strong></p>
<img src="https://secure.gravatar.com/avatar/7d9dea8db6c9981b45d28f28bb29f49d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kartman1&#39;s gravatar image" />
<p><span>kartman1</span><br />
<span class="score" title="38 reputation points">38</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kartman1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73327" class="comments-container">
&#10;</div>
<div id="comment-tools-73327" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73327-form-container" class="comment-form-container">
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

<span id="73331"></span>

<div id="answer-container-73331" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73331-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found the answer here</p>
<pre><code>https://github.com/Overv/openstreetmap-tile-server/issues/17</code></pre>
<p>if anyone is interested. (needed -m ajt)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '20, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7d9dea8db6c9981b45d28f28bb29f49d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kartman1&#39;s gravatar image" />
<p><span>kartman1</span><br />
<span class="score" title="38 reputation points">38</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kartman1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73331" class="comments-container">
&#10;</div>
<div id="comment-tools-73331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73331-form-container" class="comment-form-container">
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

