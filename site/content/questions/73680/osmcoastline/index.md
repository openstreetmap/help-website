+++
type = "question"
title = "osmcoastline"
description = '''Hello, I download denmark-latest.osm.pbf from geofabrik, then I run osmcoastline: osmcoastline -o coastline.db denmark-latest.osm.pbf  Then convert to shape : ogr2ogr -f &quot;ESRI Shapefile&quot; land_polygons.shp coastline.db land_polygons Then I view the land_polygons.shp in qgis, but now half of Denmark i...'''
date = "2020-03-22T17:52:00Z"
lastmod = "2020-03-24T07:33:00Z"
weight = 73680
keywords = [ "osmcoastline" ]
aliases = [ "/questions/73680" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmcoastline](/questions/73680/osmcoastline)

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
<span id="post-73680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73680-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I download denmark-latest.osm.pbf from geofabrik, then I run osmcoastline: <strong>osmcoastline -o coastline.db denmark-latest.osm.pbf</strong></p>
<p>Then convert to shape : <strong>ogr2ogr -f "ESRI Shapefile" land_polygons.shp coastline.db land_polygons</strong></p>
<p>Then I view the land_polygons.shp in qgis, but now half of Denmark is gone.</p>
<p>What have I done wrong ??</p>
<p>Best regards Håvard</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmcoastline" rel="tag" title="see questions tagged &#39;osmcoastline&#39;">osmcoastline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '20, 17:52</strong></p>
<img src="https://secure.gravatar.com/avatar/db5b7b23235694ee1b9ef036a4393416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HaavardHolm&#39;s gravatar image" />
<p><span>HaavardHolm</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HaavardHolm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73680" class="comments-container">
&#10;</div>
<div id="comment-tools-73680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73680-form-container" class="comment-form-container">
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

<span id="73692"></span>

<div id="answer-container-73692" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73692-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally you can not run OSMCoastline on extracts. OSMCoastline assembles ways into continuous coastline linestrings and then into land and water polygons. But if the coastline is not closed, it can't do that. This might work if your extract only contains an island, but Denmark isn't an island, so you can't determine its land area from the coastline.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '20, 07:54</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-73692" class="comments-container">
<span id="73697"></span>
<div id="comment-73697" class="comment">
<div id="post-73697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thanks again !</p>
<p>Best regards, Håvard</p>
</div>
<div id="comment-73697-info" class="comment-info">
<span class="comment-age">(23 Mar '20, 10:23)</span> <span class="comment-user userinfo">HaavardHolm</span>
</div>
</div>
<span id="73719"></span>
<div id="comment-73719" class="comment">
<div id="post-73719-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are there other ways to separate the coastline for each country ?</p>
<p>I notice the webpage : <a href="https://osmdata.openstreetmap.de/data/land-polygons.html,">https://osmdata.openstreetmap.de/data/land-polygons.html,</a> however I need to split into separate country. Could administrative borders be used ?</p>
<p>Best regards Håvard</p>
</div>
<div id="comment-73719-info" class="comment-info">
<span class="comment-age">(24 Mar '20, 07:33)</span> <span class="comment-user userinfo">HaavardHolm</span>
</div>
</div>
</div>
<div id="comment-tools-73692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73692-form-container" class="comment-form-container">
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

