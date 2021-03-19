+++
type = "question"
title = "question about tcp rate"
description = '''Hi I want to know , if I have a captured traffic file for a day, how can reach the statistics of MAXIMUM CONCURRENT TCP CONNECTIONS MAXIMUM TCP CONNECTIONS PER SECOND MAXIMUM HTTP CONNECTIONS PER SECOND MAXIMUM HTTP TRANSACTIONS PER SECOND   thanks '''
date = "2014-04-14T22:00:00Z"
lastmod = "2014-04-15T01:36:00Z"
weight = 31812
keywords = [ "connections", "concurrent", "tcp" ]
aliases = [ "/questions/31812" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [question about tcp rate](/questions/31812/question-about-tcp-rate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31812-score" class="post-score" title="current number of votes">0</div><span id="post-31812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I want to know , if I have a captured traffic file for a day, how can reach the statistics of</p><pre><code>MAXIMUM CONCURRENT TCP CONNECTIONS
MAXIMUM TCP CONNECTIONS PER SECOND
MAXIMUM HTTP CONNECTIONS PER SECOND
MAXIMUM HTTP TRANSACTIONS PER SECOND</code></pre><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-connections" rel="tag" title="see questions tagged &#39;connections&#39;">connections</span> <span class="post-tag tag-link-concurrent" rel="tag" title="see questions tagged &#39;concurrent&#39;">concurrent</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '14, 22:00</strong></p><img src="https://secure.gravatar.com/avatar/deec7afda5035771868d6acfbc90d994?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mosa&#39;s gravatar image" /><p><span>mosa</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mosa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Apr '14, 01:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-31812" class="comments-container"></div><div id="comment-tools-31812" class="comment-tools"></div><div class="clear"></div><div id="comment-31812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31826"></span>

<div id="answer-container-31826" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31826-score" class="post-score" title="current number of votes">0</div><span id="post-31826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>MAXIMUM <strong>CONCURRENT</strong> TCP CONNECTIONS</p></blockquote><p>Not that easy to count in Wireshark, as there is no such functionality</p><blockquote><p>MAXIMUM TCP CONNECTIONS PER SECOND</p></blockquote><p>Take a look at IO graphs: Statistics -&gt; IO Graph. Count the packet rate with SYN flags (Filter: tcp.flags eq 0x02). This will actually show connection <strong>attempts</strong>. If a connection fails (no SYN-ACK), it will be counted as well, but for 'statistics' this shouldn't be a problem.</p><blockquote><p>MAXIMUM HTTP CONNECTIONS PER SECOND</p></blockquote><p>Same as TCP CONNECTIONS PER SECOND, just for port 80 (Filter: tcp.port eq 80)</p><blockquote><p>MAXIMUM HTTP TRANSACTIONS PER SECOND</p></blockquote><p>Please define what a <strong>HTTP transaction</strong> is in your environment.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '14, 01:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31826" class="comments-container"></div><div id="comment-tools-31826" class="comment-tools"></div><div class="clear"></div><div id="comment-31826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

