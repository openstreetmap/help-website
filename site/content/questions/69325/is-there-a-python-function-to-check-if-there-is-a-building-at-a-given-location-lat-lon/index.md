+++
type = "question"
title = "Is there a python function to check if there is a building at a given location (lat, lon)?"
description = '''Hey guys, I am looking for a function in python that has only latitude and longitudes as input values and gives me the landuse as output value. It is basically enough to know if the location is in a building or not. The type of building is not so important. I already checked in the osmnx library bas...'''
date = "2019-05-26T15:20:00Z"
lastmod = "2019-05-30T22:30:00Z"
weight = 69325
keywords = [ "python", "osmpythontools", "lookup", "osmnx", "latitude" ]
aliases = [ "/questions/69325" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a python function to check if there is a building at a given location (lat, lon)?](/questions/69325/is-there-a-python-function-to-check-if-there-is-a-building-at-a-given-location-lat-lon)

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
<span id="post-69325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69325-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys, I am looking for a function in python that has only latitude and longitudes as input values and gives me the landuse as output value. It is basically enough to know if the location is in a building or not. The type of building is not so important. I already checked in the osmnx library based on Open Street Map, but couldn't find anything that matches my question. But maybe osmnx already offers the solution and I did not see it.</p>
<p>The solution should be something like: <strong>landuse = ??function??(lat, lon)</strong> And than the output might be "residential_building" or "agricultural_open_area".</p>
<p>I am glad for any helps Greetings Chris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-osmpythontools" rel="tag" title="see questions tagged &#39;osmpythontools&#39;">osmpythontools</span> <span class="post-tag tag-link-lookup" rel="tag" title="see questions tagged &#39;lookup&#39;">lookup</span> <span class="post-tag tag-link-osmnx" rel="tag" title="see questions tagged &#39;osmnx&#39;">osmnx</span> <span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '19, 15:20</strong></p>
<img src="https://secure.gravatar.com/avatar/03972baf37a3435f95c80a4635c5fa11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris_Ali_del_Vari&#39;s gravatar image" />
<p><span>Chris_Ali_de...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris_Ali_del_Vari has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69325" class="comments-container">
&#10;</div>
<div id="comment-tools-69325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69325-form-container" class="comment-form-container">
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

<span id="69326"></span>

<div id="answer-container-69326" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69326-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could do it with Overpass (same as the web site does when you click somewhere with the question mark icon) though if you'd like to run this more frequently, using Overpass runs the danger of making the server unusable for others. Therefore you'll want to load the OSM data into your own PostGIS database with osm2pgsql. Then you can make queries like</p>
<p>SELECT "natural",landuse,building FROM planet_osm_polygon WHERE ST_Contains(way, ST_MakePoint(lon,lat))</p>
<p>(note that for this query to work, you need to run osm2pgsql with -l option, or you might need a ST_Transform around your ST_MakePoint).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '19, 17:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-69326" class="comments-container">
<span id="69379"></span>
<div id="comment-69379" class="comment">
<div id="post-69379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank You for the fast answer. I am sure the way You described works well. Unfortunatly I don't know much about Overpass and don't know how to integrate it into Python, so I am trying a different approach with a downloaded .shp file from the city and the sjoin command of the geopanda tools. Got the approach from a Youtube Tutorial and it seems to work for me as well: <a href="https://www.youtube.com/watch?v=HzPSVwyP2Y0">https://www.youtube.com/watch?v=HzPSVwyP2Y0</a></p>
</div>
<div id="comment-69379-info" class="comment-info">
<span class="comment-age">(30 May '19, 22:30)</span> <span class="comment-user userinfo">Chris_Ali_de...</span>
</div>
</div>
</div>
<div id="comment-tools-69326" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69326-form-container" class="comment-form-container">
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

