+++
type = "question"
title = "`destination`: along the whole road or only after a junction?"
description = '''Hello, there. I was wondering: I started tagging destination on highways around me, but been told by another user that such tag is to be put only on the way leaving the junction, not along the whole road. As a GPS user, I&#x27;m accustomed to see, on the screen, the destination to follow even outside jun...'''
date = "2017-06-13T13:38:00Z"
lastmod = "2017-06-14T08:59:00Z"
weight = 56603
keywords = [ "segments", "destination", "tagging", "way", "bestpractice" ]
aliases = [ "/questions/56603" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\`destination\`: along the whole road or only after a junction?](/questions/56603/destination-along-the-whole-road-or-only-after-a-junction)

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
<span id="post-56603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56603-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, there.</p>
<p>I was wondering: I started tagging <code>destination</code> on highways around me, but been told by another user that such tag is to be put only on the way leaving the junction, not along the whole road. As a GPS user, I'm accustomed to see, on the screen, the destination to follow even outside junctions, so I'm mapping this way: I put <code>destination</code> even between junctions, as it seems to me that it eases the work for GPS users and operators integrating OSM data; besides, as it's only applying the same <code>destination</code> key-value pair on all following ways, so it's not a big deal, but is it useful to do it? Am I supposed, or required, to only add <code>destination</code> on the way leaving the junction only, or is it better to continue mapping the whole road?</p>
<p>Awaiting your answers,</p>
<p>Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-segments" rel="tag" title="see questions tagged &#39;segments&#39;">segments</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '17, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/03b6014ac927da400a55374bbbe5152a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Penegal&#39;s gravatar image" />
<p><span>Penegal</span><br />
<span class="score" title="631 reputation points">631</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Penegal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56603" class="comments-container">
&#10;</div>
<div id="comment-tools-56603" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56603-form-container" class="comment-form-container">
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

<span id="56604"></span>

<div id="answer-container-56604" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56604-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Penegal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is my understanding that <code>destination=*</code> should only be on the way connected to the junction, generally the <code>highway=motorway_link</code>. Its use is to allow route guidance to inform you of the wording you will see on the sign marking the motorway exit.</p>
<p>Putting it on all ways makes no sense, especially on bidirectional ways, as generally you can get to lots of different destinations. And we are supposed to be tagging what we see on the ground, I can't recall seeing a destination sign on a highway. Maybe signs giving distances to multiple destinations, but not a sign that says this road goes to "X" and no place else. . .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '17, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-56604" class="comments-container">
<span id="56606"></span>
<div id="comment-56606" class="comment">
<div id="post-56606-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As for "no place else", <a href="https://wiki.openstreetmap.org/wiki/Key:destination">https://wiki.openstreetmap.org/wiki/Key:destination</a> says "Different destinations on the same sign are separated with semicolons". I see a <em>lot</em> of such signs on-the-ground (above the ground, to be precise ;))</p>
</div>
<div id="comment-56606-info" class="comment-info">
<span class="comment-age">(13 Jun '17, 16:40)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="56615"></span>
<div id="comment-56615" class="comment">
<div id="post-56615-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds logical to me; more logical than my previous understanding, in fact. Besides, I now see that the order and presence of different destinations varies along a road, so reporting all of them along the whole road might only confuse the driver by reporting destinations that are only occasionnaly displayed.</p>
</div>
<div id="comment-56615-info" class="comment-info">
<span class="comment-age">(14 Jun '17, 08:59)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
</div>
<div id="comment-tools-56604" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56604-form-container" class="comment-form-container">
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

