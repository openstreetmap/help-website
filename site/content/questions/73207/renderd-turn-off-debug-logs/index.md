+++
type = "question"
title = "renderd turn off debug logs"
description = '''Is there any way to make renderd no output DEBUG level logs? There is nothing showing the man page for renderd and scanning the code doesn&#x27;t show up anything obvious for log level. I&#x27;ve tried all the usual LogLevel options in Apache but none of them go down to the renderd daemon. Specifically it is ...'''
date = "2020-02-23T18:25:00Z"
lastmod = "2020-02-23T18:25:00Z"
weight = 73207
keywords = [ "renderd", "logging" ]
aliases = [ "/questions/73207" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [renderd turn off debug logs](/questions/73207/renderd-turn-off-debug-logs)

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
<span id="post-73207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73207-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there any way to make renderd no output DEBUG level logs? There is nothing showing the man page for renderd and scanning the code doesn't show up anything obvious for log level. I've tried all the usual LogLevel options in Apache but none of them go down to the renderd daemon.</p>
<p>Specifically it is logs like these that I'm trying to hide</p>
<pre><code>Feb 23 18:22:24 oms-tileserver renderd[24621]: DEBUG: Got incoming connection, fd 27, number 18
Feb 23 18:22:24 oms-tileserver renderd[24621]: DEBUG: Got incoming request with protocol version 2
Feb 23 18:22:24 oms-tileserver renderd[24621]: DEBUG: Got command RenderLow fd(27) xml(ajt), z(16), x(31605), y(21298), mime(image/png), options()
Feb 23 18:22:24 oms-tileserver renderd[24621]: DEBUG: Got incoming connection, fd 28, number 19
Feb 23 18:22:24 oms-tileserver renderd[24621]: DEBUG: Got incoming request with protocol version 2
Feb 23 18:22:24 oms-tileserver renderd[24621]: DEBUG: Got command RenderLow fd(28) xml(ajt), z(16), x(31605), y(21297), mime(image/png), options()
Feb 23 18:22:27 oms-tileserver renderd[24621]: DEBUG: DONE TILE ajt 16 31600-31607 21296-21303 in 2.534 seconds</code></pre>
<p>I'd prefer something in the daemon rather than having to drop these in syslog if possible.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-logging" rel="tag" title="see questions tagged &#39;logging&#39;">logging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Feb '20, 18:25</strong></p>
<img src="https://secure.gravatar.com/avatar/0aa6d807c6f317f02f7837c01e2afa7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryaner&#39;s gravatar image" />
<p><span>ryaner</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryaner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73207" class="comments-container">
&#10;</div>
<div id="comment-tools-73207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73207-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

