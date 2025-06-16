+++
type = "question"
title = "Osm2pgsql import for geo-coding"
description = '''Hi guys, I set up my own tile server following this really good tutorial (http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/).  Then I realized that I also wanted to perform geocoding on my database. How can I do that? Adding the gazetteer option when importing data with osm2p...'''
date = "2013-06-12T08:22:00Z"
lastmod = "2014-10-29T12:02:00Z"
weight = 23250
keywords = [ "gazetteer", "geocoding", "osm2pgsql", "tileserver" ]
aliases = [ "/questions/23250" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Osm2pgsql import for geo-coding](/questions/23250/osm2pgsql-import-for-geo-coding)

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
<span id="post-23250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23250-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>I set up my own tile server following this really good tutorial (<a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/).">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/).</a></p>
<p>Then I realized that I also wanted to perform geocoding on my database. How can I do that? Adding the gazetteer option when importing data with osm2pgsql? I'd like to keep my configuration (set up by the kakrueger ppa).</p>
<p>Waiting for your help. Thanks!</p>
<p>Lucas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gazetteer" rel="tag" title="see questions tagged &#39;gazetteer&#39;">gazetteer</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '13, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/4015aaa7dcb688fc988901e4caaac771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalu06&#39;s gravatar image" />
<p><span>Kalu06</span><br />
<span class="score" title="140 reputation points">140</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalu06 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23250" class="comments-container">
&#10;</div>
<div id="comment-tools-23250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23250-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="23265"></span>

<div id="answer-container-23265" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23265-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Finally I removed everything I installed from the first tutorial and, then, I followed this one (<a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation)">https://wiki.openstreetmap.org/wiki/Nominatim/Installation)</a> to install Nominatim directly instead.</p>
<p>Now I'm running into some problems (I'm importing a really small PBF file for test purpose):</p>
<pre><code>Reanalysing database...
NOTICE:   no notnull values, invalid stats
ANALYZE
Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.40.1
Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline complete.
Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Total execution time: 373 milliseconds.
PHP Warning:  file_get_contents(https://www.openstreetmap.org/api/0.6/node/2340848120/1): failed to open stream: Network is unreachable in /home/lucas/src/Nominatim/utils/setup.php on line 524
PHP Notice:  Undefined offset: 1 in /home/lucas/src/Nominatim/utils/setup.php on line 526
PHP Warning:  file_get_contents(http://planet.openstreetmap.org/replication/minute/?C=M;O=D): failed to open stream: Network is unreachable in /home/lucas/src/Nominatim/utils/setup.php on line 531
PHP Notice:  Undefined variable: aRepMatch in /home/lucas/src/Nominatim/utils/setup.php on line 543
PHP Warning:  file_get_contents(http://planet.openstreetmap.org/replication/minute/?C=M;O=D): failed to open stream: Network is unreachable in /home/lucas/src/Nominatim/utils/setup.php on line 544
PHP Notice:  Undefined variable: aRepMatch in /home/lucas/src/Nominatim/utils/setup.php on line 554
PHP Warning:  file_get_contents(http://planet.openstreetmap.org/replication/minute/?C=M;O=D): failed to open stream: Network is unreachable in /home/lucas/src/Nominatim/utils/setup.php on line 555
PHP Notice:  Undefined variable: aRepMatch in /home/lucas/src/Nominatim/utils/setup.php on line 565
Getting state file: http://planet.openstreetmap.org/replication/minute/.state.txt
PHP Warning:  file_get_contents(http://planet.openstreetmap.org/replication/minute/.state.txt): failed to open stream: Network is unreachable in /home/lucas/src/Nominatim/utils/setup.php on line 567
ERROR: unable to obtain state file
unable to obtain state file</code></pre>
<p>Here is the log I get at the end of the import. I tried to modify the open_basedir in the php.ini file but didn't work.</p>
<p>Any idea?</p>
<p>Thanks</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '13, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/4015aaa7dcb688fc988901e4caaac771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalu06&#39;s gravatar image" />
<p><span>Kalu06</span><br />
<span class="score" title="140 reputation points">140</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalu06 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23265" class="comments-container">
&#10;</div>
<div id="comment-tools-23265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23265-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38073"></span>

<div id="answer-container-38073" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38073-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>the ".state.txt" in my case was solved by putting this file manually into settings folder of nominatim. if i remember right. it seems like a typo of '.' in filename. because file there is 'state.txt'. i just copied it myself into settings folder and run again the script.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '14, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a1210bd799c66ef1cd9a13792bda1c31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dima&#39;s gravatar image" />
<p><span>dima</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dima has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38073" class="comments-container">
&#10;</div>
<div id="comment-tools-38073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38073-form-container" class="comment-form-container">
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

