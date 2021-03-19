+++
type = "question"
title = "TCP Retransmission Behavior"
description = '''I have uploaded a sample trace to: http://www.cloudshark.org/captures/b6c6ccb4d513 In this trace, which was just an FTP GET between two hosts and I pulled the cable on the client in the middle of the transfer, I have some questions as to TCP Retransmission behavior that hopefully someone can help me...'''
date = "2012-07-30T17:49:00Z"
lastmod = "2012-07-31T02:02:00Z"
weight = 13146
keywords = [ "retransmissions", "tcp" ]
aliases = [ "/questions/13146" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Retransmission Behavior](/questions/13146/tcp-retransmission-behavior)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13146-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have uploaded a sample trace to: <a href="http://www.cloudshark.org/captures/b6c6ccb4d513">http://www.cloudshark.org/captures/b6c6ccb4d513</a></p><p>In this trace, which was just an FTP GET between two hosts and I pulled the cable on the client in the middle of the transfer, I have some questions as to TCP Retransmission behavior that hopefully someone can help me better understand.</p><p>Since cable was pulled in this example there was multiple successive packets dropped from server to client that ulitmatley did not get any ACK, so RTO fired.</p><p>First dropped packet is #3664 and its initial retransmission is 621ms later packet #3773. The second retrans for this packet is #3774 with 984ms delta from #3773. Shouldn't this double up and have been 1.2s? Third retrans for this first dropped packet is #3775 with 1.9s delta from #3774. OK this is a lot closer to double backoff but the payload is smaller, subset of original payload (524 bytes versus 1448 bytes). Why is this so?</p><p>Second dropped packet is #3666, which is put on the wire 29us after first dropped packet (#3664). My (incorrect) assumption was that this packet should have similar RTO and would be retransmitted about same time first dropped packet was retrans, but it was not. Its initial retrans was #3779 with delta from original packet of 16.5s and its payload was only 12 bytes versus 600 byte payload of original packet.</p><p>My best guess here is that TCP doesn't want to flood the network with a bunch of retransmissions for a given tcp connection/stream if it isn't getting an ACK for the first lost packet until some timer is past. Not sure why the payload is smaller though.</p><p>This leads me to my last question, which I believe must be tied to the answer. Wireshark shows in its TCP Analysis Flags section of a retransmitted packet that the RTO is based on a delta from a certain frame, which is usually not the frame of the original lost packet. It seems to be based on a frame at the end of a "train" of data or more likely a full tcp window of data sent. I looked at RFC 2988 and it's not clear to me how often the RTO timer is applied. Up until now I thought each packet had its own RTO timer but now I'm not so sure anymore. If anything I'm more confused.</p><p>(5.1) Every time a packet containing data is sent (including a retransmission), if the timer is not running, start it running so that it will expire after RTO seconds (for the current value of RTO).</p><p>(5.2) When all outstanding data has been acknowledged, turn off the retransmission timer.</p><p>(5.3) When an ACK is received that acknowledges new data, restart the retransmission timer so that it will expire after RTO seconds (for the current value of RTO).</p><p>I think the "if the timer is not running, start it" is making me think differently or maybe I'm just thinking too much about it.</p><p>I appreciate any feedback on this. I thought I understood this better than I do and hope this isn't too much a a newbie question.</p><p>Kind Regards</p></div><div id="question-tags" class="tags-container tags">retransmissions tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '12, 17:49</strong></p><img src="https://secure.gravatar.com/avatar/f3d0910625626ca9d6009a27d406a83f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="9691ekiM&#39;s gravatar image" /><p>9691ekiM<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="9691ekiM has no accepted answers">0%</span></p></div></div><div id="comments-container-13146" class="comments-container"></div><div id="comment-tools-13146" class="comment-tools"></div><div class="clear"></div><div id="comment-13146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13178"></span>

<div id="answer-container-13178" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13178-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry to disappoint you here, but RFCs are one thing and what the TCP stacks out there really do something else completely. You can probably drive yourself crazy if you try to find out why a stack is doing something, as it would require you to disect the stack code to tell why it does it. One good example is the doubling of the retransmission delta - some stacks do it exactly like in the RFCs, others don't care and base it on whatever magical things they do to consider the best way of retransmitting data.</p><p>This kind of thing has been a topic on this year's Sharkfest conference, and maybe you want to look at a presentation @Landi did, which you can find <a href="http://sharkfest.wireshark.org/sharkfest.12/">here</a> - take a look at presentation <strong>A-18: Effects of Receiver-Side Window Scaling on Enterprise Networks</strong>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '12, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13178" class="comments-container"><span id="13186"></span><div id="comment-13186" class="comment"><div id="post-13186-score" class="comment-score"></div><div class="comment-text"><p>To get a sense of the "real world details" you might want to look at "TCP/IP Illustrated" by Stevens for much discussion on retransmission timers and etc.</p><p>The book (1st edition) shows examples from the real world (circa 1994) of the complexity of actual TCP implementations.</p><p>(I haven't looked at the recent 2nd edition but I would expect similar detail).</p><p>Also: searching for '"TCP/IP Illustrated" "retransmission timer" "exponential backoff"' and etc will provide some extracts from the book.</p></div><div id="comment-13186-info" class="comment-info"><span class="comment-age">(31 Jul '12, 06:45)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-13178" class="comment-tools"></div><div class="clear"></div><div id="comment-13178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

