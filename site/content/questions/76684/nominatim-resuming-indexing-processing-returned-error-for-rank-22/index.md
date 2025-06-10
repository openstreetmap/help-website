+++
type = "question"
title = "Nominatim: Resuming Indexing Processing Returned Error for Rank 22"
description = '''Hi everyone, I ran out of disk space on my Compute Engine VM instance whilst it was in the process of doing rank 30. So when I increased the disk space, and then promptly re-ran the indexing process from where it left off, I got a Keyboard Interrupt traceback midway through, on rank 22. Is it safe t...'''
date = "2020-09-17T20:13:00Z"
lastmod = "2020-09-17T20:31:00Z"
weight = 76684
keywords = [ "open-street-maps", "nominatim", "compute-engine", "vm", "server" ]
aliases = [ "/questions/76684" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim: Resuming Indexing Processing Returned Error for Rank 22](/questions/76684/nominatim-resuming-indexing-processing-returned-error-for-rank-22)

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
<span id="post-76684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76684-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>I ran out of disk space on my Compute Engine VM instance whilst it was in the process of doing rank 30. So when I increased the disk space, and then promptly re-ran the indexing process from where it left off, I got a Keyboard Interrupt traceback midway through, on rank 22. Is it safe to ignore this?</p>
<pre><code>WARNING: Starting rank 22
Traceback (most recent call last):
  File &quot;/srv/nominatim/Nominatim-3.5.1/nominatim/nominatim.py&quot;, line 370, in &lt;module&gt;
    Indexer(options).run()
  File &quot;/srv/nominatim/Nominatim-3.5.1/nominatim/nominatim.py&quot;, line 210, in run
    self.index(RankRunner(rank))
  File &quot;/srv/nominatim/Nominatim-3.5.1/nominatim/nominatim.py&quot;, line 227, in index
    for r in cur:
  File &quot;/usr/lib/python3.6/encodings/utf_8.py&quot;, line 15, in decode
    def decode(input, errors=&#39;strict&#39;):
KeyboardInterrupt
WARNING: Done 0/0 in 14 @ 0.000 per second - FINISHED rank 22
WARNING: Starting rank 23
WARNING: Done 0/0 in 0 @ 0.000 per second - FINISHED rank 23
WARNING: Starting rank 24
WARNING: Done 0/0 in 1 @ 0.000 per second - FINISHED rank 24
WARNING: Starting rank 25
WARNING: Done 0/0 in 0 @ 0.000 per second - FINISHED rank 25</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-open-street-maps" rel="tag" title="see questions tagged &#39;open-street-maps&#39;">open-street-maps</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-compute-engine" rel="tag" title="see questions tagged &#39;compute-engine&#39;">compute-engine</span> <span class="post-tag tag-link-vm" rel="tag" title="see questions tagged &#39;vm&#39;">vm</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '20, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/f8dd6d1f5bf765fbbb3001eb3bdf3f60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rirhun&#39;s gravatar image" />
<p><span>rirhun</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rirhun has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '20, 20:15</strong> </span></p>
</div>
</div>
<div id="comments-container-76684" class="comments-container">
&#10;</div>
<div id="comment-tools-76684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76684-form-container" class="comment-form-container">
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

<span id="76686"></span>

<div id="answer-container-76686" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76686-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rirhun has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The reindex looks for records in the <code>placex</code> table having <code>indexed_status &gt; 0</code> (because 0 means it was already indexed). Since rank 23, 24, 25 all show 'Done 0/0' (no places found) I'm sure rank 22 also had no places. So that's fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '20, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-76686" class="comments-container">
&#10;</div>
<div id="comment-tools-76686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76686-form-container" class="comment-form-container">
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

