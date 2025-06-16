+++
type = "question"
title = "Tuning Postgresql"
description = '''Hi guys, Id&#x27; like to import the France extract in my postgresql database with osm2pgsql. With the actual settings, it&#x27;s really slow... but I saw that it&#x27;s possible to tune Postgresql in order to speed up the process. But, I know almost nothing about hardware...  How would you tune my postgresql depe...'''
date = "2013-07-18T11:42:00Z"
lastmod = "2013-07-20T01:19:00Z"
weight = 24343
keywords = [ "nominatim", "postgresql", "osm2pgsql" ]
aliases = [ "/questions/24343" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tuning Postgresql](/questions/24343/tuning-postgresql)

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
<span id="post-24343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24343-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>Id' like to import the France extract in my postgresql database with osm2pgsql. With the actual settings, it's really slow... but I saw that it's possible to tune Postgresql in order to speed up the process. But, I know almost nothing about hardware...</p>
<p>How would you tune my postgresql depending on my hard configuration (shared_buffers, work_mem, etc) ?. I'm using Ubuntu 12.04 server on a virtual machine, 4G of RAM, 100 GB HD and 4 cores.</p>
<p>Thanks! Lucas<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '13, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/4015aaa7dcb688fc988901e4caaac771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalu06&#39;s gravatar image" />
<p><span>Kalu06</span><br />
<span class="score" title="140 reputation points">140</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalu06 has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jul '13, 12:49</strong> </span></p>
</div>
</div>
<div id="comments-container-24343" class="comments-container">
<span id="24345"></span>
<div id="comment-24345" class="comment">
<div id="post-24345-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You have tagged this with nominatim, can we assume that your import uses osm2pgsql?</p>
</div>
<div id="comment-24345-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 12:19)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="24347"></span>
<div id="comment-24347" class="comment">
<div id="post-24347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. Sorry, I forgot to mention it.</p>
</div>
<div id="comment-24347-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 12:39)</span> <span class="comment-user userinfo">Kalu06</span>
</div>
</div>
</div>
<div id="comment-tools-24343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24343-form-container" class="comment-form-container">
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

<span id="24348"></span>

<div id="answer-container-24348" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24348-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-24348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tuning postgres is an art. For starters see the <a href="https://wiki.openstreetmap.org/wiki/Postgresql">osm wiki</a>, the <a href="http://wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server">postgres wiki</a>, or the <a href="http://www.postgresql.org/docs/9.2/static/runtime-config.html">postgres doc</a>. Some of the most important things you should try :</p>
<ul>
<li>raise <a href="http://www.postgresql.org/docs/9.2/static/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY">shared_buffers</a> to 30-40% of available ram</li>
<li>raise <a href="http://www.postgresql.org/docs/9.2/static/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY">work_mem</a> until you stop seeing <a href="http://www.postgresql.org/docs/9.2/static/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHAT">log_temp_file</a> warnings in the logs, unless it gets so high that you'd run out of memory</li>
<li>raise <a href="http://www.postgresql.org/docs/9.2/static/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY">maintenance_work_mem</a> to twice that</li>
<li>raise <a href="http://www.postgresql.org/docs/9.2/static/runtime-config-wal.html#RUNTIME-CONFIG-WAL-CHECKPOINTS">checkpoint_segments</a> a bit and <a href="http://www.postgresql.org/docs/9.2/static/runtime-config-wal.html#RUNTIME-CONFIG-WAL-CHECKPOINTS">checkpoint_completion_target</a> to about 0.95</li>
<li>make sure you have the latest version of postgres (9.2 at the time of writing) and linux kernel</li>
<li>run postgres on the host instead of a virtual machine</li>
<li>give postgres an SSD drive and as much memory as you can afford (ideally enough to store the whole db, plus a bit to spare)</li>
<li>try formating the partition as XFS instead of EXT4; avoid btrfs for postres for now</li>
</ul>
<p>You'll need to experiment a bit. Don't change all the settings at once, just change a few and measure the effect. Use a small (but not trivially smal) data extract (for example Auvergne instead of the whole of France) to iterate faster.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '13, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-24348" class="comments-container">
<span id="24349"></span>
<div id="comment-24349" class="comment">
<div id="post-24349-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you very much for this comprehensive answer. I'm sure it wil be very helpful. I'm going to try that right away.</p>
</div>
<div id="comment-24349-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 12:56)</span> <span class="comment-user userinfo">Kalu06</span>
</div>
</div>
<span id="24369"></span>
<div id="comment-24369" class="comment">
<div id="post-24369-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>With only 4GB of ram and a single HDD, importing France will likely always be slow. In case this is an option, adding an SSD to put your database on, or increasing your ram to at least 8Gb or better 16Gb (and setting the cache parameter in osm2pgsql correctly) is probably the only way to really speed things up substantially.</p>
</div>
<div id="comment-24369-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 21:39)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-24348" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24348-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24389"></span>

<div id="answer-container-24389" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24389-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a first attempt to tune Postgres there's also a tool called pgtune: <a href="https://github.com/gregs1104/pgtune">https://github.com/gregs1104/pgtune</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '13, 01:19</strong></p>
<img src="https://secure.gravatar.com/avatar/019a45dc05eab7273c5b5a662b899848?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Geonick&#39;s gravatar image" />
<p><span>Geonick</span><br />
<span class="score" title="106 reputation points">106</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Geonick has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24389" class="comments-container">
&#10;</div>
<div id="comment-tools-24389" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24389-form-container" class="comment-form-container">
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

