+++
type = "question"
title = "What is advantage of using multipolygon relation to create areas eg buildings"
description = '''I have seen a couple of these multipolygon relations to create fairly simple shapes.  Is there any good reason for making a rectangular building by making the 4 walls separately then creating a relationship for them as a building? I find it makes them harder to edit and don&#x27;t see any benefit. Is the...'''
date = "2014-03-27T01:51:00Z"
lastmod = "2014-03-27T16:35:00Z"
weight = 31931
keywords = [ "relations" ]
aliases = [ "/questions/31931" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is advantage of using multipolygon relation to create areas eg buildings](/questions/31931/what-is-advantage-of-using-multipolygon-relation-to-create-areas-eg-buildings)

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
<span id="post-31931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31931-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have seen a couple of these multipolygon relations to create fairly simple shapes.</p>
<p>Is there any good reason for making a rectangular building by making the 4 walls separately then creating a relationship for them as a building?</p>
<p>I find it makes them harder to edit and don't see any benefit. Is there any problem with a node having more than one way go through it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Mar '14, 01:51</strong></p>
<img src="https://secure.gravatar.com/avatar/7c24812608179f09b4374b3231cfb750?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YoP&#39;s gravatar image" />
<p><span>YoP</span><br />
<span class="score" title="506 reputation points">506</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YoP has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-31931" class="comments-container">
&#10;</div>
<div id="comment-tools-31931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31931-form-container" class="comment-form-container">
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

<span id="31942"></span>

<div id="answer-container-31942" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31942-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-31942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no good reason for mapping a simple building as a multipolygon with separate ways for each wall. Ideally, you should talk to the mapper who did this, and if he doesn't come forth with any unexpectedly good explanation, these buildings should be turned into a single closed way each.</p>
<p>In general, multipolygons for areas without holes should only be used for very large areas, and no building comes even close to that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '14, 11:38</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-31942" class="comments-container">
<span id="31950"></span>
<div id="comment-31950" class="comment">
<div id="post-31950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not even when an adjacent area runs right up a wall of the building (eg. a parking lot or another attached building)? Are you saying it's recommended to have overlapping ways rather than using multipolygons to share the way? If not, what's the recommended solution for such a scenario?</p>
</div>
<div id="comment-31950-info" class="comment-info">
<span class="comment-age">(27 Mar '14, 16:27)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="31951"></span>
<div id="comment-31951" class="comment">
<div id="post-31951-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Overlapping ways are a perfectly valid approach of modelling adjacent features. It's semantically equivalent to using a multipolygon and much easier for inexperienced users to work with.</p>
</div>
<div id="comment-31951-info" class="comment-info">
<span class="comment-age">(27 Mar '14, 16:35)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-31942" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31942-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31933"></span>

<div id="answer-container-31933" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31933-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, well I think this question mixes two slightly different things:</p>
<ol>
<li>MPs in general</li>
</ol>
<p>Multipolygones allow you to model more complex shapes as you would be able just with a single closed way. This includes esp. shapes with holes or shapes with 2 completely seperated bodys. Using MPs you can keep the semantics clear ("this is one single object") or don't need to fake the geometries (e.g. keeping a fine line that avoids a full closed hole in a doublebox shape).</p>
<ol>
<li>MPs for buildings</li>
</ol>
<p>Buildings aren't different here, but the <a href="https://wiki.openstreetmap.org/wiki/Simple_3D_Buildings">Simple 3D buildings</a> schema enforces a relation (but not to glue all the walls together). Also some <a href="https://wiki.openstreetmap.org/wiki/Indoor">indoor mapping</a> schemas might make use of this very fine grade of modelling (as you can tag walls seperately). AFAIK this wall based modelling isn't common sense yet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '14, 06:32</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-31933" class="comments-container">
<span id="31941"></span>
<div id="comment-31941" class="comment">
<div id="post-31941-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We are talking about a multipolygon relation, not a building relation, so neither Simple 3D Buildings nor indoor mapping should be relevant here.</p>
</div>
<div id="comment-31941-info" class="comment-info">
<span class="comment-age">(27 Mar '14, 11:30)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-31933" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31933-form-container" class="comment-form-container">
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

