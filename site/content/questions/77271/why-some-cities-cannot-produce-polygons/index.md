+++
type = "question"
title = "Why some cities cannot produce polygons?"
description = '''I try to use this http://polygons.openstreetmap.fr/index.py to create polygons for multiple cities, but I run into an issue of some cities having errors when I try to create polygons. For example, 537353788 does not work and it gives me the following error: http://polygons.openstreetmap.fr/index.py?...'''
date = "2020-10-27T15:08:00Z"
lastmod = "2020-10-27T15:49:00Z"
weight = 77271
keywords = [ "polygons" ]
aliases = [ "/questions/77271" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why some cities cannot produce polygons?](/questions/77271/why-some-cities-cannot-produce-polygons)

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
<span id="post-77271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77271-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I try to use this <a href="http://polygons.openstreetmap.fr/index.py">http://polygons.openstreetmap.fr/index.py</a> to create polygons for multiple cities, but I run into an issue of some cities having errors when I try to create polygons. For example, 537353788 does not work and it gives me the following error: <a href="http://polygons.openstreetmap.fr/index.py?id=537353788">http://polygons.openstreetmap.fr/index.py?id=537353788</a></p>
<p>Any idea how to correct/who to contact?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '20, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/0cd99cd8ea837714526d93ebf2296283?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NelaM99&#39;s gravatar image" />
<p><span>NelaM99</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NelaM99 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77271" class="comments-container">
<span id="77272"></span>
<div id="comment-77272" class="comment">
<div id="post-77272-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How did you arrive at the number 537353788?</p>
</div>
<div id="comment-77272-info" class="comment-info">
<span class="comment-age">(27 Oct '20, 15:13)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="77273"></span>
<div id="comment-77273" class="comment">
<div id="post-77273-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you talking about <a href="https://www.openstreetmap.org/way/537353788">Абай</a>? Its geometry is already defined as a polygon ("closed way" in OSM terms). The page you are referring to is used to convert OSM relations (including multipolygons) into polygons.</p>
</div>
<div id="comment-77273-info" class="comment-info">
<span class="comment-age">(27 Oct '20, 15:30)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="77274"></span>
<div id="comment-77274" class="comment">
<div id="post-77274-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it is Abay. The number is the Place ID number that I get at the bottom of this page: <a href="https://nominatim.openstreetmap.org/ui/details.html?osmtype=R&amp;osmid=421007&amp;class=place">https://nominatim.openstreetmap.org/ui/details.html?osmtype=R&amp;osmid=421007&amp;class=place</a></p>
</div>
<div id="comment-77274-info" class="comment-info">
<span class="comment-age">(27 Oct '20, 15:41)</span> <span class="comment-user userinfo">NelaM99</span>
</div>
</div>
<span id="77275"></span>
<div id="comment-77275" class="comment">
<div id="post-77275-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The link you gave does not show the ID 537353788 for me. If you have a Nominatim query for this village, try adding <code>&amp;polygon_geojson=1</code> to the Nominatim request to download it in GeoJSON form. Else, you could potentially use Overpass Turbo to export a single OSM object as GeoJSON. If you are exporting many such boundaries, save yourself the hassle and load OSM data into a PostGIS database with <code>osm2pgsql</code> and then export stuff from there.</p>
</div>
<div id="comment-77275-info" class="comment-info">
<span class="comment-age">(27 Oct '20, 15:49)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77271" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77271-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

