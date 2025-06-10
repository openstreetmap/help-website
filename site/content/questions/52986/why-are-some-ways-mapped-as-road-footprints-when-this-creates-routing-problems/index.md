+++
type = "question"
title = "Why are some ways mapped as road footprints when this creates routing problems?"
description = '''I have noticed certain areas have many ways mapped as the footprints of the physical roads, such as this in Indio, California. However, this polygon way itself comprises an ordered list of nodes in its perimeter. Any routing queries passing through this way must traverse the perimeter nodes in order...'''
date = "2016-11-16T21:58:00Z"
lastmod = "2016-11-17T19:35:00Z"
weight = 52986
keywords = [ "openstreetmap", "map", "ways", "mapping", "way" ]
aliases = [ "/questions/52986" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why are some ways mapped as road footprints when this creates routing problems?](/questions/52986/why-are-some-ways-mapped-as-road-footprints-when-this-creates-routing-problems)

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
<span id="post-52986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52986-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have noticed certain areas have many ways mapped as the footprints of the physical roads, such as <a href="https://www.openstreetmap.org/way/407550221#map=19/33.74460/-116.28984">this in Indio, California</a>. However, this polygon way itself comprises an ordered list of nodes in its perimeter. Any routing queries passing through this way must traverse the perimeter nodes in order.</p>
<p>In other words, in the real world I can traverse this way as a <a href="https://www.google.com/maps/place/33%C2%B044&#39;40.6%22N+116%C2%B017&#39;23.4%22W/@33.7444395,-116.290113,225m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d33.7446!4d-116.28984">straight-line path</a>, but in OSM I must traverse this way as a twisting, curling path along its perimeter. This causes shortest-path routing problems when I use this way data in other applications. Similarly, certain areas such as <a href="https://www.openstreetmap.org/way/412802431">this in Folsom, California</a> represent houses' driveways as disconnected way polygons.</p>
<p>My question is: are these polygon representations of ways correct? If so, why?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '16, 21:58</strong></p>
<img src="https://secure.gravatar.com/avatar/8eb28ad933ae655db57b6c6b8563eb67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gboeing&#39;s gravatar image" />
<p><span>gboeing</span><br />
<span class="score" title="136 reputation points">136</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gboeing has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52986" class="comments-container">
<span id="53005"></span>
<div id="comment-53005" class="comment">
<div id="post-53005-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>All those abstract and unsquare polygons in the Folsom area look like a cubist painting!</p>
</div>
<div id="comment-53005-info" class="comment-info">
<span class="comment-age">(17 Nov '16, 19:35)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-52986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52986-form-container" class="comment-form-container">
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

<span id="52989"></span>

<div id="answer-container-52989" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52989-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-52989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gboeing has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tagging it in the way that you have linked to is bad practice and not recommended by most OSM mappers, for exactly the reasons you describe.</p>
<p>The more accepted tagging is <code>area:highway=service</code> (see <a href="http://taginfo.openstreetmap.org/keys/area%3Ahighway">http://taginfo.openstreetmap.org/keys/area%3Ahighway</a> and <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/area:highway).">https://wiki.openstreetmap.org/wiki/Proposed_features/area:highway).</a> Previously some mappers would use a standard highway tag with <code>area=yes</code>, but this does not degrade gracefully for those clients that don't check the <code>area</code> tag.</p>
<p>In any case, you should supply a routable centreline with a standard <code>highway</code> tag as well as the polygon outline.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '16, 22:59</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-52989" class="comments-container">
&#10;</div>
<div id="comment-tools-52989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52989-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52990"></span>

<div id="answer-container-52990" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52990-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-52990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Currently none of the main-stream routing engines support routing over areas properly (not that it can't be done, if just hasn't been).</p>
<p>The camps are slightly divided on if additional ways should be added to improve routing till the point in time that area routing is supported more wide spread, or if such ways should not be added.</p>
<p>Doing the first naturally removes pressure on the routing engine developers to actually fix the issue, doing the later makes current apps work better.</p>
<p>As you can see, there is not going to be a hard and fast answer to your question.</p>
<p>PS: it should be noted, as Richard has pointed out, that the tagging of the driveways is broken in any case, landuse residential should be used for the whole area in question not for individual driveways. And if you are mapping the driveways as areas (with better tagging), you should likely be mapping the actual roads that way too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '16, 23:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '16, 07:49</strong> </span></p>
</div>
</div>
<div id="comments-container-52990" class="comments-container">
&#10;</div>
<div id="comment-tools-52990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52990-form-container" class="comment-form-container">
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

