+++
type = "question"
title = "How to get feature data from OSM?"
description = '''Hi there, I imported the OSM tile layer into Javascript (leaflet), and can see it visually. But how do I access the actual data of the layer? It&#x27;s vector data, made of points, lines, and polygons, right? How can I access the feature data for some part of the map with Javascript, like as json?  Ex: G...'''
date = "2018-01-17T00:03:00Z"
lastmod = "2018-01-17T11:09:00Z"
weight = 61668
keywords = [ "leaflet", "json", "javascript", "geojson" ]
aliases = [ "/questions/61668" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get feature data from OSM?](/questions/61668/how-to-get-feature-data-from-osm)

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
<span id="post-61668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61668-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I imported the OSM tile layer into Javascript (leaflet), and can see it visually. But how do I access the actual data of the layer? It's vector data, made of points, lines, and polygons, right? How can I access the feature data for some part of the map with Javascript, like as json?</p>
<p>Ex: Get the data for the polylines/polygons making up the streets/blocks of a town.</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '18, 00:03</strong></p>
<img src="https://secure.gravatar.com/avatar/25b5e5e3d20e21e07c6201549b17543f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="noncomp&#39;s gravatar image" />
<p><span>noncomp</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="noncomp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '18, 00:15</strong> </span></p>
</div>
</div>
<div id="comments-container-61668" class="comments-container">
<span id="61670"></span>
<div id="comment-61670" class="comment">
<div id="post-61670-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If I understand you well, you mean you want to access, for a certain area of the map, the underlying osm data that the OSM renderer used to create the tiles ?</p>
</div>
<div id="comment-61670-info" class="comment-info">
<span class="comment-age">(17 Jan '18, 02:12)</span> <span class="comment-user userinfo">edvac</span>
</div>
</div>
<span id="61674"></span>
<div id="comment-61674" class="comment">
<div id="post-61674-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, e.g. if it displays an area with some streets and blocks from OSM, I want to be able to access the vector feature data describing those streets and blocks. Thank you, help is much appreciated!</p>
</div>
<div id="comment-61674-info" class="comment-info">
<span class="comment-age">(17 Jan '18, 02:38)</span> <span class="comment-user userinfo">noncomp</span>
</div>
</div>
</div>
<div id="comment-tools-61668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61668-form-container" class="comment-form-container">
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

<span id="61675"></span>

<div id="answer-container-61675" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61675-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="noncomp has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can query the OSM data with <a href="http://overpass-api.de/">Overpass</a>.</p>
<p>There seems to be a <a href="https://github.com/GuillaumeAmat/leaflet-overpass-layer">framework</a> to do that from Leaflet. Another method is to build the query and parse the result yourself in Javascript.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Applications">This page</a> lists some websites that combine Overpass and Leaflet</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '18, 04:09</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '18, 11:09</strong> </span></p>
</div>
</div>
<div id="comments-container-61675" class="comments-container">
<span id="61678"></span>
<div id="comment-61678" class="comment">
<div id="post-61678-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The link you attached to "framework" doesn't link to a leaflet plugin, have you got a direct link? Thank you!</p>
</div>
<div id="comment-61678-info" class="comment-info">
<span class="comment-age">(17 Jan '18, 06:32)</span> <span class="comment-user userinfo">noncomp</span>
</div>
</div>
<span id="61681"></span>
<div id="comment-61681" class="comment">
<div id="post-61681-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>i've corrected the link. sorry for the inconvenience</p>
</div>
<div id="comment-61681-info" class="comment-info">
<span class="comment-age">(17 Jan '18, 11:09)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-61675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61675-form-container" class="comment-form-container">
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

