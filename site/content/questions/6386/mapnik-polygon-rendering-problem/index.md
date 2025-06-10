+++
type = "question"
title = "Mapnik polygon rendering problem?"
description = '''http://www.openstreetmap.org/?lat=37.89441&amp;amp;lon=-0.96381&amp;amp;zoom=16&amp;amp;layers=M if you look at the map above, the golf course (the bit in green) is sliced down the middle. At different levels of zoom the green and non-green swap sides. Osmarender shows it okay at all levels.'''
date = "2011-07-18T11:21:00Z"
lastmod = "2011-07-20T15:51:00Z"
weight = 6386
keywords = [ "bug", "mapnik" ]
aliases = [ "/questions/6386" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik polygon rendering problem?](/questions/6386/mapnik-polygon-rendering-problem)

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
<span id="post-6386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6386-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="http://www.openstreetmap.org/?lat=37.89441&amp;lon=-0.96381&amp;zoom=16&amp;layers=M">http://www.openstreetmap.org/?lat=37.89441&amp;lon=-0.96381&amp;zoom=16&amp;layers=M</a></p>
<p>if you look at the map above, the golf course (the bit in green) is sliced down the middle. At different levels of zoom the green and non-green swap sides. Osmarender shows it okay at all levels.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '11, 11:21</strong></p>
<img src="https://secure.gravatar.com/avatar/f975d12117093ce5b3b4748dc4927400?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobChafer&#39;s gravatar image" />
<p><span>RobChafer</span><br />
<span class="score" title="220 reputation points">220</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobChafer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6386" class="comments-container">
<span id="6387"></span>
<div id="comment-6387" class="comment">
<div id="post-6387-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe there is a tile border?</p>
</div>
<div id="comment-6387-info" class="comment-info">
<span class="comment-age">(18 Jul '11, 11:25)</span> <span class="comment-user userinfo">Lutz Horn</span>
</div>
</div>
</div>
<div id="comment-tools-6386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6386-form-container" class="comment-form-container">
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

<span id="6388"></span>

<div id="answer-container-6388" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6388-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general, this help system is not suitable for questions like yours. It is intended to collect answers to questions that are likely to be of interest to other people as well. Your question, in contrast, and the concrete example that goes with it, is going to be irrelevant within days (because the problem will then be fixed). Questions like that are best placed on the mailing list, or on IRC.</p>
<p>In your concrete example, the golf course multipolygon is invalid because (at the time of writing) node 945088840 which is part of the inner ring of that polygon actually lies outside of the outer ring, causing an intersection between inner and outer rings. While not all invalid polygons cause rendering problems in the Mapnik layer, I would guess that this is the root of the problem. Problems like this can be found by looking at the <a href="http://tools.geofabrik.de/osmi/?view=multipolygon&amp;lon=-0.97129&amp;lat=37.89527&amp;zoom=17&amp;overlays=invalid_geometry_hull,duplicate_ways,intersections,intersection_lines,ring_not_closed_hull,ring_not_closed,unconnected_end_nodes,touching_inner_rings_hull,touching_inner_rings,role_mismatch_hull,role_mismatch,duplicate_tags_hull,duplicate_tags,multipolygons_type_is_boundary,type_is_boundary,ways,role_markers,way_end_nodes,way_nodes">OSM Inspector Multipolygon Debug Layer</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '11, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-6388" class="comments-container">
<span id="6389"></span>
<div id="comment-6389" class="comment">
<div id="post-6389-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'll bear your comments in mind for future posts... and I'll look at the debug layer.</p>
</div>
<div id="comment-6389-info" class="comment-info">
<span class="comment-age">(18 Jul '11, 11:43)</span> <span class="comment-user userinfo">RobChafer</span>
</div>
</div>
<span id="6391"></span>
<div id="comment-6391" class="comment">
<div id="post-6391-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>'bare in mind' even (how embarrassing)</p>
</div>
<div id="comment-6391-info" class="comment-info">
<span class="comment-age">(18 Jul '11, 13:04)</span> <span class="comment-user userinfo">RobChafer</span>
</div>
</div>
<span id="6455"></span>
<div id="comment-6455" class="comment">
<div id="post-6455-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I fixed the polygon as suggested by the debug layer and it shows now. Thank you for that. Is there a part of the OSM Wiki that describes this and other helpful tools?</p>
</div>
<div id="comment-6455-info" class="comment-info">
<span class="comment-age">(20 Jul '11, 11:27)</span> <span class="comment-user userinfo">RobChafer</span>
</div>
</div>
<span id="6456"></span>
<div id="comment-6456" class="comment">
<div id="post-6456-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A lot of QA tools can be found here: <a href="http://wiki.openstreetmap.org/wiki/Quality_Assurance">http://wiki.openstreetmap.org/wiki/Quality_Assurance</a></p>
</div>
<div id="comment-6456-info" class="comment-info">
<span class="comment-age">(20 Jul '11, 15:51)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
</div>
<div id="comment-tools-6388" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6388-form-container" class="comment-form-container">
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

