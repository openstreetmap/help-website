+++
type = "question"
title = "facade surface"
description = '''Is there a way to determine exact area ovccupied by buildings or even better the lenght of the building surface (perimeter)? To top that I would need infusion of building heihgt to calculate facade area and I would need to restrict the surface to backyards and south-east to south-west oriented facad...'''
date = "2012-03-14T15:45:00Z"
lastmod = "2012-04-04T08:07:00Z"
weight = 11194
keywords = [ "building" ]
aliases = [ "/questions/11194" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [facade surface](/questions/11194/facade-surface)

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
<span id="post-11194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11194-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to determine exact area ovccupied by buildings or even better the lenght of the building surface (perimeter)? To top that I would need infusion of building heihgt to calculate facade area and I would need to restrict the surface to backyards and south-east to south-west oriented facades. Pseudocode may be:</p>
<p>Extract all Polygons of type building subtract polygon sides which are parallel within 5m to streets subtract polygon sides which are oriented towards east or north or west add attribute for estimated building height multiply height * length for the remaining polygon sections</p>
<p>I have installed Qgis but this does not offer such a tool- for achieving this. What tool is capabale of doing this? And are there cities with 3D building Models in OSM?</p>
<p>thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '12, 15:45</strong></p>
<img src="https://secure.gravatar.com/avatar/1e05effdec47314f6edf2185a9060cad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="E_fried&#39;s gravatar image" />
<p><span>E_fried</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="E_fried has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11194" class="comments-container">
&#10;</div>
<div id="comment-tools-11194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11194-form-container" class="comment-form-container">
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

<span id="11716"></span>

<div id="answer-container-11716" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11716-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are <a href="http://wiki.openstreetmap.org/wiki/Category:3D">various wiki-pages</a> regarding 3d-modelling and rendering of buildings with osm data you might want to consult. 3D-Tagging of buildings is still rather experimential and highly fragmentary. However, the city of Rostock seems to contain most building heights due to an <a href="http://wiki.openstreetmap.org/wiki/OSM-3D#Some_Interesting_Places">import</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '12, 08:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d732dd313768bd27c4ecc89ab4898c69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FischersFritz&#39;s gravatar image" />
<p><span>FischersFritz</span><br />
<span class="score" title="191 reputation points">191</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FischersFritz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11716" class="comments-container">
&#10;</div>
<div id="comment-tools-11716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11716-form-container" class="comment-form-container">
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

