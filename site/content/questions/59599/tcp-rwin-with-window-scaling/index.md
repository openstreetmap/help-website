+++
type = "question"
title = "TCP RWin with window scaling"
description = '''Hey everyone, just wondered: if i have a TCP packet with SYN flag set, there is a window size set in the RWIN header field (e.g. 0x2000) and there might be a window scale option in the options section (eg 0x030308 --&amp;gt; WinScale, Len 3, shift by 8). From what I understand, RWin should be (0x2000 &amp;l...'''
date = "2017-02-22T02:05:00Z"
lastmod = "2017-02-22T06:53:00Z"
weight = 59599
keywords = [ "tcpwindowscaling", "wireshark", "tcp", "tcpwindowsize" ]
aliases = [ "/questions/59599" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP RWin with window scaling](/questions/59599/tcp-rwin-with-window-scaling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59599-score" class="post-score" title="current number of votes">0</div><span id="post-59599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey everyone,</p><p>just wondered: if i have a TCP packet with SYN flag set, there is a window size set in the RWIN header field (e.g. 0x2000) and there might be a window scale option in the options section (eg 0x030308 --&gt; WinScale, Len 3, shift by 8). From what I understand, RWin should be (0x2000 &lt;&lt; 8 = 0x20000 = 2097152 Byte) in this case. However, wireshark displays:</p><p>Window Size Value: 8192</p><p>[calculated window size: 8192]</p><p>Window Scale: 8 (Multiply by 256)</p><p>So Im wondering .. is either the value for RWin incorrect or is the RWin calculation incorrect? (or none of both and i just misunderstood something?)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpwindowscaling" rel="tag" title="see questions tagged &#39;tcpwindowscaling&#39;">tcpwindowscaling</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-tcpwindowsize" rel="tag" title="see questions tagged &#39;tcpwindowsize&#39;">tcpwindowsize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '17, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/464cfef52dca45936c8c2fdcc7c67f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DemoniacMilk&#39;s gravatar image" /><p><span>DemoniacMilk</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DemoniacMilk has no accepted answers">0%</span></p></div></div><div id="comments-container-59599" class="comments-container"></div><div id="comment-tools-59599" class="comment-tools"></div><div class="clear"></div><div id="comment-59599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59600"></span>

<div id="answer-container-59600" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59600-score" class="post-score" title="current number of votes">3</div><span id="post-59600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please have a look here: <a href="https://ask.wireshark.org/questions/51352/window-size-value-in-the-ack-packet-of-a-syn-synack-ack-handshake?page=1&amp;focusedAnswerId=51353#51353">https://ask.wireshark.org/questions/51352/window-size-value-in-the-ack-packet-of-a-syn-synack-ack-handshake?page=1&amp;focusedAnswerId=51353#51353</a> Inside the SYN packet the WindowSaling is never used (RFC). So Wireshark is absolutely correct.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '17, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-59600" class="comments-container"><span id="59607"></span><div id="comment-59607" class="comment"><div id="post-59607-score" class="comment-score"></div><div class="comment-text"><p>Ah thank you! So its more like "hey i would like to use window scaling if you support it" with a backwards-compatible, non-shifted window size in the header.</p></div><div id="comment-59607-info" class="comment-info"><span class="comment-age">(22 Feb '17, 06:33)</span> <span class="comment-user userinfo">DemoniacMilk</span></div></div><span id="59608"></span><div id="comment-59608" class="comment"><div id="post-59608-score" class="comment-score"></div><div class="comment-text"><p>Yes that is true!</p></div><div id="comment-59608-info" class="comment-info"><span class="comment-age">(22 Feb '17, 06:53)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-59600" class="comment-tools"></div><div class="clear"></div><div id="comment-59600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

