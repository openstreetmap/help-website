+++
type = "question"
title = "Block Mailbox tagging?"
description = '''In apartment complexes and in new neighborhoods in parts of the US, residential mail delivery is to block mailboxes in a centralized location. For larger residential units, these are often inside a building (or at least covered); for smaller area, they are often a free-standing unit at the side of a...'''
date = "2012-10-09T17:54:00Z"
lastmod = "2012-10-17T00:14:00Z"
weight = 16762
keywords = [ "post_box", "tagging" ]
aliases = [ "/questions/16762" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Block Mailbox tagging?](/questions/16762/block-mailbox-tagging)

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
<span id="post-16762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16762-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In apartment complexes and in new neighborhoods in parts of the US, residential mail delivery is to block mailboxes in a centralized location. For larger residential units, these are often inside a building (or at least covered); for smaller area, they are often a free-standing unit at the side of a road. There will often be an outgoing mail receptacle with block mailboxes, but it's not usually a free-standing post box, and is typically for low-volume use.</p>
<p><strong>Amenity=post_box</strong> seems only for outgoing mail. Further, it seems too broad for the (limited) collection capability at most block mailboxes.</p>
<p>How should these be tagged?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-post_box" rel="tag" title="see questions tagged &#39;post_box&#39;">post_box</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '12, 17:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d22c8e8717accc04bd5ef650d9e38611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bellhalla&#39;s gravatar image" />
<p><span>Bellhalla</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bellhalla has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16762" class="comments-container">
<span id="16822"></span>
<div id="comment-16822" class="comment">
<div id="post-16822-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's used for incoming as well.</p>
</div>
<div id="comment-16822-info" class="comment-info">
<span class="comment-age">(11 Oct '12, 01:59)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-16762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16762-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="16766"></span>

<div id="answer-container-16766" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16766-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The question highlights a deficiency in the tagging of post boxes / letterboxes that should be "addressed" (pun not intended!).</p>
<p>There does not appear to be a tag for a mail box used for inbound mail. In Australia we refer to such things (outside houses and groups of apartments) as "letterboxes" - they are small privately-owned boxes for inbound mail - located on private land, usually just off the sidewalk. Here, the postal service never collects mail from letter boxes.</p>
<p>The wiki assumes an amenity=post_box is a larger box provided by the postal service (often placed on public land such as a sidewalk), where a community deposits outbound mail.</p>
<p>In the absence of tagging for a residential "letterbox" function (or more accurately, a combined postbox/letterbox in your case), I'd consider adding some custom tags to post_box like... amenity=post_box type=residential (or private) inbound=yes outbound=yes</p>
<p>You could also add the street address to the node... and there might be a way to add the range of unit / apartment / flat / lot numbers that are serviced by the group of letterboxes. The address tags for building entrance nodes cater for ranges of apartment (flat) numbers, so perhaps a similar adoption in this case is appropriate.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '12, 19:07</strong></p>
<img src="https://secure.gravatar.com/avatar/4200f1aaa4fa9ccd4d02db2e8e670de1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolftracker&#39;s gravatar image" />
<p><span>wolftracker</span><br />
<span class="score" title="475 reputation points">475</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolftracker has 2 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-16766" class="comments-container">
<span id="16818"></span>
<div id="comment-16818" class="comment">
<div id="post-16818-score" class="comment-score">
3
</div>
<div class="comment-text">
<blockquote>
<p>The wiki assumes an amenity=post_box is a larger box provided by the postal service (often placed on public land such as a sidewalk), where a community deposits outbound mail.</p>
</blockquote>
<p>Let's keep it that way and find a completely different tag for inbound mailboxes.</p>
</div>
<div id="comment-16818-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 19:32)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-16766" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16766-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16952"></span>

<div id="answer-container-16952" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16952-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Canada as an <a href="http://wiki.openstreetmap.org/wiki/Canadian_tagging_guidelines#Mail_Box">established tagging scheme</a> for those. Until it, these use the normal amenity=post_box (because the Canadian ones, at least allow mail to be posted there, though smaller than at the traditional boxes), with the <code>type=cmb</code> identifying them. <a href="http://www.openstreetmap.org/browse/node/322886298">Here's one.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '12, 00:14</strong></p>
<img src="https://secure.gravatar.com/avatar/01d01832dff61a6bcf68913f1dc001bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Circeus&#39;s gravatar image" />
<p><span>Circeus</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Circeus has 2 accepted answers">7%</span></p>
</div>
</div>
<div id="comments-container-16952" class="comments-container">
&#10;</div>
<div id="comment-tools-16952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16952-form-container" class="comment-form-container">
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

