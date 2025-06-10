+++
type = "question"
title = "How do you map a marina that is inside of a park?"
description = '''I&#x27;m relatively new to OSM, but I&#x27;m doing my best to muddle through and learn as I go. My current conundrum that I&#x27;ve been unable to find a solution to has to do with a marina that is inside/adjacent/part of a park. Specifically, here: https://www.openstreetmap.org/#map=17/34.78709/-87.67326 In this ...'''
date = "2016-11-15T16:32:00Z"
lastmod = "2016-11-16T17:20:00Z"
weight = 52968
keywords = [ "marina", "park" ]
aliases = [ "/questions/52968" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do you map a marina that is inside of a park?](/questions/52968/how-do-you-map-a-marina-that-is-inside-of-a-park)

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
<span id="post-52968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52968-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm relatively new to OSM, but I'm doing my best to muddle through and learn as I go. My current conundrum that I've been unable to find a solution to has to do with a marina that is inside/adjacent/part of a park. Specifically, here:</p>
<p><a href="https://www.openstreetmap.org/#map=17/34.78709/-87.67326">https://www.openstreetmap.org/#map=17/34.78709/-87.67326</a></p>
<p>In this specific example, the park extends around the marina and encloses it on 3 sides. Do I map the park to it's extents (i.e. the water's edge) and map the marina and all of its associated features (parking, piers, buildings, bathrooms, etc) resulting in the marina overlapping the park? Or do I map them exclusively separate to where they share a boundary and do not overlap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marina" rel="tag" title="see questions tagged &#39;marina&#39;">marina</span> <span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '16, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/95ff57b6d571cffa00600d67c0e0b81b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wcwalker&#39;s gravatar image" />
<p><span>wcwalker</span><br />
<span class="score" title="81 reputation points">81</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wcwalker has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52968" class="comments-container">
&#10;</div>
<div id="comment-tools-52968" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52968-form-container" class="comment-form-container">
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

<span id="52982"></span>

<div id="answer-container-52982" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52982-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-52982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wcwalker has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It really depends on how you answer whether the marina is "inside", "adjacent" or "part of". If the marina is part of the park, the park boundary should enclose it. If the marina is separate, they can in some way share a boundary. And if the marina is enclosed within the park but separate, you can make a "hole" in the park way with a multipolygon relation.</p>
<p>It doesn't especially matter if different objects overlap, although it may annoy those who tend toward OCD :) And in some cases it is entirely accurate, for example a wood that is both in a park and an adjacent residential area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '16, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-52982" class="comments-container">
&#10;</div>
<div id="comment-tools-52982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52982-form-container" class="comment-form-container">
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

