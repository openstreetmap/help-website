+++
type = "question"
title = "How to calculate rooftop area?"
description = '''Hello! I have a following issue, I need to calculate the area of a rooftop of a building that I have searched for (I am considering only flat roofs). By querying OSM through Nominatim https://nominatim.openstreetmap.org/search/${query}format=json&amp;amp;addressdetails=1&amp;amp;limit=1&amp;amp;polygon_svg=1 I ...'''
date = "2020-10-26T18:10:00Z"
lastmod = "2020-10-26T18:20:00Z"
weight = 77253
keywords = [ "calulation", "nominatim", "rooftop", "area" ]
aliases = [ "/questions/77253" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to calculate rooftop area?](/questions/77253/how-to-calculate-rooftop-area)

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
<span id="post-77253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77253-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! I have a following issue, I need to calculate the area of a rooftop of a building that I have searched for (I am considering only flat roofs). By querying OSM through Nominatim <a href="https://nominatim.openstreetmap.org/search/$%7Bquery%7Dformat=json&amp;addressdetails=1&amp;limit=1&amp;polygon_svg=1">https://nominatim.openstreetmap.org/search/${query}format=json&amp;addressdetails=1&amp;limit=1&amp;polygon_svg=1</a> I got a result with the coordinates of the nodes of the building. And as I have understand I need to use lat and long of that nodes and calculate the area of rooftop (received polygon). Can you suggest some alternate (easier) methods for this task (is there a possibility to query OSM and get that area without calculating it)?</p>
<p>For example after querying I got this result: address: {house_number: "228", road: "Sõpruse pst", quarter: "Мустамяе", suburb: "Mustamäe linnaosa", city: "Tallinn", …} boundingbox: (4) ["59.400098", "59.4003983", "24.6893501", "24.6909638"] class: "building" display_name: "228, Sõpruse pst, Мустамяе, Mustamäe linnaosa, Tallinn, Таллин, Уезд Харьюмаа, 13414, Estonia" importance: 0.22100000000000003 lat: "59.400248149999996" licence: "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright"</a> lon: "24.690156937993393" osm_id: 26871853 osm_type: "way" place_id: 93502864 svg: "M 24.6893501 -59.4002007 L 24.6893999 -59.400098 24.6909638 -59.4002956 24.6909274 -59.4003705 24.6909139 -59.4003983 Z" type: "yes"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-calulation" rel="tag" title="see questions tagged &#39;calulation&#39;">calulation</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-rooftop" rel="tag" title="see questions tagged &#39;rooftop&#39;">rooftop</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '20, 18:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a167730b5d7d1652ae251f4d48c1141e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armankulbek&#39;s gravatar image" />
<p><span>armankulbek</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armankulbek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77253" class="comments-container">
&#10;</div>
<div id="comment-tools-77253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77253-form-container" class="comment-form-container">
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

<span id="77254"></span>

<div id="answer-container-77254" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77254-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim imports full polygons for streets, landuse, cities, countries. For addresses Nominatim only imports the center point it doesn't import the building shape itself and thus can't return the size. If a building=yes is the address then during the import a center point is calculated and only that imported. When Nominatim returns a bounding box it's most likely calculated, e.g. "50 meter box around this center point". <a href="https://github.com/osm-search/Nominatim/blob/master/lib/PlaceLookup.php#L550">https://github.com/osm-search/Nominatim/blob/master/lib/PlaceLookup.php#L550</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '20, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-77254" class="comments-container">
&#10;</div>
<div id="comment-tools-77254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77254-form-container" class="comment-form-container">
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

