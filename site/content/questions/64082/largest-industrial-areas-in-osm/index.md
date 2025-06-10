+++
type = "question"
title = "Largest industrial areas in OSM"
description = '''I&#x27;m curious about the largest industrial parks / districts in OpenStreetMap. With which software can I get all landuse=industrial ways &amp;amp; relations in the planet dump by size?'''
date = "2018-06-07T18:10:00Z"
lastmod = "2018-06-07T20:01:00Z"
weight = 64082
keywords = [ "osmium", "query", "osmfilter", "postgis" ]
aliases = [ "/questions/64082" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Largest industrial areas in OSM](/questions/64082/largest-industrial-areas-in-osm)

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
<span id="post-64082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64082-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm curious about the largest industrial parks / districts in OpenStreetMap.</p>
<p>With which software can I get all landuse=industrial ways &amp; relations in the planet dump by size?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '18, 18:10</strong></p>
<img src="https://secure.gravatar.com/avatar/bdb6a1b49c42d8be4b8d87f3096a3622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Druzhba&#39;s gravatar image" />
<p><span>Druzhba</span><br />
<span class="score" title="150 reputation points">150</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Druzhba has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64082" class="comments-container">
&#10;</div>
<div id="comment-tools-64082" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64082-form-container" class="comment-form-container">
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

<span id="64084"></span>

<div id="answer-container-64084" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64084-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use <code>osmium-tool</code> to filter the planet for landuse=industrial (you want relations and ways). Then either import the resulting file to PostGIS with <code>osm2pgsql</code> or convert to shape file with a recent version of GDAL, or load directly in a suitable GIS program. PostGIS would be my favourite choice because it would easily allow some automated processing, like merging industrial areas that are very close (maybe just separated by a road).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '18, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64084" class="comments-container">
&#10;</div>
<div id="comment-tools-64084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64084-form-container" class="comment-form-container">
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

