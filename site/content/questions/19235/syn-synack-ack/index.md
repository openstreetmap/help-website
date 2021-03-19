+++
type = "question"
title = "SYN - SYN/ACK - ACK"
description = '''Hello, I&#x27;m troubleshooting an issue where I need to figure out if the some SYN/ACK that I&#x27;m seeing are in response to an specific SYN. I took to independent captures, in two different locations and simultaneously, I can see the SYN from my laptop, but I don&#x27;t see any SYN/ACK anywhere in the same cap...'''
date = "2013-03-06T09:52:00Z"
lastmod = "2013-03-06T10:19:00Z"
weight = 19235
keywords = [ "ack", "handshake", "3way", "syn" ]
aliases = [ "/questions/19235" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SYN - SYN/ACK - ACK](/questions/19235/syn-synack-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19235-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm troubleshooting an issue where I need to figure out if the some SYN/ACK that I'm seeing are in response to an specific SYN.</p><p>I took to independent captures, in two different locations and simultaneously, I can see the SYN from my laptop, but I don't see any SYN/ACK anywhere in the same capture, when I check the other capture I notice that there are many SYN/ACK but I don't know how to match one of those SYN/ACK to the SYN that the computer sent.</p><p>Can you please help me?</p></div><div id="question-tags" class="tags-container tags">ack handshake 3way syn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '13, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/3ec9add3f6ceb792756b1227b1266919?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wil1323&#39;s gravatar image" /><p>wil1323<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wil1323 has no accepted answers">0%</span></p></div></div><div id="comments-container-19235" class="comments-container"></div><div id="comment-tools-19235" class="comment-tools"></div><div class="clear"></div><div id="comment-19235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19239"></span>

<div id="answer-container-19239" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19239-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to disable the relative Sequence numbers for the TCP protocol first. You can do that in the preferences -&gt; Protocols sections, or by right clicking the TCP layer in any packet that has TCP inside. Matching packets on multiple locations usually works by finding the same two IPs talking on the same two ports with each other (a "Socket Pair"). Then, try to find the same TCP Sequence numbers of a packet in one trace in the other trace. Sequence numbers are usually unique inside one TCP conversation unless there is so much data transfered that it forces the sequence number to wrap around.</p><p>If you can find the same packet containing the same socket pair and the same TCP sequence number, you've got it. If you can't find it anywhere, it's probaby not in the trace file. It might still have been on "the wire" but wasn't captured for performance or other reasons. You can usually tell if that is the case if you see the two nodes talking happily (meaning: without retransmissions and duplicate acks) with each other even though there seem to be missing packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '13, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Mar '13, 15:15</p></div></div><div id="comments-container-19239" class="comments-container"><span id="19241"></span><div id="comment-19241" class="comment"><div id="post-19241-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, Can we decode it with stream index?</p><p>Let us say the syn is having stream index "n" and obviously the related syn-ack will have index "n" Correct me if i am wrong</p><p>Thanks</p></div><div id="comment-19241-info" class="comment-info"><span class="comment-age">(06 Mar '13, 10:37)</span> krishnayeddula</div></div><span id="19242"></span><div id="comment-19242" class="comment"><div id="post-19242-score" class="comment-score"></div><div class="comment-text"><p>Going by stream index only works if you only have one trace file. In that case you'll find all packets belonging to one conversation by filtering on its stream index.</p><p>Stream index will not work if you compare traces, because the index always starts fresh for each trace, and you can't tell if the same conversation will have the same stream index. If it is, its a pretty rare coincidence, and I wouldn't rely on being that lucky. Better use a conversation filter that contains both IPs and both ports.</p></div><div id="comment-19242-info" class="comment-info"><span class="comment-age">(06 Mar '13, 10:40)</span> Jasper ♦♦</div></div><span id="19243"></span><div id="comment-19243" class="comment"><div id="post-19243-score" class="comment-score"></div><div class="comment-text"><p>Got it thanks</p></div><div id="comment-19243-info" class="comment-info"><span class="comment-age">(06 Mar '13, 10:42)</span> krishnayeddula</div></div><span id="19245"></span><div id="comment-19245" class="comment"><div id="post-19245-score" class="comment-score"></div><div class="comment-text"><p>Hello.</p><p>One more question, by using the filter tcp.flags == 0x0012, I'm able to find all [ SYN,ACK ] packets in one capture, so now wireshark lists all SYN,ACK, but how can I do a look up in the other sniffer capture that I took, to find out what syn,ack corresponds to what syn.</p><p>Thank you again.</p></div><div id="comment-19245-info" class="comment-info"><span class="comment-age">(06 Mar '13, 13:06)</span> wil1323</div></div><span id="19246"></span><div id="comment-19246" class="comment"><div id="post-19246-score" class="comment-score"></div><div class="comment-text"><p>You'll have to compare absolute TCP sequence numbers. You could add a custom column for the sequence number to have the numbers listed for each SYN/ACK. Easiest way to do is to select the sequence number in the decode pane of any TCP packet and then use the popup menu to "apply as column".</p><p>If you have one SYN/ACK you want to track in the other file you could just filter or search for it, by using "tcp.seq==NUMBER", where "NUMBER" is the number you look for.</p></div><div id="comment-19246-info" class="comment-info"><span class="comment-age">(06 Mar '13, 13:34)</span> Jasper ♦♦</div></div></div><div id="comment-tools-19239" class="comment-tools"></div><div class="clear"></div><div id="comment-19239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

