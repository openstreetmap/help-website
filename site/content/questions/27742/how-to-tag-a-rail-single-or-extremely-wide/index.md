+++
type = "question"
title = "How to tag a rail single or extremely wide"
description = '''I searched for a tag to use for a huge rolling door or a wide cranetrack (2) but no luck. I consider to use single_rail instead of mono_rail.'''
date = "2013-11-02T15:47:00Z"
lastmod = "2013-11-07T20:34:00Z"
weight = 27742
keywords = [ "rolling_door", "single_rail", "cranetrack" ]
aliases = [ "/questions/27742" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag a rail single or extremely wide](/questions/27742/how-to-tag-a-rail-single-or-extremely-wide)

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
<span id="post-27742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27742-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I searched for a tag to use for a huge rolling door or a wide cranetrack (2) but no luck. I consider to use single_rail instead of mono_rail.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rolling_door" rel="tag" title="see questions tagged &#39;rolling_door&#39;">rolling_door</span> <span class="post-tag tag-link-single_rail" rel="tag" title="see questions tagged &#39;single_rail&#39;">single_rail</span> <span class="post-tag tag-link-cranetrack" rel="tag" title="see questions tagged &#39;cranetrack&#39;">cranetrack</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '13, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-27742" class="comments-container">
&#10;</div>
<div id="comment-tools-27742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27742-form-container" class="comment-form-container">
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

<span id="27772"></span>

<div id="answer-container-27772" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27772-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><em>Maybe</em> you should use "gauge=0" for the single track rolling door (meaning "no distance between rails") or "gauge=&lt;large_number&gt;" for the dual-rail crane track. Using "gauge=0" probably is incorrect because it would mean "2 rails, but zero millimeters between them".</p>
<p>I did not found any reference to "single_rail" in the wiki except when describing monorail systems, but I think that maybe instead of creating a new tag (that may someday be - or not - the "standard" for this kind of structure), you should use "railway=monorail" since the page for the tag value does not require the monorail to be "a system for passenger/cargo transportation".</p>
<p>Also consider (for the large door) the real relevance of mapping the rail that it runs on. For example, the VAB (Vehicle Assembly Building), one of the buildings with the largest doors in the world, does not have its rails mapped (<em>correcting - they ARE the largest doors in the world!</em>) <a href="http://en.wikipedia.org/wiki/Vehicle_Assembly_Building">see Wikipedia</a>. The same for all the largest industrial plants from Boeing that I could find. For the cranes, I also wasn't able to find any mapped, having taken just a cursory look at some of the largest seaports in the world (Rotterdam, London and area, etc).</p>
<p>Found also that some very large radio telescopes (like the <a href="http://www.openstreetmap.org/#map=18/53.23656/-2.30816">Lovell Telescope</a> or the <a href="http://www.openstreetmap.org/#map=18/50.52500/6.88403">Effelsberg Radio Telescope</a>) do not have the rails they run on mapped.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '13, 12:04</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Nov '13, 12:13</strong> </span></p>
</div>
</div>
<div id="comments-container-27772" class="comments-container">
<span id="27815"></span>
<div id="comment-27815" class="comment">
<div id="post-27815-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, thanks for the answer. But if its visible its worth mapping still ? That's hardly done, goes for bridges and other water works as well, but its IMHO no valid argument. Theyre a kind of building and should be added as well, have a look here <a href="http://www.openstreetmap.org/#map=19/51.87796/5.11822.">http://www.openstreetmap.org/#map=19/51.87796/5.11822.</a></p>
</div>
<div id="comment-27815-info" class="comment-info">
<span class="comment-age">(05 Nov '13, 12:37)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="27827"></span>
<div id="comment-27827" class="comment">
<div id="post-27827-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In the end the decision to add or not to add something to the map is on you. Do you think the data is relevant? Go on and draw it! I wouldn't map the door's rail, but surely would map the crane track, but that's my opinion. So, while I asked you to ponder if the data is relevant, I never said "don't do it".</p>
</div>
<div id="comment-27827-info" class="comment-info">
<span class="comment-age">(05 Nov '13, 14:49)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
<span id="27892"></span>
<div id="comment-27892" class="comment">
<div id="post-27892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The single rail is present, visible and historic. The wide double is a track of 3 cranes, Ill ad the gauge after a survey.</p>
</div>
<div id="comment-27892-info" class="comment-info">
<span class="comment-age">(07 Nov '13, 20:34)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-27772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27772-form-container" class="comment-form-container">
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

