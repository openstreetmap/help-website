+++
type = "question"
title = "Why do osm2pgsql and Mapnik use spherical projection 900913?"
description = '''Hi I followed the guide http://weait.com/content/build-your-own-openstreetmap-server on both an Ubuntu server and my Mac, nice guide. The guide includes how to set SRID 900913 on the PostGIS database, and mapnik seems to default to this, too. This might be a nooby question for people from a GIS back...'''
date = "2011-07-09T21:39:00Z"
lastmod = "2011-07-09T23:20:00Z"
weight = 6256
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/6256" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why do osm2pgsql and Mapnik use spherical projection 900913?](/questions/6256/why-do-osm2pgsql-and-mapnik-use-spherical-projection-900913)

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
<span id="post-6256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6256-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I followed the guide <a href="http://weait.com/content/build-your-own-openstreetmap-server">http://weait.com/content/build-your-own-openstreetmap-server</a> on both an Ubuntu server and my Mac, nice guide. The guide includes how to set SRID 900913 on the PostGIS database, and mapnik seems to default to this, too.</p>
<p>This might be a nooby question for people from a GIS background, but when I first did some queries on the data, the output confused me a lot and only once I figured out ST_Transform(way,94326) it made sense (and gave me latitude / longitude values I find useful).</p>
<p>Why is the data not stored in WGS84 (94326) by default? Are there accuracy considerations? Or is it just a convention adopted by tile renderers like Mapnik, since the map projection is probably 900913?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '11, 21:39</strong></p>
<img src="https://secure.gravatar.com/avatar/9cd78a22b04f5104b7051119257a0d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rdrey&#39;s gravatar image" />
<p><span>rdrey</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rdrey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6256" class="comments-container">
&#10;</div>
<div id="comment-tools-6256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6256-form-container" class="comment-form-container">
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

<span id="6257"></span>

<div id="answer-container-6257" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6257-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-6257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rdrey has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the central OSM database, data is indeed stored in EPSG:4326, and the same is true if you load our data into a non-rendering-optimised database e.g. with Osmosis. Only osm2pgsql and, by extension, our Mapnik style default to spherical Mercator because that's what is required for tile rendering, and not having to reproject data when rendering tiles gives a performance benefit.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '11, 22:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-6257" class="comments-container">
<span id="6258"></span>
<div id="comment-6258" class="comment">
<div id="post-6258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks! Makes sense. I should probably follow an osmosis guide the next time!</p>
</div>
<div id="comment-6258-info" class="comment-info">
<span class="comment-age">(09 Jul '11, 22:52)</span> <span class="comment-user userinfo">rdrey</span>
</div>
</div>
<span id="6259"></span>
<div id="comment-6259" class="comment">
<div id="post-6259-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I should have added that you can use the -l (ell) parameter with osm2pgsql and it will generate EPSG:4326 geometries.</p>
</div>
<div id="comment-6259-info" class="comment-info">
<span class="comment-age">(09 Jul '11, 23:20)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-6257" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6257-form-container" class="comment-form-container">
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

