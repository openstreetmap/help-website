+++
type = "question"
title = "Turn restriction fine points"
description = '''Take a look at relation 2732863. I added the turn restriction but do not completely understand how it works despite reading all the available help I could find. The restriction is only_right_turn when approaching the intersection from the south. The way forward (north) is blocked by a barrier and th...'''
date = "2013-01-31T16:32:00Z"
lastmod = "2013-02-01T06:37:00Z"
weight = 19497
keywords = [ "turn", "relations", "roles", "restriction" ]
aliases = [ "/questions/19497" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Turn restriction fine points](/questions/19497/turn-restriction-fine-points)

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
<span id="post-19497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19497-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Take a look at <a href="https://www.openstreetmap.org/browse/relation/2732863">relation 2732863</a>. I added the turn restriction but do not completely understand how it works despite reading all the available help I could find.</p>
<p>The restriction is only_right_turn when approaching the intersection from the south. The way forward (north) is blocked by a barrier and the road you're turning onto is one way going east to west. However, if coming from the north the restriction changes to only_right_turn. The same barrier is there to block southerly travel and the same east-west, one-way road forces the right turn.</p>
<p>Therefore the same intersection has two distinct turn restrictions depending on the direction of approach. But how does one specify that?</p>
<p>In the wiki I read about From: and To: members of a relation but can't figure out how to assign those roles to the ways in my turn restriction dialog in either Potlatch or JOSM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turn" rel="tag" title="see questions tagged &#39;turn&#39;">turn</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-roles" rel="tag" title="see questions tagged &#39;roles&#39;">roles</span> <span class="post-tag tag-link-restriction" rel="tag" title="see questions tagged &#39;restriction&#39;">restriction</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jan '13, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Feb '13, 09:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-19497" class="comments-container">
&#10;</div>
<div id="comment-tools-19497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19497-form-container" class="comment-form-container">
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

<span id="19498"></span>

<div id="answer-container-19498" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19498-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll have to split Tha Phae Road at the intersection node and create two separate turn restriction relations. The one for the south approach (only_left_turn) would have the southward road (Kamphaeng Din), the intersection node and the westward Tha Phae Road as relation members. Kamphaeng Din Road will have the "from" role, the intersection node the "via" role, and the westward road the "to" role.</p>
<p>Conversely, the north approach will have an only_right_turn relation, with Ratchawong Road having the "from" role. The intersection node and the westward Tha Phae Road will thus be members of both relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '13, 17:01</strong></p>
<img src="https://secure.gravatar.com/avatar/3e4de1232f3377cc783012d889d0375c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul_012&#39;s gravatar image" />
<p><span>Paul_012</span><br />
<span class="score" title="686 reputation points">686</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul_012 has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jan '13, 17:06</strong> </span></p>
</div>
</div>
<div id="comments-container-19498" class="comments-container">
<span id="19501"></span>
<div id="comment-19501" class="comment">
<div id="post-19501-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Or, looking at Bing, you could split the northern way to have oneway slip roads into and out of it, and the road from the south then won't join the way to the north and everything will be controlled by the oneway sections and not need any turn restriction relations.</p>
</div>
<div id="comment-19501-info" class="comment-info">
<span class="comment-age">(31 Jan '13, 17:55)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="19503"></span>
<div id="comment-19503" class="comment">
<div id="post-19503-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@EdLoach</span> - that sounds like a good and easy fix for this particular intersection. But I want to learn how to do this for the more general cases I'm likely to encounter in the future.</p>
<p><span>@Paul</span> - okay, fine. So how do I assign those roles? The Potlatch advanced Turn Restriction dialogs are confusing to say the least and JOSM isn't much better.</p>
<p>Thanks for your time.</p>
</div>
<div id="comment-19503-info" class="comment-info">
<span class="comment-age">(01 Feb '13, 01:16)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="19504"></span>
<div id="comment-19504" class="comment">
<div id="post-19504-score" class="comment-score">
3
</div>
<div class="comment-text">
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/JOSM_Relations_and_Turn_Based_Restrictions">Howto in Josm</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Potlatch_2/restrictions">Howto in Potlatch2</a></li>
</ul>
<p>If anything on those pages is not clear, please tell us what that is, so they can be improved.</p>
</div>
<div id="comment-19504-info" class="comment-info">
<span class="comment-age">(01 Feb '13, 06:37)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-19498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19498-form-container" class="comment-form-container">
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

