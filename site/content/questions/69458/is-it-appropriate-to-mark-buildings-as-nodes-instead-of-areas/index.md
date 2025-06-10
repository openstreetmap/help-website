+++
type = "question"
title = "Is it appropriate to mark buildings as nodes instead of areas?"
description = '''The OSM wiki seems to have conflicting information. In &quot;How to map&quot;, it states :  Set a node or draw as an area along the building outline. Tag it with building=*  However, under values, each option depicts using an area as the appropriate way to map the object. Discussion on the linked GitHub issue...'''
date = "2019-06-05T03:40:00Z"
lastmod = "2019-06-05T08:32:00Z"
weight = 69458
keywords = [ "building", "node" ]
aliases = [ "/questions/69458" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Is it appropriate to mark buildings as nodes instead of areas?](/questions/69458/is-it-appropriate-to-mark-buildings-as-nodes-instead-of-areas)

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
<span id="post-69458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69458-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The OSM wiki seems to have conflicting information. In "How to map", it states :</p>
<blockquote>
<p>Set a node or draw as an area along the building outline. Tag it with building=*</p>
</blockquote>
<p>However, under values, each option depicts using an area as the appropriate way to map the object. Discussion on the linked GitHub issue page suggests that it is inappropriate to map buildings this way, and that osm-carto does not display node buildings. The philosophy however, is <em>don't tag for the renderer</em>.</p>
<p>Is it appropriate to use nodes as opposed to no data at all (obviously outlines are more time consuming, but by using nodes some data is present instead of none at all)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '19, 03:40</strong></p>
<img src="https://secure.gravatar.com/avatar/78b12c0b5d3ee8d688e07b6ef3eeb5b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ortho_is_hot&#39;s gravatar image" />
<p><span>ortho_is_hot</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ortho_is_hot has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jun '19, 04:46</strong> </span></p>
</div>
</div>
<div id="comments-container-69458" class="comments-container">
&#10;</div>
<div id="comment-tools-69458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69458-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="69459"></span>

<div id="answer-container-69459" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69459-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-69459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ortho_is_hot has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In all my ignorance of the relevant discussions, my understanding is that yes, it is. One data point is that JOSM has a dedicated icon for displaying building=* nodes, so it's clearly a use case that the developers have explicitly handled. And it makes sense: the fact that there exists a building at this location is useful information even if commonly used styles won't show it. It's possible to query them programmatically and if anyone needs them rendered, that can easily be added. A legitimate use case would be a building you find on the ground in an area not covered by good-enough satellite imagery. You know it's there, you know what it is and have recorded its GPS position, but you don't remember the orientation well enough to draw its outline.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '19, 06:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d62eaa0c9cab6317d2887bfe6bd2163b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbethke&#39;s gravatar image" />
<p><span>mbethke</span><br />
<span class="score" title="381 reputation points">381</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbethke has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-69459" class="comments-container">
<span id="69461"></span>
<div id="comment-69461" class="comment">
<div id="post-69461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, the fact that I saw an icon (in iD) was a bit of an indication for me. Thanks for the answer</p>
</div>
<div id="comment-69461-info" class="comment-info">
<span class="comment-age">(05 Jun '19, 07:56)</span> <span class="comment-user userinfo">ortho_is_hot</span>
</div>
</div>
</div>
<div id="comment-tools-69459" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69459-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69462"></span>

<div id="answer-container-69462" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69462-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Outlines are not always possible. Sometimes this is due to a lack of imagery, sometimes because imagery is out of date and the building is new, or possibly because the building's outlines are difficult to see</p>
<p>In other cases buildings are recorded with a site survey using either mobile software that doesn't support outlines, or the time needed to draw outlines <em>now</em> would delay data availability.</p>
<p>In all of these cases, a node saying, 'there is a building here' is a better state of the map than no data at all, even if it is considered the least important tag for that object.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '19, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-69462" class="comments-container">
&#10;</div>
<div id="comment-tools-69462" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69462-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69465"></span>

<div id="answer-container-69465" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69465-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I agree to the other answers that generally, it is legitimate to create a building node instead of an outline.</p>
<p>Two more thoughts on the topic, though: The information "here is a building", only contained in a node is not very useful by itself. It gets useful if there is address information attached or any hints on the purpose or tenant of the building. These could be tagged as part of the same node or as separate nodes.</p>
<p>If there is no other information on the buildings than their locations I would at least try to define the build-up area by mapping an appropriate landuse (residential, industrial) to give some clue on the extend of the buildings (if there are more than one).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '19, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-69465" class="comments-container">
&#10;</div>
<div id="comment-tools-69465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69465-form-container" class="comment-form-container">
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

