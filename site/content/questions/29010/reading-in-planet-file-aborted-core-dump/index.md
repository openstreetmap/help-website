+++
type = "question"
title = "Reading in Planet File - Aborted Core Dump"
description = '''This problem may have been cataloged before so I&#x27;m posting in case there are continuing problems with osm.pbf planet files or to get help discovering any problems on my end. My setup:  Machine Windows 7 32 GB RAM Intel i7-3740QM 2.70 GHZ processor 236 GB disk space 64-bit VirtualBox Version 4.3.4 Li...'''
date = "2013-12-12T15:07:00Z"
lastmod = "2013-12-17T17:02:00Z"
weight = 29010
keywords = [ "pbf", "osm2pgsql" ]
aliases = [ "/questions/29010" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reading in Planet File - Aborted Core Dump](/questions/29010/reading-in-planet-file-aborted-core-dump)

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
<span id="post-29010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29010-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This problem may have been cataloged <a href="https://help.openstreetmap.org/questions/27411/reading-in-planet-file-aborted-core-dump">before</a> so I'm posting in case there are continuing problems with osm.pbf planet files or to get help discovering any problems on my end.</p>
<p>My setup:</p>
<ul>
<li><strong>Machine</strong></li>
<li>Windows 7</li>
<li>32 GB RAM</li>
<li>Intel i7-3740QM 2.70 GHZ processor</li>
<li>236 GB disk space</li>
<li>64-bit</li>
<li><strong>VirtualBox</strong></li>
<li>Version 4.3.4</li>
<li>Linux 2.6 (64-bit) running Ubuntu 12.04</li>
<li>24 GB RAM</li>
<li>620 GB disk space</li>
<li><strong>osm2pgsql command</strong>: osm2pgsql --slim -d gis -C 18000 --number-processes 3 planet-latest.pbf</li>
</ul>
<p>What happened:</p>
<p>While following the <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">Manually building a tile server directions</a> on switch2osm all steps up to the planet file import completed successfully. However, towards the end of Processing: Relation (47800 3.66/s) I got the following error:</p>
<pre><code>osm2pgsql: PolygonBuilder.cpp:261: geos::geomgraph::EdgeRing* geos::operation::overlay::PolygonBuilder::findshell(std::vector&lt;geos::operation::overlay::MinimalEdgeRing*&gt;*):Assertion &#39;shellCount &lt;=1&#39; failed. Aborted (core dumped)</code></pre>
<p>I downloaded the planet on December 10th (with command wget <a href="http://planet.openstreetmap.org/pbf/planet-latest.osm.pbf">http://planet.openstreetmap.org/pbf/planet-latest.osm.pbf</a>) and started the import the same day. Have problems been reported with planet-131204 (or was a different file planet-latest.osm.pbf on the 10th)? Could it be a problem on my end?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '13, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/7ee1136c8ef2d8dc1e88bedbd50f6db2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alpha47&#39;s gravatar image" />
<p><span>Alpha47</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alpha47 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '13, 15:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-29010" class="comments-container">
&#10;</div>
<div id="comment-tools-29010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29010-form-container" class="comment-form-container">
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

<span id="29145"></span>

<div id="answer-container-29145" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29145-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Update:</p>
<p>I switched to osm2pgsql 0.81 like daveyp1234 and got around this problem. I ran into other problems towards the end of the planet file import but right now I'm still investigating them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '13, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/7ee1136c8ef2d8dc1e88bedbd50f6db2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alpha47&#39;s gravatar image" />
<p><span>Alpha47</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alpha47 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29145" class="comments-container">
&#10;</div>
<div id="comment-tools-29145" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29145-form-container" class="comment-form-container">
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

