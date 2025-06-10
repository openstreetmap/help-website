+++
type = "question"
title = "OSM2PLSQL : Error Importing OSM File into the Database"
description = '''Hello Team, I am trying to import the history file (OSH) from Geofabrik web site as shown below https://download.geofabrik.de/europe/great-britain.html [great-britain.osh.pbf, a file that contains the full OSM history for this region for processing with e.g. osmium. This file was last modified 3 day...'''
date = "2017-10-20T07:55:00Z"
lastmod = "2017-10-20T09:13:00Z"
weight = 60190
keywords = [ "import", "osh", "osm2pgsql", "error" ]
aliases = [ "/questions/60190" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM2PLSQL : Error Importing OSM File into the Database](/questions/60190/osm2plsql-error-importing-osm-file-into-the-database)

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
<span id="post-60190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60190-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Team,</p>
<p>I am trying to import the history file (OSH) from Geofabrik web site as shown below <a href="https://download.geofabrik.de/europe/great-britain.html">https://download.geofabrik.de/europe/great-britain.html</a> [great-britain.osh.pbf, a file that contains the full OSM history for this region for processing with e.g. osmium. This file was last modified 3 days ago. File size: 1.5 GB; MD5 sum: eb54225a2019051736dde7b84d7dda3d]</p>
<p>I can successfully convert the OSH file to OSM file using the OSMIUM Utility Every time the extract for Great Britain fails with the error message when using OSM2PGSQL to import the OSM data into the PostGreSQL database. I have tried a couple of times (with different files) and get same issue. WARNING: Node 5156175847 (version 2d) has an invalid location and has been ignored. This is not expected to happen with recent planet files, so please check that your input is correct. Processing: Node(133658k 38.4k/s) Way(25181k 21.20k/s) Relation(13110 126.06/s)node cache: stored: 133658930(100.00%), storage efficiency: 50.00% (dense blocks: 0, sparse nodes: 133658930), hit rate: 99.85% Osm2pgsql failed due to ERROR: Missing ref on relation member</p>
<p>The history extracts for other regions like Australia / New Zealand / San Francisco etc all work perfectly fine without any issues and this is only for Great Britain. Can you please help me with the issue ? Is this something to do with the extract data contents ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-osh" rel="tag" title="see questions tagged &#39;osh&#39;">osh</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '17, 07:55</strong></p>
<img src="https://secure.gravatar.com/avatar/de679c3f376bc4dd7e428ad9e1a25df6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rchittor&#39;s gravatar image" />
<p><span>rchittor</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rchittor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60190" class="comments-container">
&#10;</div>
<div id="comment-tools-60190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60190-form-container" class="comment-form-container">
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

<span id="60191"></span>

<div id="answer-container-60191" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60191-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osm2pgsql is not suitable for importing history files into PostGIS. In fact, there is no software that does this in a full-featured way. It is a difficult issue because many different historical versions of an object have to be created - often more versions than the object has.</p>
<p>You may have processed other history files without errors, this does not mean that the results will make sense.</p>
<p>The only software that comes near importing a history file into PostGIS is <a href="https://github.com/MaZderMind/osm-history-renderer/tree/master/importer">https://github.com/MaZderMind/osm-history-renderer/tree/master/importer</a> but it is old and unmaintained.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '17, 09:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-60191" class="comments-container">
&#10;</div>
<div id="comment-tools-60191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60191-form-container" class="comment-form-container">
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

