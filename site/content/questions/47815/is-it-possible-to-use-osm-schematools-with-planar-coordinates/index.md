+++
type = "question"
title = "Is it possible to use OSM schema/tools with planar coordinates?"
description = '''I&#x27;m interested in using OSM infrastructure and tools (e.g.: database schema and software) without the standard global dataset--to map and perform routing calculations on a local dataset (private/offline database) of an area that&#x27;s small enough that using planar coordinates measured relative to a loc...'''
date = "2016-02-02T16:12:00Z"
lastmod = "2016-02-02T21:39:00Z"
weight = 47815
keywords = [ "planar", "coordinates" ]
aliases = [ "/questions/47815" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to use OSM schema/tools with planar coordinates?](/questions/47815/is-it-possible-to-use-osm-schematools-with-planar-coordinates)

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
<span id="post-47815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47815-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm interested in using OSM infrastructure and tools (e.g.: database schema and software) without the standard global dataset--to map and perform routing calculations on a local dataset (private/offline database) of an area that's small enough that using planar coordinates measured relative to a local origin (e.g.: a corner inside a large building) is much more straightforward than using global lat/lon coordinates (it's difficult to measure where a reference point at the site is actually located in global lat/lon, and all measurements of site features/positions will necessarily be done using planar survey techniques (e.g.: using theodolites, or tape measure and taut string...); and the local curvature of the earth is negligible on this scale, so...).</p>
<p>Is it possible to just do this with local planar coordinates? Or do I need to pick a (probably arbitrary) global frame of reference and convert my planar measurements into lat/lon?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planar" rel="tag" title="see questions tagged &#39;planar&#39;">planar</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Feb '16, 16:12</strong></p>
<img src="https://secure.gravatar.com/avatar/0fdaa37ef2b3b1af685acf1a735228d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rozzin&#39;s gravatar image" />
<p><span>rozzin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rozzin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47815" class="comments-container">
&#10;</div>
<div id="comment-tools-47815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47815-form-container" class="comment-form-container">
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

<span id="47830"></span>

<div id="answer-container-47830" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47830-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No problem at all.</p>
<p>I regularly load OSM data into PostGIS using osm2pqsql a variety of such co-ordinate systems (British National Grid, Swiss National Grid, Irish Grid, some US State Planes etc). osm2pgsql has flags to change the co-ordinate system used.</p>
<p>For raw OSM data you may need to do more work (e.g., load in WGS84, and add additional columns in PostGIS for your favoured system).</p>
<p>Another option is to use Geography datatypes in PostGIS.</p>
<p>With very small datasets you may be able to do such re-projections on the fly in a tool such as QGIS.</p>
<p>Other options include using OSGeo's ogr range of tools.</p>
<p>The actual choice will depend on what specific issues you are interested in, what type of data you want to consume, and what outputs are desired. Notably anything to do with route calculations will involve options other than those described here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '16, 21:39</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-47830" class="comments-container">
&#10;</div>
<div id="comment-tools-47830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47830-form-container" class="comment-form-container">
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

