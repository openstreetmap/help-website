+++
type = "question"
title = "How can osm2pgsql/postgresql.conf be optimized to process ways?"
description = '''I am importing the planet into postgresql (ver 9.5) with osm2pgsql. I have 32MB RAM, 1.5 TB available on the drive, and 8 processors available. Nodes come in without a problem, but ways have only crept up to about 1 k/s. This does not bode well for relations. Here are my postgresql.conf settings:  s...'''
date = "2017-11-30T22:18:00Z"
lastmod = "2017-12-01T21:59:00Z"
weight = 60910
keywords = [ "ways", "slow", "optimization", "osm2pgsql" ]
aliases = [ "/questions/60910" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can osm2pgsql/postgresql.conf be optimized to process ways?](/questions/60910/how-can-osm2pgsqlpostgresqlconf-be-optimized-to-process-ways)

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
<span id="post-60910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60910-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am importing the planet into postgresql (ver 9.5) with osm2pgsql. I have 32MB RAM, 1.5 TB available on the drive, and 8 processors available.</p>
<p>Nodes come in without a problem, but ways have only crept up to about 1 k/s. This does not bode well for relations.</p>
<p>Here are my postgresql.conf settings:</p>
<ul>
<li>shared_buffers = 2GB</li>
<li>maintenance_work_mem = 10GB</li>
<li>work_mem = 50MB</li>
<li>effective_cache_size = 24GB</li>
<li>synchronous_commit = off</li>
<li>checkpoint_timeout = 10min</li>
<li>checkpoint_completion_target = 0.9</li>
<li>fsync = off</li>
<li>full_page_writes = off</li>
<li>autovacuum = off</li>
</ul>
<p>And my osm2pgsql line:</p>
<p>osm2pgsql -d gis --create --slim -G --hstore -C 20000 -number-processes 8 --flat-nodes ~/data/flat-nodes.bin --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/planet-latest.osm.pbf</p>
<p>What is the best way to optimize way (and relation) processing? Is there a clear bottleneck?</p>
<p>Thanks for any input.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-optimization" rel="tag" title="see questions tagged &#39;optimization&#39;">optimization</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '17, 22:18</strong></p>
<img src="https://secure.gravatar.com/avatar/f624310c76d809c42a9a75f0c11e29fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ctriplej&#39;s gravatar image" />
<p><span>ctriplej</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ctriplej has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60910" class="comments-container">
<span id="60911"></span>
<div id="comment-60911" class="comment">
<div id="post-60911-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The obvious next questions I guess are "what sort of disk" (i.e. an SSD or something rotating very fast), and is this hardware that you can reconfigure at will (e.g. if it's at a cloud provider) or is it a physical piece of tin in a rack?</p>
</div>
<div id="comment-60911-info" class="comment-info">
<span class="comment-age">(30 Nov '17, 23:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60912"></span>
<div id="comment-60912" class="comment">
<div id="post-60912-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I hope you don't actually have 32MB of RAM. That would certainly be a problem! :D</p>
</div>
<div id="comment-60912-info" class="comment-info">
<span class="comment-age">(01 Dec '17, 00:33)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="60919"></span>
<div id="comment-60919" class="comment">
<div id="post-60919-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I apologize for my typo... I have 32GB RAM. I am running on a PowerEdge R530 with 4 SATA 1TB 7.2k drives, or as SomeoneElse put it, some tin in a rack. Last evening I tweaked my parameters and restarted: osm2pgsql -C 24000 and bumped work_mem up to 100MB. This morning, I see Ways running at 1.06 k/s. It seemed Ways were processing a bit faster with -C 20000. Should I take memory away from osm2pgsql and give it to postgresql instead? I feel like I should be able to squeeze better performance out of this hardware. IMPORTANT - I forget to mention it is running on a ubuntu 16.04 vm through ESXI vmware.</p>
</div>
<div id="comment-60919-info" class="comment-info">
<span class="comment-age">(01 Dec '17, 14:18)</span> <span class="comment-user userinfo">ctriplej</span>
</div>
</div>
</div>
<div id="comment-tools-60910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60910-form-container" class="comment-form-container">
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

<span id="60921"></span>

<div id="answer-container-60921" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60921-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps I have found a solution. I noticed the virtual CPU setting on my vm was 1. Now it is bumped up to 8 and the nodes are processing at a faster rate then my last run. I will see what happens when the ways start processing in a few hours. I also pushed -C to 25000. I hope this works!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '17, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/f624310c76d809c42a9a75f0c11e29fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ctriplej&#39;s gravatar image" />
<p><span>ctriplej</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ctriplej has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60921" class="comments-container">
<span id="60926"></span>
<div id="comment-60926" class="comment">
<div id="post-60926-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, perhaps I spoke too soon. The Ways processing topped out at 1.16 k/s and is now dropping after about 5 hours. I will let it run over the weekend and see what happens.</p>
<p>So I am back to ... <strong>What is the best way to optimize the processing of ways? Should I take away RAM from osm2pgsql and dedicate more RAM to postgresql? Are these the processing rates I should expect?</strong></p>
</div>
<div id="comment-60926-info" class="comment-info">
<span class="comment-age">(01 Dec '17, 20:56)</span> <span class="comment-user userinfo">ctriplej</span>
</div>
</div>
</div>
<div id="comment-tools-60921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60921-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60929"></span>

<div id="answer-container-60929" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60929-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found some good info about how ways are processed and how the hardware handles it. If anyone else is having similar problems, check out:</p>
<p><a href="https://github.com/openstreetmap/osm2pgsql/issues/517#issuecomment-164551795">https://github.com/openstreetmap/osm2pgsql/issues/517#issuecomment-164551795</a></p>
<p><a href="https://github.com/openstreetmap/osm2pgsql/issues/534">https://github.com/openstreetmap/osm2pgsql/issues/534</a></p>
<p>And the planet file just keeps getting bigger!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '17, 21:59</strong></p>
<img src="https://secure.gravatar.com/avatar/f624310c76d809c42a9a75f0c11e29fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ctriplej&#39;s gravatar image" />
<p><span>ctriplej</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ctriplej has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60929" class="comments-container">
&#10;</div>
<div id="comment-tools-60929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60929-form-container" class="comment-form-container">
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

