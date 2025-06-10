+++
type = "question"
title = "Mapnik 2.1.x + OSM + Postgis 2 + PostgreSQL 9.2 + Python26 = Only shorelines and no features"
description = '''I&#x27;m having issues generating an OSM map with generate_image.py with Mapnik. I am using PostgreSQL 9.2 with PostGIS 2 and Mapnik 2.1.x and python26 I am also on Oracle Enterpise Linux 6, which makes things a little less straightforward compared to Ubuntu. I&#x27;m getting no features, only shorelines, whi...'''
date = "2013-04-29T20:18:00Z"
lastmod = "2013-07-15T18:24:00Z"
weight = 21978
keywords = [ "osm", "mapnik" ]
aliases = [ "/questions/21978" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik 2.1.x + OSM + Postgis 2 + PostgreSQL 9.2 + Python26 = Only shorelines and no features](/questions/21978/mapnik-21x-osm-postgis-2-postgresql-92-python26-only-shorelines-and-no-features)

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
<span id="post-21978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21978-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm having issues generating an OSM map with generate_image.py with Mapnik.</p>
<p>I am using PostgreSQL 9.2 with PostGIS 2 and Mapnik 2.1.x and python26 I am also on Oracle Enterpise Linux 6, which makes things a little less straightforward compared to Ubuntu.</p>
<p>I'm getting no features, only shorelines, which I know can be a common problem.</p>
<p>So far: I found this: /usr/local/lib/mapnik/input/postgis.input So I believe Mapnik was built properly with PostGIS.</p>
<p>Every time I try to run generate_image.py, I get no errors at the prompt. In my postgresql log I see all the SELECT statements with LIMIT 0 but no further SELECT statements actually querying for the features. On another server where I have things working with Mapnik 1.7, PostgreSQL 8.4, and PostGIS 1.5, I see the LIMIT 0 selects but also a bunch of SELECTs where the actual features are being queried.</p>
<p>I can also go into psql and try to run some of the osm.xml sql searches and I get results. I can also run:</p>
<p>SELECT * FROM planet_osm_line WHERE planet_osm_line.way &amp;&amp; ST_MakeEnvelope(-226192, 6890886, -209682, 6896466, 900913);</p>
<p>Which give me a bunch of results in England, So I think my DB is loaded correctly from osm2pgsql.</p>
<p>Why is Mapnik stopping at the LIMIT 0 queries and not actually querying for the features?????</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '13, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/fbb15843641ffaf1c2259cc7ebb4735c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maw269&#39;s gravatar image" />
<p><span>maw269</span><br />
<span class="score" title="115 reputation points">115</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maw269 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '13, 23:43</strong> </span></p>
</div>
</div>
<div id="comments-container-21978" class="comments-container">
&#10;</div>
<div id="comment-tools-21978" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21978-form-container" class="comment-form-container">
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

<span id="24269"></span>

<div id="answer-container-24269" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24269-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The issue was mapnik 2.1.x. This release had a bug. I moved to mapnik 2.1.0 and it worked.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '13, 18:24</strong></p>
<img src="https://secure.gravatar.com/avatar/fbb15843641ffaf1c2259cc7ebb4735c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maw269&#39;s gravatar image" />
<p><span>maw269</span><br />
<span class="score" title="115 reputation points">115</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maw269 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24269" class="comments-container">
&#10;</div>
<div id="comment-tools-24269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24269-form-container" class="comment-form-container">
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

