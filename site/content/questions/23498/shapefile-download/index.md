+++
type = "question"
title = "Shapefile download"
description = '''How can I download a .shp of South Carolina, US? Or how can I convert to .shp one of the the downloads from http://download.geofabrik.de/north-america/us/south-carolina.html where they have the options for .osm.pbf or .osm.bz2. Thanks!'''
date = "2013-06-18T19:10:00Z"
lastmod = "2013-06-18T19:29:00Z"
weight = 23498
keywords = [ "shapefile" ]
aliases = [ "/questions/23498" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Shapefile download](/questions/23498/shapefile-download)

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
<span id="post-23498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23498-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I download a .shp of South Carolina, US? Or how can I convert to .shp one of the the downloads from <a href="http://download.geofabrik.de/north-america/us/south-carolina.html">http://download.geofabrik.de/north-america/us/south-carolina.html</a> where they have the options for .osm.pbf or .osm.bz2. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '13, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/2c28dd824f32bd54d6a79e50d6c2a732?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="QuisEs99&#39;s gravatar image" />
<p><span>QuisEs99</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="QuisEs99 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23498" class="comments-container">
&#10;</div>
<div id="comment-tools-23498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23498-form-container" class="comment-form-container">
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

<span id="23499"></span>

<div id="answer-container-23499" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23499-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-23499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try <a href="http://extract.bbbike.org">http://extract.bbbike.org</a> where you can request a shapefile for a custom area. Alternatively, you can produce shapefiles from .osm.pbf by</p>
<ul>
<li>using the osmjs program that comes with osmium or</li>
<li>using the OSM OGR driver (e.g. from ogr2ogr) to convert to shape or</li>
<li>importing the file into a PostGIS database with imposm or osm2pgsql, and then export shapefile from there with pgsql2shp</li>
</ul>
<p>Having said that, I am the guy running download.geofabrik.de and I'm working on adding shape files for US states so if you can wait for a couple more days there's likely going to be a download option for .shp.zip there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '13, 19:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23499" class="comments-container">
<span id="23500"></span>
<div id="comment-23500" class="comment">
<div id="post-23500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I'll try what you've got and post back if I need more help otherwise I will continue to watch your website for that download option. I appreciate the help!</p>
</div>
<div id="comment-23500-info" class="comment-info">
<span class="comment-age">(18 Jun '13, 19:29)</span> <span class="comment-user userinfo">QuisEs99</span>
</div>
</div>
</div>
<div id="comment-tools-23499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23499-form-container" class="comment-form-container">
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

