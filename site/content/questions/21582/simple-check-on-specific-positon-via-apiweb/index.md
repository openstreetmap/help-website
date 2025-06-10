+++
type = "question"
title = "Simple check on specific positon via API/web"
description = '''Hi, I already know Nominatim which gives me address and some (much) more information for a specific location. That&#x27;s fine but way too much for what I plan to do (and it would cause way too much traffic on Nominatim comparing to what I really need). So my question: is there a possibility to find out ...'''
date = "2013-04-16T12:00:00Z"
lastmod = "2013-04-16T12:49:00Z"
weight = 21582
keywords = [ "landuse", "nominatim", "sea", "land" ]
aliases = [ "/questions/21582" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Simple check on specific positon via API/web](/questions/21582/simple-check-on-specific-positon-via-apiweb)

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
<span id="post-21582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21582-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I already know Nominatim which gives me address and some (much) more information for a specific location. That's fine but way too much for what I plan to do (and it would cause way too much traffic on Nominatim comparing to what I really need).</p>
<p>So my question: is there a possibility to find out if a given position is located in water or outside? Means can I do a simple check if that position specifies a place on land or sea?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-sea" rel="tag" title="see questions tagged &#39;sea&#39;">sea</span> <span class="post-tag tag-link-land" rel="tag" title="see questions tagged &#39;land&#39;">land</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '13, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/76ba5bd954a4f842d93c7eaba0b39227?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Satz%20Klauer&#39;s gravatar image" />
<p><span>Satz Klauer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Satz Klauer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21582" class="comments-container">
<span id="21583"></span>
<div id="comment-21583" class="comment">
<div id="post-21583-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to clarify, would the middle of a lake count as "land" or "sea"? What about an island in the middle of the lake?</p>
</div>
<div id="comment-21583-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 12:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="21584"></span>
<div id="comment-21584" class="comment">
<div id="post-21584-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>An island in the middle of a lake would be land.</p>
</div>
<div id="comment-21584-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 12:12)</span> <span class="comment-user userinfo">Satz Klauer</span>
</div>
</div>
</div>
<div id="comment-tools-21582" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21582-form-container" class="comment-form-container">
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

<span id="21588"></span>

<div id="answer-container-21588" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21588-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no ready-made API for this. You have to load the oceans and other water areas into a PostGIS database and write a few lines of glue script (PHP or similar) for that. Rivers could be a little complicated since they are often mapped as linear features; you will want to extend them to areas when populating your database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '13, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-21588" class="comments-container">
&#10;</div>
<div id="comment-tools-21588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21588-form-container" class="comment-form-container">
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

