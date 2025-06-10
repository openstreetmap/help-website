+++
type = "question"
title = "Tags missing from Geofabrik download"
description = '''Hi there, I am using the osmtw/postgis docker image running PostgreSQL 10.4 and osmtw/osm2pgsql to synchronise with osm on Geofabrik using the osmupdate and osm2pgsql utilities. I limited myself to the region Europe/Germany/Berlin. Everything went smooth and seems to be working. The table planetosmp...'''
date = "2022-01-07T15:24:00Z"
lastmod = "2022-01-07T15:30:00Z"
weight = 82983
keywords = [ "geofabrik" ]
aliases = [ "/questions/82983" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tags missing from Geofabrik download](/questions/82983/tags-missing-from-geofabrik-download)

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
<span id="post-82983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82983-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I am using the osmtw/postgis docker image running PostgreSQL 10.4 and osmtw/osm2pgsql to synchronise with osm on Geofabrik using the osmupdate and osm2pgsql utilities. I limited myself to the region Europe/Germany/Berlin.</p>
<p>Everything went smooth and seems to be working. The table planetosmpoints contains the node objects and their tags. However, I noticed that not all tags are in the table. For instance, the "cuisine"-tag is available via the OverpassAPI, but the planetosmpoints table does not contain it.</p>
<p>Can you think of any reason why some tags may be missing from the table?</p>
<p>Many thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '22, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/e21ccded56c7ae375ff8356ce08b853d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghelbing&#39;s gravatar image" />
<p><span>ghelbing</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghelbing has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82983" class="comments-container">
&#10;</div>
<div id="comment-tools-82983" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82983-form-container" class="comment-form-container">
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

<span id="82984"></span>

<div id="answer-container-82984" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82984-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not familiar with the details of this docker image but generally, when importing the data with osm2pgsql, a so-called "style file" governs which OSM tags get their own database columns and which do not. The style file that comes with the standard OSM map style (<a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.style)">https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.style)</a> does not request a column for "cuisine".</p>
<p>Usually you would import with the "hstore" option which leads to the creation of a column "tags" containing all tags that do not have their own column. If this is the case in your setup, then you can access the "cuisine" value with the syntax <code>tags-&gt;'cuisine'</code>, e.g.</p>
<pre><code>SELECT name, tags-&gt;&#39;cuisine&#39; as cuisine
FROM planet_osm_point</code></pre>
<p>Anyway this has nothing to do with the Geofabrik download file; the .osm.pbf contains all data ans all tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '22, 15:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jan '22, 15:31</strong> </span></p>
</div>
</div>
<div id="comments-container-82984" class="comments-container">
&#10;</div>
<div id="comment-tools-82984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82984-form-container" class="comment-form-container">
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

