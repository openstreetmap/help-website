+++
type = "question"
title = "Determine if a circle intersect roads"
description = '''Hi, I am pretty new to OSM and GIS, i wondering how can i determine if a given point(lat,lon) is in a road segment or out. Further explanation on what i want to achieve :  I have a reference point(lat1,lon1). I determine a circle with a radius of 30 meters, and a center (lat1, lon1). if want to know...'''
date = "2013-07-02T04:31:00Z"
lastmod = "2013-07-02T21:13:00Z"
weight = 23886
keywords = [ "circle", "intersection", "road" ]
aliases = [ "/questions/23886" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Determine if a circle intersect roads](/questions/23886/determine-if-a-circle-intersect-roads)

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
<span id="post-23886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23886-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am pretty new to OSM and GIS, i wondering how can i determine if a given point(lat,lon) is in a road segment or out.</p>
<p>Further explanation on what i want to achieve :</p>
<p>I have a reference point(lat1,lon1). I determine a circle with a radius of 30 meters, and a center (lat1, lon1). if want to know if this circle intersect roads.</p>
<p>Any tips will be welcome !</p>
<p>Regards,</p>
<p>Julien</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-circle" rel="tag" title="see questions tagged &#39;circle&#39;">circle</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '13, 04:31</strong></p>
<img src="https://secure.gravatar.com/avatar/d5504510885482465fb4451cd3121fbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Julzen&#39;s gravatar image" />
<p><span>Julzen</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Julzen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23886" class="comments-container">
<span id="23889"></span>
<div id="comment-23889" class="comment">
<div id="post-23889-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you please tell more</p>
<ul>
<li><p>do you want to do this rather once or rather automatically hundreds of times per second?</p></li>
<li><p>do you want an offline service with local data or rather an online service?</p></li>
</ul>
</div>
<div id="comment-23889-info" class="comment-info">
<span class="comment-age">(02 Jul '13, 08:37)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="23897"></span>
<div id="comment-23897" class="comment">
<div id="post-23897-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Roland,</p>
<p>I want to do this automatically hundreds of times and i want an offline service.</p>
<p>Hope this would help!</p>
</div>
<div id="comment-23897-info" class="comment-info">
<span class="comment-age">(02 Jul '13, 11:36)</span> <span class="comment-user userinfo">Julzen</span>
</div>
</div>
</div>
<div id="comment-tools-23886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23886-form-container" class="comment-form-container">
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

<span id="23913"></span>

<div id="answer-container-23913" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23913-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-23913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The following will give you the most accurate results:</p>
<ul>
<li>Import data into PostGIS, possibly with <code>osm2pgsql</code> but others exist; for faster import, modify osm2pgsql's style file so that only roads are imported</li>
<li>in the resulting table - called planet_osm_line if you use osm2pgsql -, add a column of type "geography" that copies the contents of the existing "geometry" type column (e.g. <code>alter table planet_osm_line add column mygeographycolumn geography; update planet_osm_line set mygeographycolumn=way;</code>)</li>
<li>create a spatial index on the "geography" column</li>
<li>now query the database like this: <code>select name,osm_id,highway from planet_osm_line where ST_DWITHIN(mygeographycolumn, ST_SETSRID(ST_POINT(lon1,lat1),4326)::geography, dist)</code> (replace lon1, lat1, dist by your coordinates and radius of circle).</li>
</ul>
<p>You can skip the whole "convert to geography" bit and use a suitable projection for your area of interest which will then usually yield results in the +/- 1 metre range; if you go with the default projection of Spherical Mercator and your area of interest is far away from the Equator you will be searching ellipses, not circles.</p>
<p>SQL statements in this answer written from memory - not syntax proofed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '13, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23913" class="comments-container">
&#10;</div>
<div id="comment-tools-23913" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23913-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23901"></span>

<div id="answer-container-23901" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23901-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So you have the OSM road network and want to ask for some coordinate whether a road is (less than) 30 meters away?</p>
<p>The relevant GIS terminology would probably be "buffering" (this is drawing the circle of 30m around your point) and "intersection testing" (to see whether a road intersects the buffer around the point).</p>
<p>There are a few options for choosing software for that task.</p>
<p>You could use a Desktop GIS like Quantum GIS, and then script your analysis with e.g. python scripting. This will have a steep learning curve if you never used a GIS before.</p>
<p>You could import all OSM data into a PostGIS DB and then make the spatial queries using SQL, this would work better if you had a "working knowledge" of SQL.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '13, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-23901" class="comments-container">
&#10;</div>
<div id="comment-tools-23901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23901-form-container" class="comment-form-container">
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

