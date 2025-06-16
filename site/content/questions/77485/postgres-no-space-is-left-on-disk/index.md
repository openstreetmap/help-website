+++
type = "question"
title = "postgres : no space is left on disk"
description = '''Hello, I am trying to install OSM on a virtual machine of Esxi server 6.7 whcih on debian system. The allocated resources to the debian system are:  ram: 30G disk space: 70G CPU: 1  I am trying to import the osm map data for Germany to postgres database. I did this command : postgres@osm:~$ osm2pgsq...'''
date = "2020-11-10T09:30:00Z"
lastmod = "2020-11-11T16:40:00Z"
weight = 77485
keywords = [ "disk_usage", "postgresql", "osm2pgsql" ]
aliases = [ "/questions/77485" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [postgres : no space is left on disk](/questions/77485/postgres-no-space-is-left-on-disk)

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
<span id="post-77485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77485-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am trying to install OSM on a virtual machine of Esxi server 6.7 whcih on debian system.</p>
<p>The allocated resources to the debian system are:</p>
<ul>
<li>ram: 30G</li>
<li>disk space: 70G</li>
<li>CPU: 1</li>
</ul>
<p>I am trying to import the osm map data for Germany to postgres database.</p>
<p>I did this command :</p>
<pre><code>postgres@osm:~$ osm2pgsql --slim -d gis --hstore --multi-geometry --number-proce                                                                             sses 1 --tag-transform-script /home/osm/openstreetmap-carto/openstreetmap-carto.                                                                             lua --style /home/osm/openstreetmap-carto/openstreetmap-carto.style -C 16500 /ho                                                                             me/osm/germany-latest.osm.pbf</code></pre>
<p>Then I received this error</p>
<pre><code>Reading in file: /home/osm/germany-latest.osm.pbf
Using PBF parser.
Processing: Node(328827k 390.5k/s) Way(53629k 27.96k/s) Relation(0 0.00/s)COPY_END for COPY planet_osm_ways FROM STDIN;
 failed: ERROR:  could not extend file &quot;base/16385/34513.4&quot;: No space left on device
HINT:  Check free disk space.
CONTEXT:  COPY planet_osm_ways, line 20803763</code></pre>
<p>could you please help me, I am new on this part. I don not know exactly how much space is required</p>
<p>the output df -h on my host:</p>
<p><img src="/upfiles/23.PNG" alt="alt text" /></p>
<p>thanks for your answer. BR. Eman</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-disk_usage" rel="tag" title="see questions tagged &#39;disk_usage&#39;">disk_usage</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '20, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/e9b1e697b10bd1c9422e2fdc5b32eced?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eman7&#39;s gravatar image" />
<p><span>Eman7</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eman7 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Nov '20, 13:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-77485" class="comments-container">
&#10;</div>
<div id="comment-tools-77485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77485-form-container" class="comment-form-container">
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

<span id="77515"></span>

<div id="answer-container-77515" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77515-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A Germany import in the form you are attempting, with a data file from November 2020, will create a database of about 77 GB but will temporarily use about 90 GB of disk space.</p>
<p>It appears that your system only has 10 GB of free disk space on the / volume. You write that you have 70 GB but that space is nowhere to be seen in your "df" output, and would also not be sufficient.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '20, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-77515" class="comments-container">
&#10;</div>
<div id="comment-tools-77515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77515-form-container" class="comment-form-container">
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

