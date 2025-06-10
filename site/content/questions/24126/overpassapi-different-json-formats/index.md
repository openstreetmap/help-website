+++
type = "question"
title = "OverpassAPI: different json formats"
description = '''Hi, I use the OverpassAPI to extract some data. Exporting them via the webinterface as geoJSON works fine but when I use an OverpassQL-link (example below) I receive a JSON-file with a different structure. How can I get a geoJSON-file with this link? http://overpass-api.de/api/interpreter?data=[out:...'''
date = "2013-07-09T12:34:00Z"
lastmod = "2013-08-06T15:41:00Z"
weight = 24126
keywords = [ "overpassapi", "json", "geojson" ]
aliases = [ "/questions/24126" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [OverpassAPI: different json formats](/questions/24126/overpassapi-different-json-formats)

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
<span id="post-24126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24126-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I use the OverpassAPI to extract some data. Exporting them via the webinterface as geoJSON works fine but when I use an OverpassQL-link (example below) I receive a JSON-file with a different structure. How can I get a geoJSON-file with this link?</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D;node(51.69,10.48,51.73,10.56)%5B">http://overpass-api.de/api/interpreter?data=[out:json];node(51.69,10.48,51.73,10.56)["highway"="street_lamp"];out;;</a></p>
<p>regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '13, 12:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-24126" class="comments-container">
<span id="24127"></span>
<div id="comment-24127" class="comment">
<div id="post-24127-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How does the structure differ? Is it a valid GeoJSON file? Did you remove the duplicated semicolon at the end of your link?</p>
</div>
<div id="comment-24127-info" class="comment-info">
<span class="comment-age">(09 Jul '13, 13:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24126-form-container" class="comment-form-container">
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

<span id="24201"></span>

<div id="answer-container-24201" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24201-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-24201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ogmios has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass returns a JSON format that is a direct representation of OSM data. This is not GeoJSON, because GeoJSON doesn't fit the OSM data structure.</p>
<p>In particular, in GeoJSON everything has a geometry, and topological incidence (like two ways sharing a node) is not represented directly. Also, GeoJSON differentiates between simple polygons and non-closed ways, which OSM does not (or again, not directly).</p>
<p>For these reasons, you need a conversion from OSM data to GeoJSON, and this is what Overpass Turbo does.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '13, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-24201" class="comments-container">
&#10;</div>
<div id="comment-tools-24201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24201-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24990"></span>

<div id="answer-container-24990" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24990-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have looked at the code that Overpass Turbo uses, in the hope that I could adapt the <a href="https://github.com/tyrasd/overpass-ide/blob/gh-pages/js/OSM4Leaflet.js">OSM4Leaflet.js</a> code to easily add standard overpass JSON queries to my map.</p>
<p>This is the sort of thing I'd ideally like to be able to do:</p>
<pre><code>var jsonLayer = new L.OSM4Leaflet(json).addTo(map);</code></pre>
<p>Unfortunately I can't understand the complexities of the code used by Overpass Turbo. Could anyone help me out? It would be very useful to have a simple method be generally known.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '13, 15:41</strong></p>
<img src="https://secure.gravatar.com/avatar/1878d01ce6631ca1cca8c339a92b4d29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tom%20Chance&#39;s gravatar image" />
<p><span>Tom Chance</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tom Chance has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24990" class="comments-container">
&#10;</div>
<div id="comment-tools-24990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24990-form-container" class="comment-form-container">
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

