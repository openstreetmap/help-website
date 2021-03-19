+++
type = "question"
title = "MSS value negotiated during ftp-data session establishment but wireshark shows larger blocks sent by server"
description = '''As you can see at image during ftp-data session establishment size of MSS was negotiated equal to 1360 bytes. But then transfer started and server sends blocks much greater than MSS value, and greater than MTU (1500) value as well. Is there some missunderstanding of Wireshark output or how can be th...'''
date = "2015-05-26T23:33:00Z"
lastmod = "2015-05-27T00:44:00Z"
weight = 42691
keywords = [ "ftp", "mss", "tcp", "wireshark" ]
aliases = [ "/questions/42691" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [MSS value negotiated during ftp-data session establishment but wireshark shows larger blocks sent by server](/questions/42691/mss-value-negotiated-during-ftp-data-session-establishment-but-wireshark-shows-larger-blocks-sent-by-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42691-score" class="post-score" title="current number of votes">0</div><span id="post-42691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As you can see at image during ftp-data session establishment size of MSS was negotiated equal to 1360 bytes. But then transfer started and server sends blocks much greater than MSS value, and greater than MTU (1500) value as well. Is there some missunderstanding of Wireshark output or how can be this justified?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_tcp_q_Csi5U4a.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span> <span class="post-tag tag-link-mss" rel="tag" title="see questions tagged &#39;mss&#39;">mss</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '15, 23:33</strong></p><img src="https://secure.gravatar.com/avatar/4f86795c7a782fccae8a0b7bd270d1d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mongolio&#39;s gravatar image" /><p><span>mongolio</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mongolio has no accepted answers">0%</span></p></img></div></div><div id="comments-container-42691" class="comments-container"></div><div id="comment-tools-42691" class="comment-tools"></div><div class="clear"></div><div id="comment-42691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42693"></span>

<div id="answer-container-42693" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42693-score" class="post-score" title="current number of votes">1</div><span id="post-42693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mongolio has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>probably <a href="https://en.wikipedia.org/wiki/Large_segment_offload">Large Segment Offload</a>. Check the same session at the receiver, you then see the difference your NIC makes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '15, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-42693" class="comments-container"></div><div id="comment-tools-42693" class="comment-tools"></div><div class="clear"></div><div id="comment-42693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

