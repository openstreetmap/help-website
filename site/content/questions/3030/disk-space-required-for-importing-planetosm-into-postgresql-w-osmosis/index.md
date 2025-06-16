+++
type = "question"
title = "Disk space required for importing planet.osm into PostgreSQL w/ Osmosis?"
description = '''I&#x27;ve been trying to import this beast into PostgreSQL. I&#x27;ve been using EC2 since I don&#x27;t have enough HDD space myself. My last attempt on a large EC2 instance, with 850GB, failed because it ran out of disk space. I have a graph to show it hitting the 850GB:  I&#x27;d like to know approximately how much s...'''
date = "2011-02-14T00:59:00Z"
lastmod = "2011-02-16T21:22:00Z"
weight = 3030
keywords = [ "postgresql", "osmosis" ]
aliases = [ "/questions/3030" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Disk space required for importing planet.osm into PostgreSQL w/ Osmosis?](/questions/3030/disk-space-required-for-importing-planetosm-into-postgresql-w-osmosis)

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
<span id="post-3030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3030-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been trying to import this beast into PostgreSQL. I've been using EC2 since I don't have enough HDD space myself.</p>
<p>My last attempt on a large EC2 instance, with 850GB, failed because it ran out of disk space. I have a graph to show it hitting the 850GB:</p>
<p><img src="http://goo.gl/AS59k" alt="Graph showing disk space running out" /></p>
<p>I'd like to know approximately how much space I need, or maybe 850GB is way bigger than required and Osmosis is going into an infinite loop?</p>
<p>I couldn't find out how to enable logging on osmosis, so I can see how far it's gone into the import.</p>
<p>The command I'm using is:</p>
<pre><code>time bzcat planet-latest.osm.bz2 | osmosis --read-xml file=&quot;/dev/stdin&quot; enableDateParsing=no --write-pgsql user=&quot;osm&quot; database=&quot;osm&quot; password=&quot;osm&quot;</code></pre>
<p>For my next attempt I'll give it 1TB.. I'll update this question appropriately with my results.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Feb '11, 00:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a3c56d2345b6767f7634c04d4b4a05ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gak&#39;s gravatar image" />
<p><span>gak</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gak has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Feb '11, 03:13</strong> </span></p>
</div>
</div>
<div id="comments-container-3030" class="comments-container">
<span id="3052"></span>
<div id="comment-3052" class="comment">
<div id="post-3052-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Update: I had a strange parsing error with Osmosis, so this test is on hold for now. I'm testing my development with australia.osm for now (which was ~3.4GB). I'll update this if I ever get planet.osm going.</p>
</div>
<div id="comment-3052-info" class="comment-info">
<span class="comment-age">(15 Feb '11, 04:55)</span> <span class="comment-user userinfo">gak</span>
</div>
</div>
</div>
<div id="comment-tools-3030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3030-form-container" class="comment-form-container">
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

<span id="3107"></span>

<div id="answer-container-3107" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3107-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gak has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think there is something wrong.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Servers/yevaud">yevaud</a>, the mapnik-rendering-Server, has this configuration:</p>
<p><code>/database - sdb - 4x 300GB 10kRPM (RAID10)</code></p>
<p>the <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/df.html">usage</a> is at 60%</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '11, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/db9d4c9ffd75f95f97122bbc97b90a64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="josias&#39;s gravatar image" />
<p><span>josias</span><br />
<span class="score" title="598 reputation points">598</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="josias has 3 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-3107" class="comments-container">
<span id="3123"></span>
<div id="comment-3123" class="comment">
<div id="post-3123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I'll look into the problem.</p>
</div>
<div id="comment-3123-info" class="comment-info">
<span class="comment-age">(16 Feb '11, 21:22)</span> <span class="comment-user userinfo">gak</span>
</div>
</div>
</div>
<div id="comment-tools-3107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3107-form-container" class="comment-form-container">
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

