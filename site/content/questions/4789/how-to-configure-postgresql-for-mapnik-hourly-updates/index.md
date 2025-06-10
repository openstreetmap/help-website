+++
type = "question"
title = "How to configure postgresql for mapnik hourly updates?"
description = '''We have decent hardware: 8-core AMD, 16G RAM, SATA drives. This meant for a tile server with full planet coverage. The problem is that running hourly diffs takes constantly more than 1 hour (1.5 hours or so), so database is constantly lacking behind. The same machine is expected to be able to genera...'''
date = "2011-04-25T13:12:00Z"
lastmod = "2012-01-14T14:58:00Z"
weight = 4789
keywords = [ "osm2pgsql", "mapnik", "update" ]
aliases = [ "/questions/4789" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to configure postgresql for mapnik hourly updates?](/questions/4789/how-to-configure-postgresql-for-mapnik-hourly-updates)

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
<span id="post-4789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4789-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have decent hardware: 8-core AMD, 16G RAM, SATA drives. This meant for a tile server with full planet coverage. The problem is that running hourly diffs takes constantly more than 1 hour (1.5 hours or so), so database is constantly lacking behind. The same machine is expected to be able to generate mapnik tiles also: we expect most load for small number (region), so caching should be quite effective.</p>
<p>Config is:</p>
<ul>
<li>ubuntu 10.4 64-bit</li>
<li>postgres 9.0</li>
<li>shared_buffers = 5GB</li>
<li>work_mem = 512MB</li>
<li>maintenance_work_mem = 128MB</li>
<li><p>autovacuum = off</p></li>
<li><p>osm2pgsql is run as: osm2pgsql --append --slim -d gis -S /var/lib/postgresql/estonia.style -C16000 changes.osc.gz</p></li>
<li>sysctl.conf: kernel.shmmax = 8589934592 kernel.shmmni = 18589934592</li>
</ul>
<p>Monitoring shows following suspicious stuff:</p>
<ul>
<li>only one core is used for postgres UPDATE transactions, can it be fixed?</li>
<li>iostat does shows idle for data disk for most of the time</li>
<li>1G of memory is used (based on htop)</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '11, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ff53f6579540c3da3a1ad5180515cc67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JaakL&#39;s gravatar image" />
<p><span>JaakL</span><br />
<span class="score" title="42 reputation points">42</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JaakL has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4789" class="comments-container">
&#10;</div>
<div id="comment-tools-4789" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4789-form-container" class="comment-form-container">
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

<span id="9954"></span>

<div id="answer-container-9954" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9954-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osm2pgsql is run as: osm2pgsql --number-processes=8 --append --slim -d gis -S /var/lib/postgresql/estonia.style -C16000 changes.osc.gz</p>
<p>Shold make you use all cores....</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '12, 14:58</strong></p>
<img src="https://secure.gravatar.com/avatar/6bf3adc8d0f26946f3c24cedff97f72d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Magnus%20L&#39;s gravatar image" />
<p><span>Magnus L</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Magnus L has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9954" class="comments-container">
&#10;</div>
<div id="comment-tools-9954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9954-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4796"></span>

<div id="answer-container-4796" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4796-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am surprised to hear that your disks are idle; the usual recommendation in these cases is to increase disk performace by using fast hard disks, putting your PostgreSQL data on a RAID-0 or RAID-1 device (combining multiple SATA drives with Linux Software RAID), or even getting an SSD.</p>
<p>If you can get hold of a 250GB+ SSD for a week, connect that, copy your tablespace over and see how long the diff application takes then. I should be surprised if it were more than 15 minutes for a hourly diff.</p>
<p>Also, make sure you have FASTUPDATE set to OFF on your indexes (they will automatically have been created like that if you did your initial import with an osm2pgsql SVN version checked out after 31st January 2011). See <a href="http://lists.openstreetmap.org/pipermail/dev/2011-January/021704.html">this thread on the dev mailing list</a> for details.</p>
<p>You could try a slight increase in maintenance_work_mem (say, to 512 MB), and you could try fsync=off. Note that if you intend to continue with autovacuum=off you will have to make sure your tables are vacuumed some other way (e.g. nightly).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '11, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-4796" class="comments-container">
<span id="4829"></span>
<div id="comment-4829" class="comment">
<div id="post-4829-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Disks should be fast enough - these are 15000 rpm disks in stripe. There must be something in configuration, but we don't figure out what. Just to confirm: hourly global updates should work with our hardware, also without SSD?</p>
</div>
<div id="comment-4829-info" class="comment-info">
<span class="comment-age">(26 Apr '11, 16:05)</span> <span class="comment-user userinfo">JaakL</span>
</div>
</div>
<span id="4830"></span>
<div id="comment-4830" class="comment">
<div id="post-4830-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Let's put it this way - I have never heard of anybody who complained about not being able to apply hourly updates on 15krpm striped disks. Maybe check your disk subsystem independently of Postgres and if everything looks fine, you'll probably have to investige Postgres more thoroughly - maybe increase logging and see where all this disk-idle-but-machine-busy time is spent...</p>
</div>
<div id="comment-4830-info" class="comment-info">
<span class="comment-age">(26 Apr '11, 16:11)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-4796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4796-form-container" class="comment-form-container">
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

