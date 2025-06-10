+++
type = "question"
title = "calculation of area of nodes in osm"
description = '''Hey, i want to calculate the area of trees in a city (Zürich, Switzerland), but when i do this (Python or QGIS) the result is 0. When you take a look on the map, there are many trees found with &quot;natural=tree&quot;. How does the calculation of Nodes work? And what is the area of the tree that is calculate...'''
date = "2022-05-30T16:02:00Z"
lastmod = "2022-05-31T11:52:00Z"
weight = 84625
keywords = [ "node" ]
aliases = [ "/questions/84625" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [calculation of area of nodes in osm](/questions/84625/calculation-of-area-of-nodes-in-osm)

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
<span id="post-84625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84625-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey, i want to calculate the area of trees in a city (Zürich, Switzerland), but when i do this (Python or QGIS) the result is 0. When you take a look on the map, there are many trees found with "natural=tree". How does the calculation of Nodes work? And what is the area of the tree that is calculated - only the trunk? And maybe it's just a really small number that the output is 0? Thanks for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '22, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/749db2750393b3be709a6e9a2c654b39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="milo22948392&#39;s gravatar image" />
<p><span>milo22948392</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="milo22948392 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84625" class="comments-container">
&#10;</div>
<div id="comment-tools-84625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84625-form-container" class="comment-form-container">
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

<span id="84626"></span>

<div id="answer-container-84626" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84626-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-84626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nodes are points, so have no area.</p>
<p>For <a href="https://wiki.openstreetmap.org/wiki/Tag:natural%3Dtree">trees the wiki</a> mentions optional tags of circumference, diameter, and diameter_crown which you could use to calculate an approximate area.</p>
<p>Overpass suggests these are little used in Zurich (diameter_crown is on one tree note and three tree row ways for example).</p>
<p>There might also be larger areas tagged with landuse=forest or natural=wood.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '22, 17:18</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-84626" class="comments-container">
<span id="84628"></span>
<div id="comment-84628" class="comment">
<div id="post-84628-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Perhaps you could count the trees and multiple by an average circumference, add to the areas of separately mapped wood and forest, abd then try and see if there's any overlap between the two (individual trees mapped in an area of wood or forest)?</p>
</div>
<div id="comment-84628-info" class="comment-info">
<span class="comment-age">(30 May '22, 17:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84630"></span>
<div id="comment-84630" class="comment">
<div id="post-84630-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>For completeness, in addition to the nodes and areas already mentioned, there is also a line: natural=tree_row. I don't know about Zürich but in my city this is used quite a lot on tree-lined avenues.</p>
</div>
<div id="comment-84630-info" class="comment-info">
<span class="comment-age">(30 May '22, 17:43)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="84634"></span>
<div id="comment-84634" class="comment">
<div id="post-84634-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much!</p>
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: is there any technique to check if there's an overlap or do i just check some samples in the map?</p>
</div>
<div id="comment-84634-info" class="comment-info">
<span class="comment-age">(31 May '22, 09:15)</span> <span class="comment-user userinfo">milo22948392</span>
</div>
</div>
<span id="84639"></span>
<div id="comment-84639" class="comment">
<div id="post-84639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sampling might be the easiest way, because I suspect that most single trees won't be in areas mapped as woodland, but it might be possible to do something with Overpass turbo (perhaps see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example</a> - there are some "X within Y" examples there) or using a geographically aware database (an example of this sort of question is <a href="https://gis.stackexchange.com/questions/290072/locating-geometries-within-a-polygon-area">https://gis.stackexchange.com/questions/290072/locating-geometries-within-a-polygon-area</a> - have a look at that and links from there).</p>
</div>
<div id="comment-84639-info" class="comment-info">
<span class="comment-age">(31 May '22, 11:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84626" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84626-form-container" class="comment-form-container">
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

