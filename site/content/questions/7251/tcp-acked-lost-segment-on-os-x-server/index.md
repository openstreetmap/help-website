+++
type = "question"
title = "TCP ACKed lost segment on OS X server"
description = '''I&#x27;m running wireshark to capture packets on a mac os X system and I can see TCP ACKed lost segment packets on a TCP connection to a client. is there a reason why it happens? I thought if i&#x27;m capturing on the server I will see all the packets that are sent to the client'''
date = "2011-11-06T03:23:00Z"
lastmod = "2011-11-07T05:23:00Z"
weight = 7251
keywords = [ "tcp" ]
aliases = [ "/questions/7251" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP ACKed lost segment on OS X server](/questions/7251/tcp-acked-lost-segment-on-os-x-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7251-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running wireshark to capture packets on a mac os X system and I can see TCP ACKed lost segment packets on a TCP connection to a client. is there a reason why it happens? I thought if i'm capturing on the server I will see all the packets that are sent to the client</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '11, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/5d64d21de6598960bf2db61f1ca705cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddayan&#39;s gravatar image" /><p>ddayan<br />
<span class="score" title="41 reputation points">41</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddayan has no accepted answers">0%</span></p></div></div><div id="comments-container-7251" class="comments-container"></div><div id="comment-tools-7251" class="comment-tools"></div><div class="clear"></div><div id="comment-7251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7254"></span>

<div id="answer-container-7254" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7254-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>An ACK to a lost segment means that you see an acknowledge of a packet that hasn't made it into the capture file. If you're capturing on the server it probably means that you had too much traffic going in and out for Wireshark to be able to capture it all for performance reasons. Whenever that happens you'll see ACKs to lost segments, because it was there but you didn't capture the segment.</p><p>Take a look at the status bar after stopping the capture; there should be a "Drop" counter that tells you how many packets were lost due to insufficient capture performance. If it is anything above zero your capture device is too slow to get it all.</p><p>Try capturing with dumpcap or other tools that do not have the overhead of Wireshark displaying packets in real time (or turn of as much of that as possible: displaying in real time, color coding, life statistics etc).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '11, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7254" class="comments-container"><span id="7259"></span><div id="comment-7259" class="comment"><div id="post-7259-score" class="comment-score"></div><div class="comment-text"><p>i tried to use tcpdump -nnvvXSs 1514 -i en0 -w good_con_7_11 I receive: 0 packets captured 0 packets received by filter 0 packets dropped by kernel</p><p>I still get ACK lost segments (although now I receive smaller amount), anything else that I could do?</p></div><div id="comment-7259-info" class="comment-info"><span class="comment-age">(07 Nov '11, 04:20)</span> ddayan</div></div><span id="7260"></span><div id="comment-7260" class="comment"><div id="post-7260-score" class="comment-score"></div><div class="comment-text"><p>Ok, in that case you're probably capturing at a SPAN port, which is slammed shut with packets and starts dropping on the SPAN port itself. The only thing you can do is span the data to a faster port (for example from 100MBit to 1G or 1G to 10G), but that is often not possible (especially for the 1-&gt;10G). Otherwise you need to reduce the amount of packets going to the SPAN port, or go for a TAP, but that usually requires a FDX capture solution unless you deploy an aggregation TAP (which might drop, once again).</p></div><div id="comment-7260-info" class="comment-info"><span class="comment-age">(07 Nov '11, 04:57)</span> Jasper ♦♦</div></div></div><div id="comment-tools-7254" class="comment-tools"></div><div class="clear"></div><div id="comment-7254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7261"></span>

<div id="answer-container-7261" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7261-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just to make sure that we are not overlooking the obvious:</p><p>Is your server using exactly one network card?</p><p>If you have more than one NIC the packets might be received over one interface and the ACKs are transmitted over another card.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '11, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-7261" class="comments-container"><span id="7262"></span><div id="comment-7262" class="comment"><div id="post-7262-score" class="comment-score"></div><div class="comment-text"><p>yes only one NIC (it's a laptop)</p></div><div id="comment-7262-info" class="comment-info"><span class="comment-age">(07 Nov '11, 06:16)</span> ddayan</div></div></div><div id="comment-tools-7261" class="comment-tools"></div><div class="clear"></div><div id="comment-7261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

