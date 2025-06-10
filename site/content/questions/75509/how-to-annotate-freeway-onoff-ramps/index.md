+++
type = "question"
title = "How to annotate freeway on/off ramps?"
description = '''Consider https://www.openstreetmap.org/#map=17/42.85888/-73.77169. As I write this, I-87 is annotated as having 3 lanes south of the on/off ramps (south of 146). However, the off ramp starts all the way back at the Sitterly Road overpass, and the on ramp doesn&#x27;t fully merge until just before the eme...'''
date = "2020-07-02T22:38:00Z"
lastmod = "2020-07-04T09:44:00Z"
weight = 75509
keywords = [ "lanes" ]
aliases = [ "/questions/75509" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to annotate freeway on/off ramps?](/questions/75509/how-to-annotate-freeway-onoff-ramps)

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
<span id="post-75509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75509-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Consider <a href="https://www.openstreetmap.org/#map=17/42.85888/-73.77169.">https://www.openstreetmap.org/#map=17/42.85888/-73.77169.</a> As I write this, I-87 is annotated as having 3 lanes south of the on/off ramps (south of 146). However, the off ramp starts all the way back at the Sitterly Road overpass, and the on ramp doesn't fully merge until just before the emergency vehicle turn-around only slightly north of said overpass. Accordingly, there are actually four lanes for these stretches.</p>
<p>What is the correct way to model this?</p>
<p>I'm thinking, for the off ramp, the <code>highway:motorway_junction</code> should be pushed back, the relevant segment made 4-lane, and possibly get <code>change:lanes=yes|yes|yes|no</code>; the location where the ramp splits from the freeway should be left as-is (currently where the ramp actually separates from the freeway). For the on ramp, make the relevant segment 4-lane with <code>change:lanes=yes|yes|not_right|yes</code>. Is that the sensible thing to do, or is there another way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '20, 22:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a8c0982f10a17627b74ab9ade7517df6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mwoehlke&#39;s gravatar image" />
<p><span>mwoehlke</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mwoehlke has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75509" class="comments-container">
&#10;</div>
<div id="comment-tools-75509" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75509-form-container" class="comment-form-container">
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

<span id="75532"></span>

<div id="answer-container-75532" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75532-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's not entirely correct in this case. You are allowed to change lanes on merging and diverging lanes as well. They aren't solid white lines. The point of exit indication (<code>highway=motorway_junction</code>) should remain as is.</p>
<p>For clarity, refer to northbound to add a <code>turn:lanes=none|none|none|merge_to_left</code> on southbound.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '20, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '20, 09:47</strong> </span></p>
</div>
</div>
<div id="comments-container-75532" class="comments-container">
&#10;</div>
<div id="comment-tools-75532" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75532-form-container" class="comment-form-container">
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

