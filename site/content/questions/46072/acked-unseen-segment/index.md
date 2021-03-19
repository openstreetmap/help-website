+++
type = "question"
title = "acked unseen segment"
description = '''what last packet is marked as it is? Is it ok?   1.1.1.1 2.2.2.2 TCP 74 49538?443 [SYN] Seq=0 Win=8192 Len=0 MSS=1420 WS=4 SACK_PERM=1 TSval=149611 TSecr=0  2.2.2.2 1.1.1.1 TCP 74 443?49538 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1 TSval=979974123 TSecr=149611  1.1.1.1 2.2.2....'''
date = "2015-09-23T03:37:00Z"
lastmod = "2015-09-23T03:40:00Z"
weight = 46072
keywords = [ "acked", "unseen" ]
aliases = [ "/questions/46072" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [acked unseen segment](/questions/46072/acked-unseen-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46072-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>what last packet is marked as it is? Is it ok?</p><pre><code>1.1.1.1        2.2.2.2                             TCP      74     49538?443 [SYN] Seq=0 Win=8192 Len=0 MSS=1420 WS=4 SACK_PERM=1 TSval=149611 TSecr=0            
2.2.2.2           1.1.1.1                          TCP      74     443?49538 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1 TSval=979974123 TSecr=149611            
1.1.1.1        2.2.2.2                             TCP      66     49538?443 [ACK] Seq=1 Ack=1 Win=66176 Len=0 TSval=149613 TSecr=979974123            
1.1.1.1        2.2.2.2                             SSL      285    [Packet size limited during capture]                                       
2.2.2.2           1.1.1.1                          SSL      1474   [Packet size limited during capture]                                       
2.2.2.2           1.1.1.1                          SSL      1474   Continuation Data[Packet size limited during capture]                      
1.1.1.1        2.2.2.2                             TCP      66     49538?443 [ACK] Seq=220 Ack=2817 Win=66176 Len=0 TSval=149616 TSecr=979974126            
2.2.2.2           1.1.1.1                          TCP      409    443?49538 [PSH, ACK] Seq=2817 Ack=220 Win=66048 Len=343 TSval=979974128 TSecr=149616[Packet size limited during capture]            
1.1.1.1        2.2.2.2                             TCP      66     49538?443 [ACK] Seq=220 Ack=3160 Win=65832 Len=0 TSval=149637 TSecr=979974128            
1.1.1.1        2.2.2.2                             TCP      66     49538?443 [FIN, ACK] Seq=220 Ack=3160 Win=65832 Len=0 TSval=149674 TSecr=979974128            
2.2.2.2           1.1.1.1                          TCP      60     443?49538 [RST, ACK] Seq=3160 Ack=221 Win=0 Len=0                        
1.1.1.1        2.2.2.2                             TCP      60     [TCP ACKed unseen segment] 49538?443 [RST, ACK] Seq=221 Ack=3161 Win=0 Len=0            </code></pre></div><div id="question-tags" class="tags-container tags">acked unseen</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '15, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/92b8d8aae513f16380dd2db84828cb8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dragec&#39;s gravatar image" /><p>Dragec<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dragec has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Sep '15, 04:01</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-46072" class="comments-container"></div><div id="comment-tools-46072" class="comment-tools"></div><div class="clear"></div><div id="comment-46072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46073"></span>

<div id="answer-container-46073" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46073-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It just means that the receiver acknowledged a packet that you did not capture. So your capture device wasn't fast enough to capture all packets, but the real communication worked fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '15, 03:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-46073" class="comments-container"><span id="46074"></span><div id="comment-46074" class="comment"><div id="post-46074-score" class="comment-score"></div><div class="comment-text"><p>problem is that it is highly unlikely that any packet is lost. So I'd like to know what are the other possible answers. Mybe firewall somehow messed communication? Or WS does not interpret something correctlly?</p></div><div id="comment-46074-info" class="comment-info"><span class="comment-age">(23 Sep '15, 03:43)</span> Dragec</div></div><span id="46075"></span><div id="comment-46075" class="comment"><div id="post-46075-score" class="comment-score">1</div><div class="comment-text"><p>The packet was <strong>not</strong> lost. You just did not capture it. But you captured the acknowledgement for it, so Wireshark tells you that there was something that wasn't captured but not lost.</p><p>Your firewall is fine, Wireshark is fine. Your capture device is too slow.</p></div><div id="comment-46075-info" class="comment-info"><span class="comment-age">(23 Sep '15, 03:45)</span> Jasper ♦♦</div></div></div><div id="comment-tools-46073" class="comment-tools"></div><div class="clear"></div><div id="comment-46073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

