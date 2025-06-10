+++
type = "question"
title = "Place not found (Geofabrik OSM Inspector)"
description = '''Hi, Geofabrik OSM Inspector shows an error: &quot;Place not found&quot; for houses. There is an multipoligon (neighbourhood) with tags: landuse=residential name=коттеджный посёлок «Серебряные Родники» place=neighbourhood type=multipolygon Houses inside this place with tags: addr:housenumber=5 addr:neighbourho...'''
date = "2022-12-16T06:35:00Z"
lastmod = "2023-01-11T06:57:00Z"
weight = 86350
keywords = [ "geofabrik", "place", "help", "osminspector", "address" ]
aliases = [ "/questions/86350" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Place not found (Geofabrik OSM Inspector)](/questions/86350/place-not-found-geofabrik-osm-inspector)

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
<span id="post-86350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86350-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, <a href="https://tools.geofabrik.de/osmi/?view=addresses&amp;lon=37.43563&amp;lat=55.92561&amp;zoom=17&amp;baselayer=Geofabrik%20Standard&amp;overlays=entrances_deprecated%2Centrances%2Cno_addr_street%2Cstreet_not_found%2Cplace_not_found%2Cnodes_with_addresses_interpolated%2Cinterpolation%2Cinterpolation_errors%2Cnearest_areas%2Caddrx_on_nonclosed_way">Geofabrik OSM Inspector shows an error</a>: "Place not found" for houses.</p>
<p>There is an <a href="https://www.openstreetmap.org/relation/4115672">multipoligon (neighbourhood)</a> with tags:<br />
landuse=residential<br />
name=коттеджный посёлок «Серебряные Родники»<br />
place=neighbourhood<br />
type=multipolygon</p>
<p><a href="https://www.openstreetmap.org/way/187174919">Houses</a> inside this place with tags:<br />
addr:housenumber=5<br />
addr:neighbourhood=Вашутино<br />
addr:place=коттеджный посёлок «Серебряные Родники»<br />
building=house</p>
<p>I tried to remove tag addr:neighbourhood (leave only addr:place and addr:housenumber), still the error remains. I can't figure out what's going on, maybe you have an idea?</p>
<hr />
<p>I mean, I have key addr:place on buildings corresponds to name to neighbourhood, but the error still occurs. I don't know what's the problem.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-osminspector" rel="tag" title="see questions tagged &#39;osminspector&#39;">osminspector</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '22, 06:35</strong></p>
<img src="https://secure.gravatar.com/avatar/f31ec9174ed009ba0892937c184d5a29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grass-snake&#39;s gravatar image" />
<p><span>Grass-snake</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grass-snake has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-86350" class="comments-container">
&#10;</div>
<div id="comment-tools-86350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86350-form-container" class="comment-form-container">
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

<span id="86355"></span>

<div id="answer-container-86355" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86355-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim found <a href="https://www.openstreetmap.org/search?query=5%20%D0%92%D0%B0%D1%88%D1%83%D1%82%D0%B8%D0%BD%D0%BE#map=17/59.43508/40.20039">it</a>, so maybe some issue with Geofabrik? Different <a href="https://tools.geofabrik.de/osmi/?view=addresses&amp;lon=40.20039&amp;lat=59.43508&amp;zoom=17&amp;baselayer=Geofabrik%20Standard&amp;overlays=entrances_deprecated%2Centrances%2Cno_addr_street%2Cstreet_not_found%2Cplace_not_found%2Cnodes_with_addresses_interpolated%2Cinterpolation%2Cinterpolation_errors%2Cnearest_areas%2Caddrx_on_nonclosed_way">location</a> maybe? I am just guessing since I don't understand russian, just copy and paste stuff.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '22, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/d7e115e2e912ad2d50353b2fbd153cab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kucai&#39;s gravatar image" />
<p><span>kucai</span><br />
<span class="score" title="86 reputation points">86</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kucai has one accepted answer">9%</span> </br></br></p>
</div>
</div>
<div id="comments-container-86355" class="comments-container">
&#10;</div>
<div id="comment-tools-86355" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86355-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86484"></span>

<div id="answer-container-86484" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86484-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Wow, I figured out what the problem is!<br />
Information for those who will face the same problem and find this topic.</p>
<p>Sometimes addresses do not contain a street name. Some addresses instead of the street name contain some other elements "‹name of some territory›, ‹house number›" (for example, village A, house 1). This may be the name of a neighbourhood, settlement, territorial zone or other object.</p>
<p>If you use such a scheme, then on houses or POI, you usually need to add only tags addr:place= <em>and addr:housenumber=</em> (possibly addr:postcode=* if required). But with the designation of territory boundaries, all conditions must be met:</p>
<ol>
<li>Be sure to have a point with the designation of the territory. If you just drew borders, but did not create a node, then Nominatim will determine the address, but the Geofabrik OSM Inspector (validator) will generate an error.<br />
<em>That was exactly what my problem was.</em></li>
<li>Of course, this point must be inside the (multi-)polygon (even if it consists of several outer borders or there are inner parts, so that it must be inside).</li>
<li>There should be only one point for one border (have not figured it out yet).</li>
<li>The same place= <em>and name=</em> tags must be present on the border of the territory and on the node. For example, if tags place=neighbourhood and name=Name are indicated on the border, then the same values must be indicated on the point up to a character (otherwise it will not work).</li>
<li>Only the place and name tags (and type=multipolygon for the multipolygon) should be on the border. All other tags (postal_code, wikipedia/wikidata, population, etc. just need to be added to the node).</li>
</ol>
<p>Recommendation: Don't use tags place= <em>and landuse=</em> on the same feature. If a particular land use covers the entire area, just create a new polygon and list only the landuse= <em>(without name=</em> tag). Specify place= <em>and name=</em> tags on the separate (multi-)polygon. Otherwise, the title on some renders (including OSM Carto) may be duplicated.</p>
<p>If the boundary consists few outer polygon contours, you can add landuse= <em>to each contour and then add them to the multipolygon. Important: if the boundary consists of several unclosed lines, then you need to combine them into the multipolygon, then add the landuse=</em> tag on the multipolygon. Add these lines for the boundary. Do not add multipolygon to a multipolygon, only lines.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '23, 06:57</strong></p>
<img src="https://secure.gravatar.com/avatar/f31ec9174ed009ba0892937c184d5a29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grass-snake&#39;s gravatar image" />
<p><span>Grass-snake</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grass-snake has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-86484" class="comments-container">
&#10;</div>
<div id="comment-tools-86484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86484-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

