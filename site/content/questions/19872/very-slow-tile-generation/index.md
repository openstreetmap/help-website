+++
type = "question"
title = "very slow tile generation"
description = '''I am using mapnik to generate tiles from a full planet osm2pgsql db, and am finding it extremely slow. It is taking minutes to generate a single tile. I generated full planet tiles for levels 0-7 in a about a week, but now I&#x27;ve narrowed it to a single medium-sized country for levels 8-16. I&#x27;m curren...'''
date = "2013-02-12T15:44:00Z"
lastmod = "2013-02-12T17:03:00Z"
weight = 19872
keywords = [ "tiles", "mapnik" ]
aliases = [ "/questions/19872" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [very slow tile generation](/questions/19872/very-slow-tile-generation)

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
<span id="post-19872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19872-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using mapnik to generate tiles from a full planet osm2pgsql db, and am finding it <em>extremely</em> slow. It is taking minutes to generate a single tile. I generated full planet tiles for levels 0-7 in a about a week, but now I've narrowed it to a single medium-sized country for levels 8-16. I'm currently at level 11 and generating only about 4000 tiles in 24 hours, using 6 threads.</p>
<p>I am using someone else's planet db on a good-sized Ubuntu machine with plenty of cores and RAM. However, the postgres on this machine just has the default installed settings and was not tuned for the import (which took a few weeks). Unfortunately I cannot tune it myself, though I can ask for changes.</p>
<p>Any suggestions as to why the speed is so awful? Are there some specific postgres tuning recommendations for tile generation that would help? I have two other planet imports going on two other machines with postgres that was tuned for import, but the imports are not going to finish any time soon.</p>
<p>FOLLOWUP: This may have been due to using a database created by <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Import_and_index_OSM_data">Nominatim's setup.php</a> rather than a database created by using osm2pgsql in a straightforward way.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '13, 15:44</strong></p>
<img src="https://secure.gravatar.com/avatar/507c65170b1d6d484cf28f1a4db5ecb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dhalbert&#39;s gravatar image" />
<p><span>dhalbert</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dhalbert has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '13, 21:27</strong> </span></p>
</div>
</div>
<div id="comments-container-19872" class="comments-container">
&#10;</div>
<div id="comment-tools-19872" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19872-form-container" class="comment-form-container">
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

<span id="19876"></span>

<div id="answer-container-19876" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19876-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dhalbert has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure how long tiles should take for levels 0-7, but this sounds to me like an absence of GIST indexes on the geometry columns (or failure to update the stats associated with the indexes).</p>
<p>Whatever is the cause the way to diagnose the problem is to look at query execution plans. You should be able to turn query logging on for the PostgreSQL instance and grab a few representative queries. Using PGAdmin (or something similar) get the query execution plans for these queries and look at which indexes are being used. A typical mapnik tile will require 30+ individual queries so once you've worked out what the problem is for one the issue should be fine for all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '13, 17:03</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-19876" class="comments-container">
&#10;</div>
<div id="comment-tools-19876" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19876-form-container" class="comment-form-container">
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

