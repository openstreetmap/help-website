+++
type = "question"
title = "Nominatim: nodes displayed on tiles"
description = '''Can you advice, how can I filter ONLY nodes which are displayed on map tiles from nominatim/details response - hierarchy section?'''
date = "2019-10-23T11:54:00Z"
lastmod = "2019-10-23T12:31:00Z"
weight = 71270
keywords = [ "hierarchy", "nominatim" ]
aliases = [ "/questions/71270" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim: nodes displayed on tiles](/questions/71270/nominatim-nodes-displayed-on-tiles)

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
<span id="post-71270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71270-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can you advice, how can I filter ONLY nodes which are displayed on map tiles from nominatim/details response - hierarchy section?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '19, 11:54</strong></p>
<img src="https://secure.gravatar.com/avatar/199acbf6ccda81e10cb3379a8f89f5b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="atom-systems&#39;s gravatar image" />
<p><span>atom-systems</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="atom-systems has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71270" class="comments-container">
&#10;</div>
<div id="comment-tools-71270" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71270-form-container" class="comment-form-container">
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

<span id="71271"></span>

<div id="answer-container-71271" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71271-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="atom-systems has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not possible, because Nominatim does not know anything about the map tiles. Whether something is shown on the map or not can be influenced by many factors, even for example how many other labels there are nearby. These are decisions made when rendering the tile (and decisions that each map style could make differently) so there's no way to do this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '19, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71271" class="comments-container">
<span id="71273"></span>
<div id="comment-71273" class="comment">
<div id="post-71273-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik for your answer. Can you advice alternative way how to get these nodes?</p>
</div>
<div id="comment-71273-info" class="comment-info">
<span class="comment-age">(23 Oct '19, 12:31)</span> <span class="comment-user userinfo">atom-systems</span>
</div>
</div>
</div>
<div id="comment-tools-71271" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71271-form-container" class="comment-form-container">
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

