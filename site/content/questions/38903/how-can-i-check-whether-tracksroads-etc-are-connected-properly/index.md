+++
type = "question"
title = "How can I check whether tracks/roads etc. are connected properly?"
description = '''How can I check whether tracks/roads etc. are connected properly? I have some examples where I know that much better route exist but I can not see in OSM where the tracks/roads are not connected properly. How to check?'''
date = "2014-11-28T21:05:00Z"
lastmod = "2014-11-28T21:22:00Z"
weight = 38903
keywords = [ "tracks", "quality_assurance", "connection", "check" ]
aliases = [ "/questions/38903" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I check whether tracks/roads etc. are connected properly?](/questions/38903/how-can-i-check-whether-tracksroads-etc-are-connected-properly)

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
<span id="post-38903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38903-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I check whether tracks/roads etc. are connected properly?</p>
<p>I have some examples where I know that much better route exist but I can not see in OSM where the tracks/roads are not connected properly.</p>
<p>How to check?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tracks" rel="tag" title="see questions tagged &#39;tracks&#39;">tracks</span> <span class="post-tag tag-link-quality_assurance" rel="tag" title="see questions tagged &#39;quality_assurance&#39;">quality_assurance</span> <span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-check" rel="tag" title="see questions tagged &#39;check&#39;">check</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '14, 21:05</strong></p>
<img src="https://secure.gravatar.com/avatar/5af0874dec426fc7ba735e1416e9febb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Axel%20Kaske&#39;s gravatar image" />
<p><span>Axel Kaske</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Axel Kaske has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '14, 21:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-38903" class="comments-container">
&#10;</div>
<div id="comment-tools-38903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38903-form-container" class="comment-form-container">
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

<span id="38904"></span>

<div id="answer-container-38904" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38904-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-38904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use various quality assurance tools to check for "almost-junctions". E.g. keep right or OSM inspector – OSMi – (routing view). OSMi in addition shows you parts of the road network which are "islands" (i.e. not connected to the rest of the network). There are more tools with similar features. See <span>QA in our wiki</span>.</p>
<p>Of course you could simply use routing engines and look at some routes. <a href="http://map.project-osrm.org/">OSRM</a> is very handy, because of its route dragging feature in the web interface.</p>
<p>And if you mean to check if there is a connection of two or more ways inside your editor: your editor may show nodes which are used by more than one way in a different shape/colour. This works everywhere: move the suspected connection with the mouse a bit. All connected ways will also move then. After this, be sure to use "undo" to undo your test move. This method could be regarded as troublesome, because you may forget to undo or undo too much, …</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '14, 21:22</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '14, 21:25</strong> </span></p>
</div>
</div>
<div id="comments-container-38904" class="comments-container">
&#10;</div>
<div id="comment-tools-38904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38904-form-container" class="comment-form-container">
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

