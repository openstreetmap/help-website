+++
type = "question"
title = "Updating N America data to planet data"
description = '''I read the installation guide on http://wiki.openstreetmap.org/wiki/Nominatim/Installation but I&#x27;m still a bit hazy in my understanding of updates. I currently have North America data (from http://download.geofabrik.de/) successfully installed and running on my machine. I&#x27;m trying to update my data ...'''
date = "2014-02-06T01:46:00Z"
lastmod = "2014-02-06T08:47:00Z"
weight = 30492
keywords = [ "nominatim", "osm", "osm2pgsql", "update" ]
aliases = [ "/questions/30492" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Updating N America data to planet data](/questions/30492/updating-n-america-data-to-planet-data)

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
<span id="post-30492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30492-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I read the installation guide on <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">http://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> but I'm still a bit hazy in my understanding of updates. I currently have North America data (from <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a>) successfully installed and running on my machine. I'm trying to update my data to the full planet data - I just downloaded the most recent .osm.pbf planet data from <a href="http://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/">http://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/</a></p>
<p>Currently, the only thing I know how to do is wiping the entire DB clean and importing again from scratch, but figured that would be unnecessary if I could simply update on top of what I already have.</p>
<p>What do I have to do to update my current map data? Would my service be unavailable during the update? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '14, 01:46</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '14, 01:47</strong> </span></p>
</div>
</div>
<div id="comments-container-30492" class="comments-container">
&#10;</div>
<div id="comment-tools-30492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30492-form-container" class="comment-form-container">
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

<span id="30496"></span>

<div id="answer-container-30496" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30496-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-30496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="baekacaek has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(See also <a href="https://help.openstreetmap.org/questions/15505/import-more-osm-files-in-to-nominatim">Import more OSM files into Nominatim.)</a></p>
<p>You could theoretically produce a data file that contains the whole world without N America and load that, or load continent after continent. However this is likely to be <em>much</em> slower than simply starting from scratch with a full planet file.</p>
<p>If you choose to start from scratch then your service will be unavailable while you import, but if you choose to add data piecemeal then your service will likely be very slow during the update period.</p>
<p>If you have the luxury of a second server with enough fast disk capacity to do a full OSM import, and that server has the same software versions as your production machine, then you could run a full import on that server and then, with a very short interruption in availability, simply copy over the PostgreSQL database directory to your production machine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '14, 08:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30496" class="comments-container">
&#10;</div>
<div id="comment-tools-30496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30496-form-container" class="comment-form-container">
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

