+++
type = "question"
title = "Using OGC Polygon from OSM Export"
description = '''I have some OSM data downloaded by someone else. The geom is in text e.g.  POLYGON ((5585434.5396439433 2454059.8880860955, 5585440.2817584425... I imported the data into SQL Server 2008 R2 and I need to convert the OSM text data to Geometry data in SQL Server using the OGC methods provided by the M...'''
date = "2013-07-17T19:02:00Z"
lastmod = "2013-07-18T20:15:00Z"
weight = 24324
keywords = [ "srid", "sqlserver", "ogc" ]
aliases = [ "/questions/24324" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using OGC Polygon from OSM Export](/questions/24324/using-ogc-polygon-from-osm-export)

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
<span id="post-24324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24324-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some OSM data downloaded by someone else. The geom is in text e.g. POLYGON ((5585434.5396439433 2454059.8880860955, 5585440.2817584425...</p>
<p>I imported the data into SQL Server 2008 R2 and I need to convert the OSM text data to Geometry data in SQL Server using the OGC methods provided by the Microsoft server.</p>
<p>Has anyone done this already and could you give me some pointers? I'm new to SQL spatial so keep it simple.</p>
<p>I think my first task is to figure out the SRID that they source data is in. The POLYGON above is somewhere near -120 long, 35 lat +/- 2. I want the final geom object to have a lat/long SRID 4236.</p>
<p>What SRID would have been used on the initial export from OSM? The text above could have been the result of someone changing the OSM data so I'll have to research that.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-srid" rel="tag" title="see questions tagged &#39;srid&#39;">srid</span> <span class="post-tag tag-link-sqlserver" rel="tag" title="see questions tagged &#39;sqlserver&#39;">sqlserver</span> <span class="post-tag tag-link-ogc" rel="tag" title="see questions tagged &#39;ogc&#39;">ogc</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '13, 19:02</strong></p>
<img src="https://secure.gravatar.com/avatar/59471706320680735692ffe86da3d247?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rheitzman&#39;s gravatar image" />
<p><span>rheitzman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rheitzman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24324" class="comments-container">
&#10;</div>
<div id="comment-tools-24324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24324-form-container" class="comment-form-container">
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

<span id="24326"></span>

<div id="answer-container-24326" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24326-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM data will nearly always be in either WGS84 (<a href="http://spatialreference.org/ref/epsg/4326/">ESPG:4326</a> - I presume 4236 in your question is a typo) or Spherical Mercator (Google Maps) projections. The values in your POLYGON sample appear to be in the latter (EPSG:900913 or EPSG:3857 ) as they are clearly not in lat/lon units and are most likely to be in metres.</p>
<p>The POLYGON data is in <a href="http://en.wikipedia.org/wiki/Well-known_text">WKT format</a>, so you just need a function which converts WKT to the internal geoemetry representation. A 5 second google search suggests this might be what you need: <a href="http://msdn.microsoft.com/en-us/library/bb933823.aspx">STGeomfromText()</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '13, 19:28</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-24326" class="comments-container">
<span id="24366"></span>
<div id="comment-24366" class="comment">
<div id="post-24366-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks!<br />
</p>
<p>FYI Other readers be aware that the spatial extension names are case sensitive in SQL Server - something we are not used to. STGeomFromText()</p>
</div>
<div id="comment-24366-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 20:15)</span> <span class="comment-user userinfo">rheitzman</span>
</div>
</div>
</div>
<div id="comment-tools-24326" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24326-form-container" class="comment-form-container">
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

