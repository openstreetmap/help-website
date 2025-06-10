+++
type = "question"
title = "OSM2PGSQL coordinates"
description = '''Hello! I have all the XML data into PostGres DB using OSM2PGSQL. I get the coordinates of a node and what I get is the next: 471196104, -858385498 (it is in Washington) I dont know the format of the this coordinates and how to convert it. I would like to have coordinates in a &quot;normal&quot; format, I mean...'''
date = "2012-03-19T18:34:00Z"
lastmod = "2012-03-19T19:12:00Z"
weight = 11336
keywords = [ "osm2pgsql", "coordinates" ]
aliases = [ "/questions/11336" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSM2PGSQL coordinates](/questions/11336/osm2pgsql-coordinates)

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
<span id="post-11336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11336-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>I have all the XML data into PostGres DB using OSM2PGSQL. I get the coordinates of a node and what I get is the next:</p>
<p>471196104, -858385498 (it is in Washington)</p>
<p>I dont know the format of the this coordinates and how to convert it. I would like to have coordinates in a "normal" format, I mean something like this: 41.347187,2.0309942</p>
<p>Thank you for the help in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '12, 18:34</strong></p>
<img src="https://secure.gravatar.com/avatar/15d8349c5774d9702b147a72c3b9fdf9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aruizga7&#39;s gravatar image" />
<p><span>aruizga7</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aruizga7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11336" class="comments-container">
&#10;</div>
<div id="comment-tools-11336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11336-form-container" class="comment-form-container">
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

<span id="11338"></span>

<div id="answer-container-11338" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11338-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aruizga7 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The coordinates you got is in spherical mercator projection. osm2pgsql transforms all the coordinates to mercator before inserting them to the database. To get the coordinates in another projection use the function <a href="http://www.postgis.org/documentation/manual-1.5/ST_Transform.html">ST_Transform</a> in postgis.</p>
<p>The standard latlon coordinates you want is <a href="http://spatialreference.org/ref/epsg/4326/">EPSG:4326</a> and spherical mercator is <a href="http://spatialreference.org/ref/sr-org/6864/">EPSG:3857</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '12, 19:12</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11338" class="comments-container">
&#10;</div>
<div id="comment-tools-11338" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11338-form-container" class="comment-form-container">
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

