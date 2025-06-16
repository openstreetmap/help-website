+++
type = "question"
title = "[closed] No results on Nominatim search"
description = '''Hi guys, I just installed Nominatim on my Ubuntu 12.04 (personal OSM server for offline use). I&#x27;m wondering why I got no result when peforming a search on search.php ?! I checked in the nominatim DB and there&#x27;s data... Here&#x27;s the log I get at the end of my import:  Reanalysing database... NOTICE: no...'''
date = "2013-06-13T15:14:00Z"
lastmod = "2013-06-14T10:55:00Z"
weight = 23341
keywords = [ "xml", "nominatim", "searching" ]
aliases = [ "/questions/23341" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] No results on Nominatim search](/questions/23341/closed-no-results-on-nominatim-search)

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
<span id="post-23341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23341-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys, I just installed Nominatim on my Ubuntu 12.04 (personal OSM server for offline use). I'm wondering why I got no result when peforming a search on search.php ?! I checked in the nominatim DB and there's data... Here's the log I get at the end of my import:</p>
<p><code>Reanalysing database... NOTICE: no notnull values, invalid stats ANALYZE Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.40.1 Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Launching pipeline execution. Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline executing, waiting for completion. Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline complete. Jun 12, 2013 2:41:08 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Total execution time: 373 milliseconds. PHP Warning: file_get_contents(</code><a href="https://www.openstreetmap.org/api/0.6/node/2340848120/1):"><code>https://www.openstreetmap.org/api/0.6/node/2340848120/1):</code></a><code> failed to open stream: Network is unreachable in /home/lucas/src/Nominatim/utils/setup.php on line 524 PHP Notice: Undefined offset: 1 in /home/lucas/src/Nominatim/utils/setup.php on line 526 PHP Warning: file_get_contents(</code><a href="http://planet.openstreetmap.org/replication/minute/?C=M;O=D):"><code>http://planet.openstreetmap.org/replication/minute/?C=M;O=D):</code></a><code> failed to open stream: Network is unreachable in /home/lucas/src/Nominatim/utils/setup.php on line 531 PHP Notice: Undefined variable: aRepMatch in /home/lucas/src/Nominatim/utils/setup.php on line 543 PHP Warning: file_get_contents(</code><a href="http://planet.openstreetmap.org/replication/minute/?C=M;O=D):"><code>http://planet.openstreetmap.org/replication/minute/?C=M;O=D):</code></a><code> failed to open stream: Network is unreachable in /home/lucas/src/Nominatim/utils/setup.php on line 544 PHP Notice: Undefined variable: aRepMatch in /home/lucas/src/Nominatim/utils/setup.php on line 554 PHP Warning: file_get_contents(</code><a href="http://planet.openstreetmap.org/replication/minute/?C=M;O=D):"><code>http://planet.openstreetmap.org/replication/minute/?C=M;O=D):</code></a><code> failed to open stream: Network is unreachable in /home/lucas/src/Nominatim/utils/setup.php on line 555 PHP Notice: Undefined variable: aRepMatch in /home/lucas/src/Nominatim/utils/setup.php on line 565 Getting state file: </code><a href="http://planet.openstreetmap.org/replication/minute/.state.txt"><code>http://planet.openstreetmap.org/replication/minute/.state.txt</code></a><code> PHP Warning: file_get_contents(</code><a href="http://planet.openstreetmap.org/replication/minute/.state.txt):"><code>http://planet.openstreetmap.org/replication/minute/.state.txt):</code></a><code> failed to open stream: Network is unreachable in /home/lucas/src/Nominatim/utils/setup.php on line 567 ERROR: unable to obtain state file unable to obtain state file</code></p>
<p>However, these lines seem to be referring only to the "updating" process handled by Nominatim. By the way, I'm using a proxy. Thanks, Lucas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-searching" rel="tag" title="see questions tagged &#39;searching&#39;">searching</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '13, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/4015aaa7dcb688fc988901e4caaac771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalu06&#39;s gravatar image" />
<p><span>Kalu06</span><br />
<span class="score" title="140 reputation points">140</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalu06 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jun '13, 15:16</strong> </span></p>
</div>
</div>
<div id="comments-container-23341" class="comments-container">
<span id="23364"></span>
<div id="comment-23364" class="comment">
<div id="post-23364-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I know nothing about Nominatim (except how to spell it), but in order to give those that do a chance I suggest that you read the link below and edit a few more details into the question:</p>
<p><a href="http://www.joelonsoftware.com/articles/fog0000000029.html">http://www.joelonsoftware.com/articles/fog0000000029.html</a></p>
</div>
<div id="comment-23364-info" class="comment-info">
<span class="comment-age">(14 Jun '13, 09:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="23365"></span>
<div id="comment-23365" class="comment">
<div id="post-23365-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's true. I'm going to edit my post right away.</p>
</div>
<div id="comment-23365-info" class="comment-info">
<span class="comment-age">(14 Jun '13, 09:49)</span> <span class="comment-user userinfo">Kalu06</span>
</div>
</div>
</div>
<div id="comment-tools-23341" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23341-form-container" class="comment-form-container">
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

<span id="23368"></span>

<div id="answer-container-23368" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23368-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-23368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I figured it out!</p>
<p>Actually, I realized that setup.php was failing during the 'osmosis-init'. I run <code>./utils/setup.php --index --create-search-indices</code> (after the <code>setup.php --all</code> who failed) and now everything is working great!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jun '13, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/4015aaa7dcb688fc988901e4caaac771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalu06&#39;s gravatar image" />
<p><span>Kalu06</span><br />
<span class="score" title="140 reputation points">140</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalu06 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23368" class="comments-container">
&#10;</div>
<div id="comment-tools-23368" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23368-form-container" class="comment-form-container">
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

