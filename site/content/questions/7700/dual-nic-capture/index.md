+++
type = "question"
title = "dual nic capture"
description = '''IS there a way to capture from 2 active 10 GB interfaces? I have set up a Linux server with to 10 GB interface to monitor 2 10 GB circuits between our 2 data centers. Interfaces are unnumbered ( layer 2), 1 interface to each switches the circuits terminate on'''
date = "2011-11-29T11:28:00Z"
lastmod = "2011-11-29T14:32:00Z"
weight = 7700
keywords = [ "nic", "dual", "capture" ]
aliases = [ "/questions/7700" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dual nic capture](/questions/7700/dual-nic-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7700-score" class="post-score" title="current number of votes">0</div><span id="post-7700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>IS there a way to capture from 2 active 10 GB interfaces? I have set up a Linux server with to 10 GB interface to monitor 2 10 GB circuits between our 2 data centers. Interfaces are unnumbered ( layer 2), 1 interface to each switches the circuits terminate on</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span> <span class="post-tag tag-link-dual" rel="tag" title="see questions tagged &#39;dual&#39;">dual</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '11, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/2f998da3de78b2710242207b49133ac1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sjweinstein&#39;s gravatar image" /><p><span>sjweinstein</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sjweinstein has no accepted answers">0%</span></p></div></div><div id="comments-container-7700" class="comments-container"></div><div id="comment-tools-7700" class="comment-tools"></div><div class="clear"></div><div id="comment-7700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7701"></span>

<div id="answer-container-7701" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7701-score" class="post-score" title="current number of votes">0</div><span id="post-7701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depending on the data rate and the write performance of the Linux server it might work. You will have to have your disk array to write at the speed of something like 1,2 to 1,5GByte/s if your two 10G links are really full, and even more if you're trying to capture with a full duplex tap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '11, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7701" class="comments-container"><span id="7703"></span><div id="comment-7703" class="comment"><div id="post-7703-score" class="comment-score"></div><div class="comment-text"><p>I understand the need fro fast drive, etc, but how can i have 2 nics actively capturing, the GUI only allows starting a capture on one NIC at a time. I am not that literate with UNIX/LINUX so how would i configure a pseudo(?) interface taht would be just these two interfaces?</p></div><div id="comment-7703-info" class="comment-info"><span class="comment-age">(29 Nov '11, 12:27)</span> <span class="comment-user userinfo">sjweinstein</span></div></div><span id="7704"></span><div id="comment-7704" class="comment"><div id="post-7704-score" class="comment-score"></div><div class="comment-text"><p>I converted your answer to a comment.</p><p>You could start two capture processes, either by starting two instances of Wireshark, or, even better, by capturing with two dumpcap processes at the same time.</p><p>If you want one capture to aggregate your two NICs you might try that with the "All Interfaces" Pseudo interface offered on UNIX/LINUX, and I heard the Wireshark Developer version 1.7 can do that on Windows, too, but I haven't tried it.</p><p>Or you merge your two traces from separate NICs with mergecap afterwards, but that might give some funny results.</p></div><div id="comment-7704-info" class="comment-info"><span class="comment-age">(29 Nov '11, 12:32)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="7705"></span><div id="comment-7705" class="comment"><div id="post-7705-score" class="comment-score"></div><div class="comment-text"><p>Indeed in 1.7.0 you can capture from multiple interfaces at the same time.</p><p>All solutions based on standard NIC's will give you funny results, no matter how you capture and/or combine the packets. This is due to the interrupt handling. NIC's will queue the packets in their buffers and on each interrupt handling the OS will read the whole buffer. This can result in ACK's being seen before the packet was seen which it ACKs (if they arrive at different NICs).</p></div><div id="comment-7705-info" class="comment-info"><span class="comment-age">(29 Nov '11, 12:43)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="7709"></span><div id="comment-7709" class="comment"><div id="post-7709-score" class="comment-score"></div><div class="comment-text"><p>The "all interfaces" pseudo-interface is <em>only</em> available on Linux; it's <em>not</em> available on other UN*Xes (their underlying capture mechanisms, unlike Linux's mechanism, must be bound to a particular interface).</p></div><div id="comment-7709-info" class="comment-info"><span class="comment-age">(29 Nov '11, 14:32)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-7701" class="comment-tools"></div><div class="clear"></div><div id="comment-7701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

