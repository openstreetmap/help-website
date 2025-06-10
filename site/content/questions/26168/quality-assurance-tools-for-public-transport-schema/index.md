+++
type = "question"
title = "Quality Assurance tools for Public Transport Schema"
description = '''I&#x27;ve been working lately on mapping the bus lines in my home city (Tucson, AZ, USA), but I&#x27;m not sure how to confirm that my edits are correct. Öpnvkarte and the main site transport layer are nice, and do well with &quot;overshooting&quot; errors where I forgot to properly split a way at a turn in the bus rou...'''
date = "2013-09-07T07:42:00Z"
lastmod = "2013-09-08T16:19:00Z"
weight = 26168
keywords = [ "bus", "public-transport", "quality" ]
aliases = [ "/questions/26168" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Quality Assurance tools for Public Transport Schema](/questions/26168/quality-assurance-tools-for-public-transport-schema)

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
<span id="post-26168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26168-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been working lately on mapping the bus lines in my home city (Tucson, AZ, USA), but I'm not sure how to confirm that my edits are correct.</p>
<p>Öpnvkarte and the main site transport layer are nice, and do well with "overshooting" errors where I forgot to properly split a way at a turn in the bus route. They don't, however, help me to:</p>
<ul>
<li>Keep the ways within the relations ordered (as recommended by the Public Transport schema). I'm especially not sure what happens when I split a way that's part of a relation (e.g. when a bus route I'm mapping now shares a road with a previously-mapped one along a small section).</li>
<li>Deal with stops. I haven't gotten to this step yet, preferring to do the routes first, but the few I've tried don't seem to appear correctly.</li>
</ul>
<p>There's a lot of contradictory information on public transport mapping -- the Öpnvkarte page mentions the 'forward'/'backward' roles, for example, and there's many ways to map stops. I'm wondering if there's a tool I can use as a sort of baseline, or at the very least to check some subset of what I'm doing a bit more thoroughly.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-quality" rel="tag" title="see questions tagged &#39;quality&#39;">quality</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '13, 07:42</strong></p>
<img src="https://secure.gravatar.com/avatar/bb82047b8a0bdf018f053debeb8cf665?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ianmcorvidae&#39;s gravatar image" />
<p><span>ianmcorvidae</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ianmcorvidae has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26168" class="comments-container">
&#10;</div>
<div id="comment-tools-26168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26168-form-container" class="comment-form-container">
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

<span id="26169"></span>

<div id="answer-container-26169" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26169-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I find JOSM useful while creating the relation - double clicking on the relation will highlight it so that it's easy to verify connectivity. It also has a "Public Transport" plugin that will automatically order ways in the relation and assign forward/backward roles to create a continuous path.</p>
<p>Re: Stops - some of the map rendering is behind, so most people tag bus stops with both highway=bus_stop and public_transport=platform to assist with the transition.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '13, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-26169" class="comments-container">
<span id="26171"></span>
<div id="comment-26171" class="comment">
<div id="post-26171-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Good to know -- I don't generally use JOSM (a couple times of it failing to let me type letters was enough -- probably my own fault with OS/window manager choices, but perhaps I'll need to try again!). Do you know how/if the public transport plugin figures out what it should consider the start and which the end?</p>
</div>
<div id="comment-26171-info" class="comment-info">
<span class="comment-age">(07 Sep '13, 11:39)</span> <span class="comment-user userinfo">ianmcorvidae</span>
</div>
</div>
<span id="26204"></span>
<div id="comment-26204" class="comment">
<div id="post-26204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It picks the open segment as start / end. If it picks the wrong direction, you can use the Public Transport Plugin "Reflect" tool to reverse the sense of start and end.</p>
</div>
<div id="comment-26204-info" class="comment-info">
<span class="comment-age">(08 Sep '13, 16:19)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
</div>
<div id="comment-tools-26169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26169-form-container" class="comment-form-container">
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

