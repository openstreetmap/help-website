+++
type = "question"
title = "Problem importing Europe"
description = '''Hi guys, i seem to be having a bit of an issue importing Europe PBF terminate called after throwing an instance of &#x27;std::runtime_error&#x27;  what(): CREATE INDEX planet_osm_ways_nodes ON planet_osm_ways USING gin (nodes) WITH (FASTUPDATE=OFF) ;  failed: ERROR: could not extend file &quot;base/16385/4138500.7...'''
date = "2018-05-01T10:09:00Z"
lastmod = "2018-05-01T10:22:00Z"
weight = 63250
keywords = [ "import" ]
aliases = [ "/questions/63250" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problem importing Europe](/questions/63250/problem-importing-europe)

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
<span id="post-63250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63250-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>i seem to be having a bit of an issue importing Europe PBF</p>
<pre><code>terminate called after throwing an instance of &#39;std::runtime_error&#39;
  what():  CREATE INDEX planet_osm_ways_nodes ON planet_osm_ways USING gin (nodes) WITH (FASTUPDATE=OFF) ;
 failed: ERROR:  could not extend file &quot;base/16385/4138500.7&quot;: No space left on device
HINT:  Check free disk space.
&#10;Aborted
osm@osm-tiles:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       440G  313G  105G  75% /
devtmpfs         16G     0   16G   0% /dev
tmpfs            16G  4.0K   16G   1% /dev/shm
tmpfs            16G  1.6G   15G  10% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs            16G     0   16G   0% /sys/fs/cgroup</code></pre>
<p>As you can see, i have 25% of my disk space available, or has it removed stuff once its realised its not enough space?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '18, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/fa4e6fbb05a1a2a9d8ab31540b4ee391?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gaza1994&#39;s gravatar image" />
<p><span>gaza1994</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gaza1994 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63250" class="comments-container">
<span id="63252"></span>
<div id="comment-63252" class="comment">
<div id="post-63252-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you give us more of a clue - starting with what software you were actually running?</p>
<p>Can you import something smaller? Does that work OK?</p>
</div>
<div id="comment-63252-info" class="comment-info">
<span class="comment-age">(01 May '18, 10:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63250-form-container" class="comment-form-container">
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

<span id="63254"></span>

<div id="answer-container-63254" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63254-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-63254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gaza1994 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, Postgres will remove the intermediate files. CREATE INDEX is an atomic operation, so there is no point in keeping files of the failed operation around. <code>watch df -h /</code> while the import is ongoing will show you how far it goes. There may also be quotas or mount options that prevent non-root users from filling up the disk completely, but the threshold is certainly higher than 25%.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '18, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-63254" class="comments-container">
&#10;</div>
<div id="comment-tools-63254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63254-form-container" class="comment-form-container">
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

