+++
type = "question"
title = "tracing pcap file, relation between ack and seq and len"
description = '''Hello, i have this problem while tracing this Pcap file, i am trying to understand the relation between ack and seq and len , i thought i understand it but check packet 7 , i don&#x27;t understand ..can anyone explain to me please what is happening here ? i thought that the ack = seq no. + Len , but here...'''
date = "2015-05-26T15:28:00Z"
lastmod = "2015-05-26T21:39:00Z"
weight = 42680
keywords = [ "wireshark", "trace", "sequencenumber", "acknowledgement" ]
aliases = [ "/questions/42680" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tracing pcap file, relation between ack and seq and len](/questions/42680/tracing-pcap-file-relation-between-ack-and-seq-and-len)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42680-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i have this problem while tracing this Pcap file, i am trying to understand the relation between ack and seq and len , i thought i understand it but check packet 7 , i don't understand ..can anyone explain to me please what is happening here ? i thought that the ack = seq no. + Len <img src="https://osqa-ask.wireshark.org/upfiles/q.png" alt="alt text" />, but here in line 7 what i understood doesn't apply!</p></div><div id="question-tags" class="tags-container tags">wireshark trace sequencenumber acknowledgement</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '15, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p>yas1234<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-42680" class="comments-container"></div><div id="comment-tools-42680" class="comment-tools"></div><div class="clear"></div><div id="comment-42680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42688"></span>

<div id="answer-container-42688" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42688-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>you have captured locally, which means that you see outgoing packets that are much larger than they actually were. This is caused by the network card performing segment offloading. The ACK you see is for a much smaller packet (which is correct). The big packet in line 5 isn't what was really sent.</p><p>If you try to track sequence and ack numbers, do NOT use captures you've taken locally. Use a third PC to record what the other two are sending.</p><p>Also see <a href="https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/">https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '15, 21:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42688" class="comments-container"></div><div id="comment-tools-42688" class="comment-tools"></div><div class="clear"></div><div id="comment-42688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

