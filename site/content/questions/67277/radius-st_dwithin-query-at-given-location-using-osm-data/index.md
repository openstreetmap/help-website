+++
type = "question"
title = "Radius ST_DWITHIN query at given location using OSM data"
description = '''I imported OSM data using osm2pgsql and querying it using postgis extentsion but struggling to get some decent output.  I would like to query for ATMs within 500 meters at location long/lat (-0.1470123 51.5149226) (London) Here is my query SELECT name, ST_AsText(ST_Transform(way,4326)) FROM planet_o...'''
date = "2018-12-19T14:03:00Z"
lastmod = "2018-12-19T14:03:00Z"
weight = 67277
keywords = [ "osm", "osm2pgsql", "postgis" ]
aliases = [ "/questions/67277" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Radius ST_DWITHIN query at given location using OSM data](/questions/67277/radius-st_dwithin-query-at-given-location-using-osm-data)

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
<span id="post-67277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67277-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I imported OSM data using osm2pgsql and querying it using postgis extentsion but struggling to get some decent output.</p>
<p>I would like to query for ATMs within 500 meters at location long/lat (-0.1470123 51.5149226) (London) Here is my query</p>
<p>SELECT name, ST_AsText(ST_Transform(way,4326)) FROM planet_osm_point WHERE amenity = 'atm' AND ST_DWITHIN(way, ST_TRANSFORM(ST_SETSRID(ST_MAKEPOINT(-0.1470123,51.5149226),4326),900913), 500);</p>
<p>Can you help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '18, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ac18356019d6ebeea5c9c8e33414ed74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrparadox&#39;s gravatar image" />
<p><span>mrparadox</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrparadox has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67277" class="comments-container">
&#10;</div>
<div id="comment-tools-67277" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67277-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

