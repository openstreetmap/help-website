+++
type = "question"
title = "How to record JOSM network traffic?"
description = '''I think I found a bug but I need to make sure, by seeing what JOSM is reading and writing to the network. I could use tcpflow, but we are dealing with HTTPS. So how might I log this traffic easily? Must I install a &quot;man in the middle&quot; or is there a debugging logging switch somewhere within JOSM othe...'''
date = "2018-02-19T03:52:00Z"
lastmod = "2018-02-19T06:25:00Z"
weight = 62197
keywords = [ "josm", "logging", "network", "debugging" ]
aliases = [ "/questions/62197" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to record JOSM network traffic?](/questions/62197/how-to-record-josm-network-traffic)

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
<span id="post-62197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62197-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I think I found a bug but I need to make sure, by seeing what JOSM is reading and writing to the network.</p>
<p>I could use tcpflow, but we are dealing with HTTPS.</p>
<p>So how might I log this traffic easily?</p>
<p>Must I install a "man in the middle" or is there a debugging logging switch somewhere within JOSM other than the items in the Help menu?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-logging" rel="tag" title="see questions tagged &#39;logging&#39;">logging</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-debugging" rel="tag" title="see questions tagged &#39;debugging&#39;">debugging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '18, 03:52</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Feb '18, 03:56</strong> </span></p>
</div>
</div>
<div id="comments-container-62197" class="comments-container">
&#10;</div>
<div id="comment-tools-62197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62197-form-container" class="comment-form-container">
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

<span id="62199"></span>

<div id="answer-container-62199" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62199-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>$ josm --debug #seems to do about 85% of what I want!</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '18, 06:25</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62199" class="comments-container">
&#10;</div>
<div id="comment-tools-62199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62199-form-container" class="comment-form-container">
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

