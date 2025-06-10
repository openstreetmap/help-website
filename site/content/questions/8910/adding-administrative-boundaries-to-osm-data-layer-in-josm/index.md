+++
type = "question"
title = "Adding administrative boundaries to OSM Data Layer in JOSM"
description = '''I have selected civil parish boundaries from OS Boundary-Line for my area of South Oxfordshire, converted them to WGS84 and created a .osm file. These boundaries are polygons, yet the boundaries in OSM that I see are lines. From some articles I have read, I assume that the OS boundaries are merged w...'''
date = "2011-11-10T18:59:00Z"
lastmod = "2011-11-12T12:50:00Z"
weight = 8910
keywords = [ "opendata", "boundaries", "josm" ]
aliases = [ "/questions/8910" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Adding administrative boundaries to OSM Data Layer in JOSM](/questions/8910/adding-administrative-boundaries-to-osm-data-layer-in-josm)

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
<span id="post-8910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8910-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have selected civil parish boundaries from OS Boundary-Line for my area of South Oxfordshire, converted them to WGS84 and created a .osm file. These boundaries are polygons, yet the boundaries in OSM that I see are lines. From some articles I have read, I assume that the OS boundaries are merged with the OSM Data Layer in JOSM and adjusted if necessary to join to existing boundaries or deleted where they are coincident, but they are not completely redrawn. How, then, is the apparent conversion from polygon to line achieved?</p>
<p>Is there another issue, too, where some contributors take no account of features such as roads that are boundary limits in reality, while other contributors link boundary lines to these features to make a relation?<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opendata" rel="tag" title="see questions tagged &#39;opendata&#39;">opendata</span> <span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '11, 18:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ffcc41f13929627742b4936ec178c6f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silver%20mapper&#39;s gravatar image" />
<p><span>silver mapper</span><br />
<span class="score" title="256 reputation points">256</span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silver mapper has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-8910" class="comments-container">
&#10;</div>
<div id="comment-tools-8910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8910-form-container" class="comment-form-container">
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

<span id="8912"></span>

<div id="answer-container-8912" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8912-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-8912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Adminstrative boundaries typically are not isolated but build a mesh - the southern border of county A is the nothern border of county B, etc.</p>
<p>Therefore it is common practice to model boundaries as "multipolygon" or "boundary" relations, contstructed from a number of connected ways, so that the way that forms the border between A and B need only be drawn once, and can be used by both the A and B multipolygons. This is by far the best way of mapping boundaries, and you should strive to split up your polygon into individual border lines that are then re-used like that. (Some border lines will even take part in more than two boundary relations when different admin_levels are involved.)</p>
<p>If the polygon you have loaded from your conversion program is one closed circle, select two (!) points on it by clicking the first, then shift-clicking the second, and press "p" for split in JOSM.</p>
<p>The second-best way of mapping boundaries is to have neighbouring polygons use the same nodes along their common border, but not the same way. This means that along the border you have two ways on top of each other.</p>
<p>The worst way of mapping boundaries, but one that sadly often occurs when people import data without the required diligence, is when separate polygons each have their own, coincidental, set of nodes along the common border.</p>
<p>Whether or not existing features should be used as part of boundary relations is a matter of some discussion. Personally I am very much in favour of using e.g. the way that forms the river as part of the boundary relation. Others say that this must only be done if the river indeed <em>is</em> the boundary - they ask the question: If the river should change its course, would the boundary still follow the river? If yes, use the river geometry; if no, draw a separate geometry.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '11, 19:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Nov '11, 19:41</strong> </span></p>
</div>
</div>
<div id="comments-container-8912" class="comments-container">
<span id="8924"></span>
<div id="comment-8924" class="comment">
<div id="post-8924-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have my boundaries .osm file (like you created) as one layer &amp; the downloaded map area as a 2nd layer. You can then select the single way in the boundaries layer after splitting it, &amp; copy &amp; paste it into the other layer. You then decided yourself what tags it needs, whether to merge the end nodes with existing nodes in the map layer and what relations to add it to. I'm not sure either how you created your boundaries layer; I think ogr2osm which I use creates ways and multipolygon relations if required (I usually convert one parish at a time though, in which case it uses single closed ways).</p>
</div>
<div id="comment-8924-info" class="comment-info">
<span class="comment-age">(11 Nov '11, 09:00)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="8937"></span>
<div id="comment-8937" class="comment">
<div id="post-8937-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In my experience rural UK county and parish boundaries run alongside a road, rather than the road being the boundary. This means the road falls firmly into a county or parish, rather than being shared by two. Sometimes there is a definite kink in the boundary as it crosses from one side to of the road to the other. In urban areas roads are more likely to define the boundary. I would always draw two separate ways for road and a boundary.</p>
</div>
<div id="comment-8937-info" class="comment-info">
<span class="comment-age">(11 Nov '11, 21:31)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
<span id="8946"></span>
<div id="comment-8946" class="comment">
<div id="post-8946-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ed, Chris, I thank you for your comments.</p>
<p>I spent this morning working with several parishes. Having made a .osm file of South Oxfordshire, I used my own batch file to run Chris's excellent <a href="http://extractpoly.py">extractpoly.py</a> to extract a single parish boundary to .osm. My process afterwards replicated exactly what Ed describes. I shan't attempt to relate the Boundary-Line data to existing OSM data: too many issues. I have, though, used the existing administrative boundary in the River Thames. Now, I have to establish whether contributors implement parent/child relations in administrative boundaries.</p>
</div>
<div id="comment-8946-info" class="comment-info">
<span class="comment-age">(12 Nov '11, 12:50)</span> <span class="comment-user userinfo">silver mapper</span>
</div>
</div>
</div>
<div id="comment-tools-8912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8912-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8911"></span>

<div id="answer-container-8911" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8911-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In OSM terms a polygon is a circular way or a multipolygon relation. The convertion tool you used might have converted the polygon into a circular way.</p>
<p>You can just open the file in JOSM and merge it with the existing data. You should then have several ways that together makes a polygon. You should then make a new relation of those ways and tag it with <em>type=multipolygon</em>, <em>name=</em>* and other tags for the multipolygon.</p>
<p>Be aware that a way can be part of many multipolygons and when you edit it you might have to edit the neighbouring multipolygons as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '11, 19:11</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8911" class="comments-container">
&#10;</div>
<div id="comment-tools-8911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8911-form-container" class="comment-form-container">
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

