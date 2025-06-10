+++
type = "question"
title = "How to map closed bank branch that still offers ATM service?"
description = '''I have a former bank branch office in the area that was closed down but still offers ATM and other self service activities like account statement printing and a post box from the same place. Should this be changed from amenity=bank to amenity=atm or should the state better be represented as amenity=...'''
date = "2021-09-24T14:52:00Z"
lastmod = "2021-09-24T18:07:00Z"
weight = 81933
keywords = [ "atm", "bank" ]
aliases = [ "/questions/81933" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to map closed bank branch that still offers ATM service?](/questions/81933/how-to-map-closed-bank-branch-that-still-offers-atm-service)

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
<span id="post-81933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81933-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a former bank branch office in the area that was closed down but still offers ATM and other self service activities like account statement printing and a post box from the same place. Should this be changed from amenity=bank to amenity=atm or should the state better be represented as amenity=bank with opening hours of 24/7 closed - which might confuse people regarding the status of the ATM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-atm" rel="tag" title="see questions tagged &#39;atm&#39;">atm</span> <span class="post-tag tag-link-bank" rel="tag" title="see questions tagged &#39;bank&#39;">bank</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '21, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/f2526e8e6ebcf38aefa6460b8b3b58c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ReinerB&#39;s gravatar image" />
<p><span>ReinerB</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ReinerB has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81933" class="comments-container">
&#10;</div>
<div id="comment-tools-81933" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81933-form-container" class="comment-form-container">
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

<span id="81939"></span>

<div id="answer-container-81939" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81939-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ReinerB has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would recommend against keeping it as <code>amenity=bank</code> and setting it to always closed. If a data consumer doesn't utilize the opening_hours tag (the main OSM map rendering is one example), this tagging would make it look like an active bank.</p>
<p>IMO, you should change the bank to closed:amenity=bank, so other mappers can see the status and won't inadvertently re-map the bank as being open. You can then add new nodes for the <code>amenity=atm</code> and <code>amenity=post_box</code>. Maybe also add a note to the ATM for the benefit of other mappers explaining that the ATM is still operational, even though the bank isn't.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '21, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-81939" class="comments-container">
<span id="81940"></span>
<div id="comment-81940" class="comment">
<div id="post-81940-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I take it by post box you mean a place for delivering letters intended for the bank, not a post box offering a generic postal collection. Please don't use amenity=post_box for such things. I think letter_box is sometimes used for delivery points.</p>
</div>
<div id="comment-81940-info" class="comment-info">
<span class="comment-age">(24 Sep '21, 18:07)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81939" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81939-form-container" class="comment-form-container">
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

