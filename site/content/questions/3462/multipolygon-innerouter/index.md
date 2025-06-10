+++
type = "question"
title = "multipolygon inner/outer"
description = '''Can a multipolygon outer share part of a way with an inner of the same multipolygon?'''
date = "2011-03-01T02:28:00Z"
lastmod = "2021-12-07T17:46:00Z"
weight = 3462
keywords = [ "outer", "inner", "multipolygon" ]
aliases = [ "/questions/3462" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [multipolygon inner/outer](/questions/3462/multipolygon-innerouter)

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
<span id="post-3462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3462-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can a multipolygon outer share part of a way with an inner of the same multipolygon?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-outer" rel="tag" title="see questions tagged &#39;outer&#39;">outer</span> <span class="post-tag tag-link-inner" rel="tag" title="see questions tagged &#39;inner&#39;">inner</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Mar '11, 02:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a6cb4a88637b00f42389b7550700b70c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="upstream&#39;s gravatar image" />
<p><span>upstream</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="upstream has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3462" class="comments-container">
<span id="82776"></span>
<div id="comment-82776" class="comment">
<div id="post-82776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm seeing a lot of people putting "simple" concave multipolygons (multipolygon relations that have no holes and folds into itself without crossing) with the concave parts as "inner" - am I missing something, or despite being concave, should it not still be outer?</p>
<p>Since I'm seeing this a lot, just need to make sure and there's no clear examples anywhere though I can see why someone might call it "inner" ... incorrectly I assume.</p>
<p>Example: think of a "PacMan" figure, and imagine a way that traces the edges. This way that traces the edges no matter how it's split up into a multipolygon relation, all of the ways should be "outer" including the concave "mouth" portion, and the eye, if drawn, would be the only part that could be "inner"?</p>
<p>Example: if tracing a multipolygon that looks like ⛻ there should be zero "inner" ways.</p>
<p>Another example: think of a spiral shaped hedge. All ways should be "outer" including the center of the spiral.</p>
<p>All three of these examples could be drawn without a multipolygon but ignore that for now... (except if PacMan had an eye...)</p>
</div>
<div id="comment-82776-info" class="comment-info">
<span class="comment-age">(07 Dec '21, 11:15)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="82787"></span>
<div id="comment-82787" class="comment">
<div id="post-82787-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tagging those ways as inner would almost certainly be considered an error. Can you give an example of one of these?</p>
</div>
<div id="comment-82787-info" class="comment-info">
<span class="comment-age">(07 Dec '21, 16:54)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="82788"></span>
<div id="comment-82788" class="comment">
<div id="post-82788-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've been correcting them as my gut feel was that it was indeed an error. Here's one I haven't touched yet though it wasn't as egregious as others I've seen:</p>
<p><a href="https://www.openstreetmap.org/relation/11117214">https://www.openstreetmap.org/relation/11117214</a></p>
<p>specifically at this member: <a href="https://www.openstreetmap.org/way/805895181">https://www.openstreetmap.org/way/805895181</a></p>
<p>This member should be marked as "outer" despite being "inside" as far as I know about how topology works.</p>
</div>
<div id="comment-82788-info" class="comment-info">
<span class="comment-age">(07 Dec '21, 17:20)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="82789"></span>
<div id="comment-82789" class="comment">
<div id="post-82789-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, that way should be an outer. The JOSM validator throws an error that the multipolygon isn't closed, which is true because there isn't a continuous ring of outer ways due to that one mis-roled way.</p>
</div>
<div id="comment-82789-info" class="comment-info">
<span class="comment-age">(07 Dec '21, 17:46)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-3462" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3462-form-container" class="comment-form-container">
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

<span id="3463"></span>

<div id="answer-container-3463" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3463-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-3463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No. The outer and inner of a multipolygon relation must not touch or cross. No sharing of points either.<br />
</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Relation:multipolygon">http://wiki.openstreetmap.org/wiki/Relation:multipolygon</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '11, 02:35</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Mar '11, 02:39</strong> </span></p>
</div>
</div>
<div id="comments-container-3463" class="comments-container">
<span id="3465"></span>
<div id="comment-3465" class="comment">
<div id="post-3465-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The reason being because if the 'inner' touches the 'outer', then it is no longer 'inner' - the 'outer' way can just divert around what was the 'inner' to exclude the inner area.</p>
</div>
<div id="comment-3465-info" class="comment-info">
<span class="comment-age">(01 Mar '11, 09:30)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="3474"></span>
<div id="comment-3474" class="comment">
<div id="post-3474-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Interestingly in OSM we allow inner rings to touch. This is not conform to standard OGC Simple Features but allows for simpler modeling in OSM when you have multiple different adjacent features inside the outer way which you want to exclude from the polygon.</p>
</div>
<div id="comment-3474-info" class="comment-info">
<span class="comment-age">(01 Mar '11, 11:59)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-3463" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3463-form-container" class="comment-form-container">
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

