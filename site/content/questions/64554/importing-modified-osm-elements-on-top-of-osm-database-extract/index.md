+++
type = "question"
title = "Importing modified OSM elements on top of OSM database extract"
description = '''I&#x27;ve got a dataset of custom ids / tags mapped to OSM way ids. I wish I could import them, but this currently not possible. How can I add this data, which is in .osm format, to a osm pbf database export e.g. from Geofabrik? If this is impossible and as I&#x27;m going to import the osm pbf file anyway: Ca...'''
date = "2018-07-05T19:27:00Z"
lastmod = "2018-07-05T22:30:00Z"
weight = 64554
keywords = [ "import", "postgresql" ]
aliases = [ "/questions/64554" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Importing modified OSM elements on top of OSM database extract](/questions/64554/importing-modified-osm-elements-on-top-of-osm-database-extract)

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
<span id="post-64554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64554-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've got a dataset of custom ids / tags mapped to OSM way ids. I wish I could import them, but this currently not possible.</p>
<p>How can I add this data, which is in .osm format, to a osm pbf database export e.g. from Geofabrik?</p>
<p>If this is impossible and as I'm going to import the osm pbf file anyway: Can I "overwrite" features by doing a osm2psql import of custom data on top of a prior OSM import?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '18, 19:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0dd38728dd1aa85ca045b06a4273a37f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="norcross&#39;s gravatar image" />
<p><span>norcross</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="norcross has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '18, 19:32</strong> </span></p>
</div>
</div>
<div id="comments-container-64554" class="comments-container">
&#10;</div>
<div id="comment-tools-64554" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64554-form-container" class="comment-form-container">
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

<span id="64555"></span>

<div id="answer-container-64555" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64555-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use the <code>osmium</code> program (C++) or <code>osmosis</code> (Java) to merge both files into one. Or you could use the <code>--append</code> mode of osm2pgsql to load your data after you've loaded the OSM data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '18, 22:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64555" class="comments-container">
&#10;</div>
<div id="comment-tools-64555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64555-form-container" class="comment-form-container">
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

