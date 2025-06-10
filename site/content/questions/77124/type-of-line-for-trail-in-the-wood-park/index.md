+++
type = "question"
title = "Type of line for trail in the wood (park)."
description = '''What is the best type of line to use when you want to map a trail in a park that is not accessible to vehicles. To date, I have been using HIGHWAY PATH. Tks.'''
date = "2020-10-16T19:47:00Z"
lastmod = "2020-10-16T21:30:00Z"
weight = 77124
keywords = [ "park", "line", "type" ]
aliases = [ "/questions/77124" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Type of line for trail in the wood (park).](/questions/77124/type-of-line-for-trail-in-the-wood-park)

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
<span id="post-77124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77124-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the best type of line to use when you want to map a trail in a park that is not accessible to vehicles. To date, I have been using HIGHWAY PATH. Tks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span> <span class="post-tag tag-link-line" rel="tag" title="see questions tagged &#39;line&#39;">line</span> <span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '20, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/2543a7449d6f2079437d752a76deaa42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="c1954m&#39;s gravatar image" />
<p><span>c1954m</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="c1954m has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77124" class="comments-container">
&#10;</div>
<div id="comment-tools-77124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77124-form-container" class="comment-form-container">
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

<span id="77125"></span>

<div id="answer-container-77125" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77125-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is some variation on this depending on local mapping customs.</p>
<p>If the trail is exclusively for the use of one type of access or even primarily for one type, then you could use <code>highway=cycleway</code> (exclusively or mostly bicycles), <code>highway=footway</code> (exclusively or mostly foot traffic) or <code>highway=bridleway</code> (exclusively or mostly horses). In my area most trails are open for hiking, mountain biking and often equestrian use. My reading of the wiki indicates that these <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dpath">general use trails</a> should be <code>highway=path</code>.</p>
<p>From my point of view when rendering maps, it is very useful to add some other tags to help make clear the type of trail. These additional tags may include <a href="https://wiki.openstreetmap.org/wiki/Key:surface"><code>surface=*</code></a>, <a href="https://wiki.openstreetmap.org/wiki/Key:sac_scale"><code>sac_scale=*</code></a>, <a href="https://wiki.openstreetmap.org/wiki/Key:trail_visibility"><code>trail_visibility=*</code></a>, <code>foot=yes|no</code>, <code>bicycle=yes|no|designated</code>, <code>horse=yes|no</code>, <code>wheelchair=yes|no|designated</code>, and possibly others</p>
<p>I can’t say about other people attempting to render maps, but I consider a hiking trail to be quite different from a walkway in a city park and since mappers can and will use <code>highway=footway</code> or <code>highway=path</code> for each. So adding some other tags are useful in figuring out how to render the trail. For example a way tagged with <code>highway=path, surface=unpaved, trail_visibility=good</code> is likely a hiking trail. But a <code>highway=path, surface=concrete, wheelchair=yes</code> is likely what in my local dialect would be called a “sidewalk” (even if it isn’t along side a road).</p>
<p>So I guess my final advice is to look to see what other mappers in your area have decided to do and follow their example. But please add additional descriptive tags to help clarify what is there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '20, 21:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-77125" class="comments-container">
&#10;</div>
<div id="comment-tools-77125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77125-form-container" class="comment-form-container">
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

