+++
type = "question"
title = "Define NEW and ESTABLISHED TCP packet based on TCP control bits"
description = '''How to define NEW and ESTABLISHED TCP packet based on TCP flags? I would think that NEW TCP packet has SYN flag set, ACK flag not set, RST flag not set, FIN flag not set and value of the rest of the flags is not important: NS CWR ECE URG ACK PSH RST SYN FIN x x x x 0 x 0 1 0  And ESTABLISHED TCP pac...'''
date = "2017-05-10T04:09:00Z"
lastmod = "2017-05-10T04:12:00Z"
weight = 61323
keywords = [ "tcpflags", "tcp" ]
aliases = [ "/questions/61323" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Define NEW and ESTABLISHED TCP packet based on TCP control bits](/questions/61323/define-new-and-established-tcp-packet-based-on-tcp-control-bits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61323-score" class="post-score" title="current number of votes">0</div><span id="post-61323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to define <code>NEW</code> and <code>ESTABLISHED</code> TCP packet based on TCP flags? I would think that <code>NEW</code> TCP packet has <code>SYN</code> flag set, <code>ACK</code> flag not set, <code>RST</code> flag not set, <code>FIN</code> flag not set and value of the rest of the flags is not important:</p><pre><code>NS CWR ECE URG ACK PSH RST SYN FIN
x  x   x   x   0   x   0   1   0</code></pre><p>And <code>ESTABLISHED</code> TCP packets are all the packets with <code>ACK</code> flag set:</p><pre><code>NS CWR ECE URG ACK PSH RST SYN FIN
x  x   x   x   1   x   x   x   x</code></pre><p>Is this correct?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpflags" rel="tag" title="see questions tagged &#39;tcpflags&#39;">tcpflags</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '17, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/c153148e19e1e7c04c48a2a5c4f68b54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrtn&#39;s gravatar image" /><p><span>mrtn</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrtn has no accepted answers">0%</span></p></div></div><div id="comments-container-61323" class="comments-container"></div><div id="comment-tools-61323" class="comment-tools"></div><div class="clear"></div><div id="comment-61323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61324"></span>

<div id="answer-container-61324" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61324-score" class="post-score" title="current number of votes">0</div><span id="post-61324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It can be a bit of a "what's your kind of definition for new/established" thing, but basically you're correct - as soon as the SYN flags are done for, the connection is established and all packets carry ACK flag (but should not have SYN set, or RST, because SYN is "new" again, and RST is abort/shutdown).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '17, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61324" class="comments-container"></div><div id="comment-tools-61324" class="comment-tools"></div><div class="clear"></div><div id="comment-61324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

