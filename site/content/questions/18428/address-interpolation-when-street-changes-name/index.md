+++
type = "question"
title = "Address interpolation when street changes name"
description = '''I draw address interpolation ways by making two parallel ways extending through the whole length of the street (not one way per block). I also put addr:street on each address node, rather than the interpolation way. If a street changes name, and thus it&#x27;s split into two ways with different name= tag...'''
date = "2012-12-13T20:05:00Z"
lastmod = "2012-12-14T00:34:00Z"
weight = 18428
keywords = [ "name-change", "interpolation", "splitting", "address" ]
aliases = [ "/questions/18428" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Address interpolation when street changes name](/questions/18428/address-interpolation-when-street-changes-name)

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
<span id="post-18428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18428-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I draw address interpolation ways by making two parallel ways extending through the whole length of the street (not one way per block). I also put <code>addr:street</code> on each address node, rather than the interpolation way.</p>
<p>If a street changes name, and thus it's split into two ways with different <code>name=</code> tags, should I split the interpolation way at this point too? The housenumbers continue along the street as if nothing had happened, it's only the name that changes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-name-change" rel="tag" title="see questions tagged &#39;name-change&#39;">name-change</span> <span class="post-tag tag-link-interpolation" rel="tag" title="see questions tagged &#39;interpolation&#39;">interpolation</span> <span class="post-tag tag-link-splitting" rel="tag" title="see questions tagged &#39;splitting&#39;">splitting</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '12, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/15962db3bafebdaa725a4c5709ccd932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nicolas17&#39;s gravatar image" />
<p><span>nicolas17</span><br />
<span class="score" title="86 reputation points">86</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nicolas17 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18428" class="comments-container">
&#10;</div>
<div id="comment-tools-18428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18428-form-container" class="comment-form-container">
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

<span id="18434"></span>

<div id="answer-container-18434" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18434-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nicolas17 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The best data is data that has all housenumbers in it, so no interpolation. Of course, this isn't always feasible, and the interpolation method gives good data with less work.</p>
<p>But, the smaller you can get those interpolation ways, the better. I would certainly split it when it's changing street names, and I would even try to split it per block (if you have that data).</p>
<p>When a street changes names, but you keep the same interpolation way, I don't know how existing software is going to handle this, so for compatibility reasons, it would be best to split in different parts.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '12, 23:25</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-18434" class="comments-container">
<span id="18436"></span>
<div id="comment-18436" class="comment">
<div id="post-18436-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>atm I don't even have accurate-enough information in the interpolation. For example I know that a block goes from 100 to 200, but I haven't collected the exact number of the house on the corner. If I split per block I end up with four nodes with the same number (see around node 295097394).</p>
</div>
<div id="comment-18436-info" class="comment-info">
<span class="comment-age">(14 Dec '12, 00:34)</span> <span class="comment-user userinfo">nicolas17</span>
</div>
</div>
</div>
<div id="comment-tools-18434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18434-form-container" class="comment-form-container">
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

