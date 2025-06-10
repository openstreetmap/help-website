+++
type = "question"
title = "Query features in a local OSM instance"
description = '''I&#x27;ve setup a local OSM Website instance and ran an experiment with a group during few months and now I want to parse the data. The overall data is less than 10k points and I need to show them in a single image, in a Kernel density map for example. The Website only shows mapped data after a high zoom...'''
date = "2020-09-22T20:37:00Z"
lastmod = "2020-09-22T22:05:00Z"
weight = 76773
keywords = [ "openstreetmap", "website", "query", "railsport" ]
aliases = [ "/questions/76773" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Query features in a local OSM instance](/questions/76773/query-features-in-a-local-osm-instance)

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
<span id="post-76773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76773-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've setup a local OSM Website instance and ran an experiment with a group during few months and now I want to parse the data. The overall data is less than 10k points and I need to show them in a single image, in a Kernel density map for example. The Website only shows mapped data after a high zoom level, in which the whole area isn't covered. Is there a way to gather this data from my local OSM server? If I could export the data and convert to shp or another GIS-like file I could make that map with 3rd party GIS, but I don't know how to export all the data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '20, 20:37</strong></p>
<img src="https://secure.gravatar.com/avatar/5f1f061e7e81f0e885227d27d95752f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlosguedes&#39;s gravatar image" />
<p><span>carlosguedes</span><br />
<span class="score" title="91 reputation points">91</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlosguedes has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76773" class="comments-container">
&#10;</div>
<div id="comment-tools-76773" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76773-form-container" class="comment-form-container">
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

<span id="76774"></span>

<div id="answer-container-76774" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76774-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="carlosguedes has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have a local instance of the OSM web site, then you can use the /map API call to download all of your data as an OSM xml file. This can then be imported into a PostGIS database with osm2pgsql, or directly loaded into QGIS, or converted to shape files with e.g. osmium or ogr2ogr.</p>
<p>If the area covered by your points is larger than 0.25 degrees squared you will have to adjust the <code>max_request_area</code> setting in your configuration. Likewise if you wanted to export more than 50,000 nods (adjust <code>max_number_of_nodes</code>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '20, 22:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-76774" class="comments-container">
&#10;</div>
<div id="comment-tools-76774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76774-form-container" class="comment-form-container">
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

