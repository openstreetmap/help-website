+++
type = "question"
title = "Entrance to a building through a tunnel"
description = '''Which is the best way to draw and tag an entrance which is not in the building wall but about 20 m away from the building leading underground to the basement floors. The way from the entrance to the building is a tunnel covered by earth and grass (not a grass covered roof) so it cannot be seen from ...'''
date = "2019-06-10T17:28:00Z"
lastmod = "2019-06-10T20:25:00Z"
weight = 69561
keywords = [ "tunnel", "slope", "entrance" ]
aliases = [ "/questions/69561" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Entrance to a building through a tunnel](/questions/69561/entrance-to-a-building-through-a-tunnel)

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
<span id="post-69561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69561-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Which is the best way to draw and tag an entrance which is not in the building wall but about 20 m away from the building leading underground to the basement floors. The way from the entrance to the building is a tunnel covered by earth and grass (not a grass covered roof) so it cannot be seen from above. I can imagine that my question is not unique but can appear where buildings are built on slopes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tunnel" rel="tag" title="see questions tagged &#39;tunnel&#39;">tunnel</span> <span class="post-tag tag-link-slope" rel="tag" title="see questions tagged &#39;slope&#39;">slope</span> <span class="post-tag tag-link-entrance" rel="tag" title="see questions tagged &#39;entrance&#39;">entrance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jun '19, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/5fbbaa507e58a4860ab2ce17e8ddee14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Archiver&#39;s gravatar image" />
<p><span>Archiver</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Archiver has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jun '19, 17:34</strong> </span></p>
</div>
</div>
<div id="comments-container-69561" class="comments-container">
&#10;</div>
<div id="comment-tools-69561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69561-form-container" class="comment-form-container">
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

<span id="69568"></span>

<div id="answer-container-69568" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69568-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can map the way in the tunnel:<br />
highway=path<br />
tunnel=yes<br />
layer=-1 (if anything else is crossing above)<br />
level=-1 (or whatever is appropriate for the rest of the building level the tunnel connects to)</p>
<p>And then connect the tunnel to the overground road network and put an entrance=main or =yes on the end point of the tunnel.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '19, 20:25</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jun '19, 16:23</strong> </span></p>
</div>
</div>
<div id="comments-container-69568" class="comments-container">
&#10;</div>
<div id="comment-tools-69568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69568-form-container" class="comment-form-container">
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

