+++
type = "question"
title = "Capture machine dropping packets originating from it."
description = '''Hello, I have come across this weird behaviour. Session is a standard HTTPS session to a webserver on our internal network. The session starts fine : SYN, SYN/ACK, ACK Then TLS : Client Hello, Server Hello. The client Hello is Seq 1, Ack 1, Len 517 Server Hello is Seq 1, Ack 518, Len 137. The next p...'''
date = "2016-01-12T23:48:00Z"
lastmod = "2016-01-13T00:50:00Z"
weight = 49157
keywords = [ "capture", "drops" ]
aliases = [ "/questions/49157" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture machine dropping packets originating from it.](/questions/49157/capture-machine-dropping-packets-originating-from-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49157-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have come across this weird behaviour. Session is a standard HTTPS session to a webserver on our internal network.</p><p>The session starts fine : SYN, SYN/ACK, ACK Then TLS : Client Hello, Server Hello.</p><p>The client Hello is Seq 1, Ack 1, Len 517 Server Hello is Seq 1, Ack 518, Len 137.</p><p>The next packet in the capture file is from the client (which is also the machine Wireshark is running on) : Seq 569, Ack 138, Len 536. At this point WS complains about "TCP Previous Segment not captured", which makes sense given the Seq number... except that Wireshark is running on the client machine, so the network has not been involved at all in dropping this packet. So where did it go ??</p><p>The next two packets are a DUP ACK from the server, and then a retransmit by the client, which shows that it's not just that WS didn't capture the packet, it really did not go out over the network.</p><p>From there the session continues normally.</p><p>The client machine is Windows 7 Enterprise SP1 64bit, fairly up to date, and running nothing very out of the ordinary. Client app is Chrome 47. No system firewall enabled, only Symantec Antivirus (for its AV scanning ability, not firewall). WS version 2.0.0, WinPCAP 4.1.3.</p><p>Does anyone have a brilliant idea what could cause a client machine to eat a packet in the network stack like that ?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">capture drops</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '16, 23:48</strong></p><img src="https://secure.gravatar.com/avatar/2df2a2ad6f2f3f2ff608a539cbd28a5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeremy%20Gibbons&#39;s gravatar image" /><p>Jeremy Gibbons<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeremy Gibbons has no accepted answers">0%</span></p></div></div><div id="comments-container-49157" class="comments-container"></div><div id="comment-tools-49157" class="comment-tools"></div><div class="clear"></div><div id="comment-49157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49159"></span>

<div id="answer-container-49159" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49159-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please search through the site for similar questions. Many kinds of security software are capable to mysteriously steal packets, even if they are not primarily firewalls, so you may have to disable your Symantec Antivirus completely to verify. The other subject to search for here (but less likely to apply to your case as part of the traffic is visible to you and as the packet seems to really have been lost completely, not just in the capture) is "tcp chimney" and "tcp offloading".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '16, 00:50</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jan '16, 00:52</p></div></div><div id="comments-container-49159" class="comments-container"><span id="49160"></span><div id="comment-49160" class="comment"><div id="post-49160-score" class="comment-score"></div><div class="comment-text"><p>@sindy I did, but did not see anything matching these symptoms. TCP Offload / Chimney would seem to be more drastic (I would not be seeing any TCP traffic at all, whereas here I am missing a single packet that got gobbled up somewhere in the network stack). I am aware of most of the usual traps for common WS use so I'm really puzzled as to what is happening. I will try and have SEP be deactivated, and see if I can reproduce then. Thanks.</p></div><div id="comment-49160-info" class="comment-info"><span class="comment-age">(13 Jan '16, 01:13)</span> Jeremy Gibbons</div></div></div><div id="comment-tools-49159" class="comment-tools"></div><div class="clear"></div><div id="comment-49159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

