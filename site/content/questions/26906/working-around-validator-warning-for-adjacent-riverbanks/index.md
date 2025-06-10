+++
type = "question"
title = "Working around validator warning for adjacent riverbanks"
description = '''I finally understood (I think !) the reason why some mappers add a node where a riverbank way ends and another begins:  This is, as far as I can figure out, a way to avoid JOSM validator&#x27;s &quot;ovelapping ways&quot; warning. Of course, the warning is yet another anoying false-positive, but to me it seems lik...'''
date = "2013-10-02T12:47:00Z"
lastmod = "2013-10-06T16:48:00Z"
weight = 26906
keywords = [ "river", "riverbank", "overlap", "validator" ]
aliases = [ "/questions/26906" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Working around validator warning for adjacent riverbanks](/questions/26906/working-around-validator-warning-for-adjacent-riverbanks)

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
<span id="post-26906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26906-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I finally understood (I think !) the reason why some mappers add a node where a riverbank way ends and another begins:</p>
<p><img src="http://help.openstreetmap.org/upfiles/riverbank_overlap.png" alt="alt text" /></p>
<p>This is, as far as I can figure out, a way to avoid JOSM validator's "ovelapping ways" warning.</p>
<p>Of course, the warning is yet another anoying false-positive, but to me it seems like the workaround is an actual semantic error (overlapping areas as opposed to areas sharing an edge). I should probably file a bug to the validator, but I wonder what people think. Is this workaround a good thing ? Wouldn't validators other than the JOSM one complain about this ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-riverbank" rel="tag" title="see questions tagged &#39;riverbank&#39;">riverbank</span> <span class="post-tag tag-link-overlap" rel="tag" title="see questions tagged &#39;overlap&#39;">overlap</span> <span class="post-tag tag-link-validator" rel="tag" title="see questions tagged &#39;validator&#39;">validator</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Oct '13, 12:47</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</img>
</div>
</div>
<div id="comments-container-26906" class="comments-container">
<span id="26907"></span>
<div id="comment-26907" class="comment">
<div id="post-26907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In a way, using a single multipolygon relation for the whole river fixes the issue cleanly, but that has even more annoying problems of its own. And it doesn't ultimately solve the issue of "touching riverbanks" once we reach a tributary.</p>
</div>
<div id="comment-26907-info" class="comment-info">
<span class="comment-age">(02 Oct '13, 12:47)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26906-form-container" class="comment-form-container">
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

<span id="26908"></span>

<div id="answer-container-26908" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26908-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-26908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vincent de Phily has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would file a bug against JOSM's validator because the fix displayed in your image should be avoided. It is not very clean and has no purpose except avoiding a warning of a single editor. Other validators handle this case correctly, for example keepright never reports such issues but is able to identify other overlapping ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Oct '13, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-26908" class="comments-container">
<span id="26913"></span>
<div id="comment-26913" class="comment">
<div id="post-26913-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Thanks.</p>
<p>Ticket created : <a href="https://josm.openstreetmap.de/ticket/9140">https://josm.openstreetmap.de/ticket/9140</a></p>
</div>
<div id="comment-26913-info" class="comment-info">
<span class="comment-age">(02 Oct '13, 17:16)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="26964"></span>
<div id="comment-26964" class="comment">
<div id="post-26964-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Fixed in JOSM 6300.</p>
</div>
<div id="comment-26964-info" class="comment-info">
<span class="comment-age">(06 Oct '13, 16:48)</span> <span class="comment-user userinfo">don-vip</span>
</div>
</div>
</div>
<div id="comment-tools-26908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26908-form-container" class="comment-form-container">
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

