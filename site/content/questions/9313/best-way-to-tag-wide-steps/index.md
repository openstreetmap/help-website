+++
type = "question"
title = "Best way to tag wide steps?"
description = '''How would you tag a set of wide steps, like those found in a brick-surfaced park or palazzo? When using &quot;highway=pedestrian; area=yes&quot;, connecting these areas that are on different levels with a single way just doesn&#x27;t cut it.'''
date = "2011-12-02T14:45:00Z"
lastmod = "2011-12-03T04:14:00Z"
weight = 9313
keywords = [ "pedestrian", "steps", "area" ]
aliases = [ "/questions/9313" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Best way to tag wide steps?](/questions/9313/best-way-to-tag-wide-steps)

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
<span id="post-9313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9313-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How would you tag a set of wide steps, like those found in a brick-surfaced park or palazzo? When using "highway=pedestrian; area=yes", connecting these areas that are on different levels with a single way just doesn't cut it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-steps" rel="tag" title="see questions tagged &#39;steps&#39;">steps</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '11, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/7a76490c93062562b6a4674a380b87d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wambag&#39;s gravatar image" />
<p><span>wambag</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wambag has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9313" class="comments-container">
<span id="9314"></span>
<div id="comment-9314" class="comment">
<div id="post-9314-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What's wrong with "highway=steps" ?</p>
</div>
<div id="comment-9314-info" class="comment-info">
<span class="comment-age">(02 Dec '11, 16:03)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="9315"></span>
<div id="comment-9315" class="comment">
<div id="post-9315-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>highway=steps is for ways and therefore a rather poor solution for connecting large areas which have one wide stair instead of one or more narrow ones. One could tag an area between those two other areas as highway=steps, but then something like a direction tag is needed to indicate the direction of the steps.</p>
</div>
<div id="comment-9315-info" class="comment-info">
<span class="comment-age">(02 Dec '11, 16:16)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="9318"></span>
<div id="comment-9318" class="comment">
<div id="post-9318-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also wanted to ask that. It applies to more objects that are usually linear, but sometimes they are not...</p>
</div>
<div id="comment-9318-info" class="comment-info">
<span class="comment-age">(02 Dec '11, 17:45)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-9313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9313-form-container" class="comment-form-container">
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

<span id="9320"></span>

<div id="answer-container-9320" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9320-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-9320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no established solution for this yet, so it is too early to answer the question.</p>
<p>You should definitely create a highway=steps way. Today's applications will usually not understand anything else.</p>
<p>It is likely that future solutions to the problem will still involve a highway=steps way indicating the up/down direction, which also serves as a fallback for more primitive applications. The area covered by the steps can be mapped <em>in addition</em> to this, similar to the banks of large rivers. A tag that has been proposed for this purpose is <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/area:highway">area:highway</a>=steps.</p>
<p>Other approaches under discussion include <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Area#Area-steps.2C_steps_which_are_wide_and.2For_irregular">Area Relations</a>, as well as a draft for <a href="https://wiki.openstreetmap.org/wiki/DE:Stairs_modelling">Stairs Modelling</a> (German text with images) that would provide all the information necessary even for 3D visualization, but is still unfinished and cannot be used as a tagging guideline at this point.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '11, 18:21</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-9320" class="comments-container">
&#10;</div>
<div id="comment-tools-9320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9320-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9317"></span>

<div id="answer-container-9317" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9317-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've thought of this as analogous to river/riverbank, where a way (waterway=river, or highway=steps) can show the flow direction and an area (waterway=riverbank, or highway=steps; area=yes) the exact boundaries.</p>
<p><a href="http://www.mail-archive.com/talk@openstreetmap.org/msg30153.html">More discussion</a> on OSM-Talk last year. Some combination of highway=steps; area=yes with a way to denote up/down seemed popular.</p>
<p>Another proposed option is here: <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Area#area-steps">Proposed Area Relations</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '11, 17:01</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-9317" class="comments-container">
<span id="9324"></span>
<div id="comment-9324" class="comment">
<div id="post-9324-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you all who commented. Yep, I figured this was an issue that must have been discussed, I just did not know in which forum. Funny, seems like this is a recurring theme that an agreed-upon area relation could handle in many situations, not just with steps but with any way that is not best described by a line. As with the river/riverbank case, it is an awkward marriage of the technical and aesthetic aspects of mapping.</p>
</div>
<div id="comment-9324-info" class="comment-info">
<span class="comment-age">(03 Dec '11, 04:14)</span> <span class="comment-user userinfo">wambag</span>
</div>
</div>
</div>
<div id="comment-tools-9317" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9317-form-container" class="comment-form-container">
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

