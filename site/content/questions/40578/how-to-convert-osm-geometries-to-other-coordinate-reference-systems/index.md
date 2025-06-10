+++
type = "question"
title = "How to convert OSM geometries to other coordinate reference systems?"
description = '''Hi everyone, I haven&#x27;t found any useable source on the web which tells me how to convert data from OSM which I have imported with osm2pgsql into my postGIS database to another coordinate reference Systems (CRS) like UTM or lat/Long. How can I do this task with the integrated functions in the postGIS...'''
date = "2015-01-24T20:47:00Z"
lastmod = "2015-01-25T00:44:00Z"
weight = 40578
keywords = [ "conversion", "postgis", "coordinates", "osm2pgsql" ]
aliases = [ "/questions/40578" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert OSM geometries to other coordinate reference systems?](/questions/40578/how-to-convert-osm-geometries-to-other-coordinate-reference-systems)

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
<span id="post-40578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40578-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>I haven't found any useable source on the web which tells me how to convert data from OSM which I have imported with osm2pgsql into my postGIS database to another coordinate reference Systems (CRS) like UTM or lat/Long. How can I do this task with the integrated functions in the postGIS database or vice versa, how to convert data from another database with e.g. UTM coordinates to the format OSM is using?</p>
<p>Thanks, Stefan aka nordie69</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-conversion" rel="tag" title="see questions tagged &#39;conversion&#39;">conversion</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '15, 20:47</strong></p>
<img src="https://secure.gravatar.com/avatar/194bd6ccac093a55e95c4b66f9baadf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nordie69&#39;s gravatar image" />
<p><span>nordie69</span><br />
<span class="score" title="45 reputation points">45</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nordie69 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40578" class="comments-container">
&#10;</div>
<div id="comment-tools-40578" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40578-form-container" class="comment-form-container">
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

<span id="40587"></span>

<div id="answer-container-40587" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40587-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-40587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unless you have specified a different CRS upon import (using the <code>-l</code> or <code>-E</code>), your import is in EPSG:3857 a.k.a EPSG:900913. To convert to a different CRS, use the PostGIS ST_Transform method:</p>
<pre><code>SELECT name, ST_AsText(ST_Transform(way, 4326))
FROM planet_osm_point
WHERE amenity=&#39;pub&#39;;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '15, 00:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-40587" class="comments-container">
&#10;</div>
<div id="comment-tools-40587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40587-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40588"></span>

<div id="answer-container-40588" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40588-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use standard PostGIS function <code>st_transform(geometry,EPSG#)</code>. Using <code>ST_Setsrid</code> is useful to ensure the DB knows which co-ordinate system it is using. It is relatively easy to alter the standard table to add additional geometry columns, but the tables may not then be suitable for updates.</p>
<p>osm2pgsql allows the specification of the desired co-ordinate system as a flag on input. I'd use this if working predominantly in one co-ordinate system.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '15, 00:44</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Mar '15, 16:08</strong> </span></p>
</div>
</div>
<div id="comments-container-40588" class="comments-container">
&#10;</div>
<div id="comment-tools-40588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40588-form-container" class="comment-form-container">
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

