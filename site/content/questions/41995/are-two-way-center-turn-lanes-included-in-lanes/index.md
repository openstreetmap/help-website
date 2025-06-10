+++
type = "question"
title = "Are two-way center turn lanes included in &quot;lanes=&quot;?"
description = '''Are two-way center turn lanes (example) to be included when adding &quot;lanes=&quot;?'''
date = "2015-03-29T17:07:00Z"
lastmod = "2015-03-29T20:03:00Z"
weight = 41995
keywords = [ "lanes", "turnlanes" ]
aliases = [ "/questions/41995" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Are two-way center turn lanes included in "lanes="?](/questions/41995/are-two-way-center-turn-lanes-included-in-lanes)

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
<span id="post-41995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41995-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Are two-way center turn lanes (<a href="https://commons.wikimedia.org/wiki/File:Citystreet.svg">example</a>) to be included when adding "lanes="?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-turnlanes" rel="tag" title="see questions tagged &#39;turnlanes&#39;">turnlanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '15, 17:07</strong></p>
<img src="https://secure.gravatar.com/avatar/500d1cf90bf7d1402320bd860264bed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AmaryllisGardener&#39;s gravatar image" />
<p><span>AmaryllisGar...</span><br />
<span class="score" title="341 reputation points">341</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AmaryllisGardener has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '15, 17:31</strong> </span></p>
</div>
</div>
<div id="comments-container-41995" class="comments-container">
&#10;</div>
<div id="comment-tools-41995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41995-form-container" class="comment-form-container">
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

<span id="41999"></span>

<div id="answer-container-41999" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41999-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-41999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AmaryllisGardener has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looks to me like there is a separate tag, see: <a href="https://wiki.openstreetmap.org/wiki/Key:centre_turn_lane">https://wiki.openstreetmap.org/wiki/Key:centre_turn_lane</a></p>
<p>On the other hand, there is another section that says it should be counted as a lane: <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/lanes_General_Extension/ProposalPreVoting#Center.2Fmedian_turn_lanes">https://wiki.openstreetmap.org/wiki/Proposed_features/lanes_General_Extension/ProposalPreVoting#Center.2Fmedian_turn_lanes</a></p>
<p>There appears to be support for the "turn lanes" tagging in at least one renderer that I am aware of and in JOSM: <a href="https://wiki.openstreetmap.org/wiki/Key:turn#Turning_indications_per_lane">https://wiki.openstreetmap.org/wiki/Key:turn#Turning_indications_per_lane</a></p>
<p>Given that mis-mash of tagging descriptions, I have avoided tagging center turn lanes. However I think I'd probably tag your example as:</p>
<p>lanes=5, lanes:forward=2, lanes:backward=2, lanes:both_ways=1, centre_turn_lane=yes</p>
<p>Which, I think, covers the different ways I see in the wiki. Looks like everyone else is confused too as there are only a small number of roads tagged either way even though that is a fairly common road geometry.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '15, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '15, 19:45</strong> </span></p>
</div>
</div>
<div id="comments-container-41999" class="comments-container">
<span id="42001"></span>
<div id="comment-42001" class="comment">
<div id="post-42001-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That makes sense. Thank you! :)</p>
</div>
<div id="comment-42001-info" class="comment-info">
<span class="comment-age">(29 Mar '15, 20:03)</span> <span class="comment-user userinfo">AmaryllisGar...</span>
</div>
</div>
</div>
<div id="comment-tools-41999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41999-form-container" class="comment-form-container">
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

