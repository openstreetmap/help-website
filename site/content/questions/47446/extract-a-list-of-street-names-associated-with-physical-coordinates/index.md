+++
type = "question"
title = "Extract a list of street names associated with physical coordinates"
description = '''Hi folks, I am new to OSM and spatial data. I downloaded a PBF file for Germany from Geofabrik and imported it into a local Postgres-database using osm2pgsql. I would now like to extract all streets in this file/database and their GPS coordinates in WKT or GeoJSON. However, it seems that streets are...'''
date = "2016-01-11T09:05:00Z"
lastmod = "2016-01-11T17:11:00Z"
weight = 47446
keywords = [ "extract", "streetnames" ]
aliases = [ "/questions/47446" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extract a list of street names associated with physical coordinates](/questions/47446/extract-a-list-of-street-names-associated-with-physical-coordinates)

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
<span id="post-47446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47446-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi folks,</p>
<p>I am new to OSM and spatial data. I downloaded a PBF file for Germany from Geofabrik and imported it into a local Postgres-database using osm2pgsql. I would now like to extract all streets in this file/database and their GPS coordinates in WKT or GeoJSON.</p>
<p>However, it seems that streets are fragmented into smaller pieces and I am unsure how to merge these pieces. Also what would be the best approach (tool and data provider) to extract such information? Would it be best to use the PBF-file, the Postgis Database, or even shape-files?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '16, 09:05</strong></p>
<img src="https://secure.gravatar.com/avatar/d02513167c7db497e2a95e37e83c5490?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Erechtheus&#39;s gravatar image" />
<p><span>Erechtheus</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Erechtheus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47446" class="comments-container">
&#10;</div>
<div id="comment-tools-47446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47446-form-container" class="comment-form-container">
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

<span id="47451"></span>

<div id="answer-container-47451" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47451-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Erechtheus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you work with raw OSM data (either in a program you've written yourself, perhaps using the Osmium library, or through a Postgres setup where you have imported the data with osmosis and not osm2pgsql) then you have easy access to the node IDs used by a way; it would then be relatively easy to do something like "if two ways have the same name and share a start/end node, connect them into one object".</p>
<p>If you work with geometry data, i.e. OSM imported with osm2pgsql, then you have lost the topology (way ends in node ID X) but you have gained geometry; now it will be easy to run something like "if to ways have the same name and lie within 100 metres of each other, treat them as one object".</p>
<p>It depends on what you want to achieve really. Keep in mind that streets often don't have one start and one end point; there are streets shaped like a Christmas tree or <a href="http://www.openstreetmap.org/#map=19/49.00165/8.39601">having loops,</a> there are streets that are interrupted by a plaza or a piece of another street, or streets with separately mapped parallel lanes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '16, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-47451" class="comments-container">
&#10;</div>
<div id="comment-tools-47451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47451-form-container" class="comment-form-container">
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

