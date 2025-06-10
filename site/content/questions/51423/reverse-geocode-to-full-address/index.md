+++
type = "question"
title = "Reverse geocode to full address"
description = '''Using Nominatim, I&#x27;m able to retrieve a full address from a reverse search. I click in the map, generating a lat/lon value for my click and it will bring back a full address, as such:  http://nominatim.openstreetmap.org/reverse.php?format=html&amp;amp;lat=53.1072166918934&amp;amp;lon=-2.3291015625&amp;amp;zoom=...'''
date = "2016-08-15T14:54:00Z"
lastmod = "2019-05-30T10:43:00Z"
weight = 51423
keywords = [ "osrm", "nominatim", "geocoding" ]
aliases = [ "/questions/51423" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse geocode to full address](/questions/51423/reverse-geocode-to-full-address)

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
<span id="post-51423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51423-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using Nominatim, I'm able to retrieve a full address from a reverse search. I click in the map, generating a lat/lon value for my click and it will bring back a full address, as such:</p>
<p><a href="http://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=53.1072166918934&amp;lon=-2.3291015625&amp;zoom="><code>http://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=53.1072166918934&amp;lon=-2.3291015625&amp;zoom=</code></a></p>
<p>If I query either raw OSM data (<a href="http://www.openstreetmap.org/api/0.6/way/25958840">HERE</a>) I'm only able to see the street name. Where is OSM getting the rest of the data from? Am I able to achieve a similar level of depth?</p>
<p>I'm currently running a web server hosting <code>OSRM</code> and a C# application feeding in queries, but I'm only ever able to get a <code>street name</code> back instead of a full address...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Aug '16, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a7cb490555f288a4bc1232439157dc1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesGould&#39;s gravatar image" />
<p><span>JamesGould</span><br />
<span class="score" title="196 reputation points">196</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesGould has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-51423" class="comments-container">
&#10;</div>
<div id="comment-tools-51423" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51423-form-container" class="comment-form-container">
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

<span id="51426"></span>

<div id="answer-container-51426" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51426-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-51426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer is <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a>.</p>
<p>Nominatim builds an address hierarchy using information from the element's <a href="https://wiki.openstreetmap.org/wiki/Addresses">address tags</a> and <a href="https://wiki.openstreetmap.org/wiki/Relation:associatedStreet">associatedStreet relations</a>, <a href="https://wiki.openstreetmap.org/wiki/Key:place">places</a> in the element's proximity, <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">administrative boundaries</a> enclosing the element and so on. Some of these steps are explained at the <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Development_overview">development overview</a>.</p>
<p>If you open your link and click on <em>details</em> you can <a href="https://nominatim.openstreetmap.org/details.php?place_id=65040303">see the address hierarchy</a> Nominatim has built and which other OSM elements were used to create this hierarchy.</p>
<p>Also note that there are some other <a href="https://wiki.openstreetmap.org/wiki/Search_engines">geocoders for OSM</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '16, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '16, 19:04</strong> </span></p>
</div>
</div>
<div id="comments-container-51426" class="comments-container">
<span id="51433"></span>
<div id="comment-51433" class="comment">
<div id="post-51433-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I also thought that Nominatim included a few other sources than just pure OSM data (e.g. Tiger address data)</p>
</div>
<div id="comment-51433-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 09:50)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="51434"></span>
<div id="comment-51434" class="comment">
<div id="post-51434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, for the US Nominatim also uses Tiger address data as far as I know. Maybe similar additional data is used for some other countries. I still haven't found any good documentation for all this stuff.</p>
</div>
<div id="comment-51434-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 09:53)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51426-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69374"></span>

<div id="answer-container-69374" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69374-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-69374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>SELECT string_agg( place,&#39;,&#39;) as place FROM (
SELECT name AS PLACE, SUBSTRING(planet_osm_polygon.admin_level FROM &#39;[0-9]{1,2}&#39;)::INT AS admin_level_int
FROM
planet_osm_polygon
WHERE
boundary = &#39;administrative&#39; AND
ST_Intersects(&#39;SRID=4326;POINT(78.44131 17.51671)&#39;::geometry, way)
ORDER BY admin_level_int desc
) AS geocoder</code></pre>
<p><br />
output: Ward 129 Suraram, Greater Hyderabad Municipal Corporation North Zone, Hyderabad, Medchal-Malkajgiri District, Telangana<br />
if you get mixed SRID geometries error change 'way' as ST_Transform(way,4326)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '19, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/c8232e813e7b56f3d5e3db75cf6ad7ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Prasad%20Raju%20Vegesna&#39;s gravatar image" />
<p><span>Prasad Raju ...</span><br />
<span class="score" title="0 reputation points">0</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Prasad Raju Vegesna has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-69374" class="comments-container">
&#10;</div>
<div id="comment-tools-69374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69374-form-container" class="comment-form-container">
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

