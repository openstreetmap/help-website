+++
type = "question"
title = "TCP Previous segment lost - Bug?"
description = '''Hi, I&#x27;ve come along some strange behavior of Wireshark. During a couple of captures, a lot of warnings appeared saying [TCP Previous segment lost]. Normally, this could occur is packets get lost or something, but you would suspect that the missing packets would be retransmitted some time later on (a...'''
date = "2011-01-07T03:00:00Z"
lastmod = "2011-01-10T06:43:00Z"
weight = 1664
keywords = [ "frames", "segment", "lost", "tcp", "previous" ]
aliases = [ "/questions/1664" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Previous segment lost - Bug?](/questions/1664/tcp-previous-segment-lost-bug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1664-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I've come along some strange behavior of Wireshark. During a couple of captures, a lot of warnings appeared saying [TCP Previous segment lost]. Normally, this could occur is packets get lost or something, but you would suspect that the missing packets would be retransmitted some time later on (after the number of bytes in the send window are send and the first (missing) packet is not acknowledged by that time). Looking in the capture file I see the following (exported to CSV to make it clear text):</p><pre><code>1611    21.736.504  10.98.18.127    10.74.37.2  TCP 445 1641    [Continuation to #1590] 445 &gt; 1641 [ACK] Seq=1387288 Ack=7262 Win=65535 Len=1380    1387288 1380    1388668 
1612    21.736.620  10.98.18.127    10.74.37.2  TCP 445 1641    [Continuation to #1590] 445 &gt; 1641 [ACK] Seq=1388668 Ack=7262 Win=65535 Len=1380    1388668 1380    1390048 
1613    21.736.718  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1361068 Win=65535 Len=0   7262    0   7262    
1614    21.736.769  10.98.18.127    10.74.37.2  TCP 445 1641    [Continuation to #1590] 445 &gt; 1641 [ACK] Seq=1390048 Ack=7262 Win=65535 Len=1380    1390048 1380    1391428 
1615    21.736.877  10.98.18.127    10.74.37.2  TCP 445 1641    [Continuation to #1590] 445 &gt; 1641 [ACK] Seq=1391428 Ack=7262 Win=65535 Len=1380    1391428 1380    1392808 
1616    21.736.992  10.98.18.127    10.74.37.2  TCP 445 1641    [Continuation to #1590] 445 &gt; 1641 [ACK] Seq=1392808 Ack=7262 Win=65535 Len=1380    1392808 1380    1394188 
1617    21.737.116  10.98.18.127    10.74.37.2  TCP 445 1641    [Continuation to #1590] [TCP Previous segment lost] 445 &gt; 1641 [ACK] Seq=1396948 Ack=7262 Win=65535 Len=1380    1396948 1380    1398328 
1618    21.737.232  10.98.18.127    10.74.37.2  TCP 445 1641    [Continuation to #1590] [TCP Previous segment lost] 445 &gt; 1641 [ACK] Seq=1403848 Ack=7262 Win=65535 Len=1380    1403848 1380    1405228 
1619    21.737.349  10.98.18.127    10.74.37.2  TCP 445 1641    [Continuation to #1590] [TCP Previous segment lost] 445 &gt; 1641 [ACK] Seq=1413508 Ack=7262 Win=65535 Len=1380    1413508 1380    1414888 
1620    21.737.889  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1373488 Win=65535 Len=0   7262    0   7262    12
1621    21.737.891  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1376248 Win=65535 Len=0   7262    0   7262    14
1622    21.737.894  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1380388 Win=65535 Len=0   7262    0   7262    17
1623    21.737.896  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1384528 Win=65535 Len=0   7262    0   7262    20
1624    21.737.897  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1388668 Win=65535 Len=0   7262    0   7262    23
1625    21.737.899  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1392808 Win=65535 Len=0   7262    0   7262    27
1626    21.737.903  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1396948 Win=65535 Len=0   7262    0   7262    29
1627    21.737.904  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1401088 Win=65535 Len=0   7262    0   7262    ?
1628    21.738.779  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1405228 Win=65535 Len=0   7262    0   7262    30
1629    21.738.781  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1407988 Win=65535 Len=0   7262    0   7262    ?
1630    21.738.783  10.74.37.2  10.98.18.127    TCP 1641    445 1641 &gt; 445 [ACK] Seq=7262 Ack=1412128 Win=65535 Len=0   7262    0   7262    ?
1631    21.738.785  10.74.37.2  10.98.18.127    TCP 1641    445 [TCP ACKed lost segment] 1641 &gt; 445 [ACK] Seq=7262 Ack=1416268 Win=65535 Len=0  7262    0   7262    ?
1632    21.738.787  10.74.37.2  10.98.18.127    TCP 1641    445 [TCP ACKed lost segment] 1641 &gt; 445 [ACK] Seq=7262 Ack=1419811 Win=65535 Len=0  7262    0   7262    
1633    21.738.789  10.74.37.2  10.98.18.127    SMB 1641    445 Read AndX Request, FID: 0x400d, 61440 bytes at offset 1413120   
1634    21.739.728  10.98.18.127    10.74.37.2  SMB 445 1641    Read AndX Response, FID: 0x400d, 61440 bytes        </code></pre><p>Frame 1616 would suggest that the next sequencenr would be 1394188, but it's 1396948 so indeed it seems like a packet is missing. However, in frame 1627 sequence 1401088 is acknowledges meaning that all bytes before are received correctly. But I cannot find any (re)tranmission of the frame with sequence 1394188 so what's going on here? Is this a bug in Wireshark?</p><p>Hope someone can answer this for me</p></div><div id="question-tags" class="tags-container tags">frames segment lost tcp previous</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '11, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/77561cf8258d1fb9930f1575820e8c34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lutetia&#39;s gravatar image" /><p>lutetia<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lutetia has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jan '11, 03:06</p></div></div><div id="comments-container-1664" class="comments-container"><span id="1666"></span><div id="comment-1666" class="comment"><div id="post-1666-score" class="comment-score"></div><div class="comment-text"><p>Is wireshark showing any packet drops on capture? Also are you using a teaming NIC that might be load-balancing (and some packets are travelling across the other physical NIC)?</p></div><div id="comment-1666-info" class="comment-info"><span class="comment-age">(07 Jan '11, 03:36)</span> martyvis</div></div></div><div id="comment-tools-1664" class="comment-tools"></div><div class="clear"></div><div id="comment-1664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1665"></span>

<div id="answer-container-1665" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1665-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm curious if it is possible that either the traffic rate was to fast for Wireshark to deal with or if there was some other path that that packet could have taken. The receiver certainly received 2 frames that would follow 1616 as indicated by the non-duplicate ack's that follow. This looks to me like wireshark some how is not getting all of the packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '11, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1665" class="comments-container"></div><div id="comment-tools-1665" class="comment-tools"></div><div class="clear"></div><div id="comment-1665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1667"></span>

<div id="answer-container-1667" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1667-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Paul,there was no other path, and I've seen this in five or six captures I've made. I've used a Dell laptop with a 1 Gbps Broadcom network interface on a spawnport of a 3750 Cisco switch, to monitor all traffic on another 1 Gbps link on that switch. In the Capture options I've filtered one IP address to capture (10.74.37.2 in this case). That PC was attached to a 100 Mbps link so it's hard to believe that my laptop couldn't see all traffic from that PC. So to me it looks like some bug in Wireshark.</p><p>Regards</p><p>John Lasschuit</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '11, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/77561cf8258d1fb9930f1575820e8c34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lutetia&#39;s gravatar image" /><p>lutetia<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lutetia has no accepted answers">0%</span></p></div></div><div id="comments-container-1667" class="comments-container"><span id="1668"></span><div id="comment-1668" class="comment"><div id="post-1668-score" class="comment-score">1</div><div class="comment-text"><p>If you span 1 Gbit link, you will get both RX and TX frames, resulting in 2 Gbit/s of traffic on a fully utilized link. This will oversubscribe the spanport. Filtering on one specific IP addres takes place on the capturing host <em>after</em> the switch has dropped packets due to the oversubscription. It does not matter that the filtered host only has a 100Mbit, unless you are able to filter <em>before</em> aggregating the two 1 Gbit/s flows to a 1 Gbit/s port.</p><p>You can verify this by checking the counters on the destination span port.</p></div><div id="comment-1668-info" class="comment-info"><span class="comment-age">(07 Jan '11, 05:30)</span> SYN-bit ♦♦</div></div><span id="1669"></span><div id="comment-1669" class="comment"><div id="post-1669-score" class="comment-score"></div><div class="comment-text"><p>Of course it would be easier to span the 100 Mbit/s server port to your 1 Gbit/s monitor port :-)</p></div><div id="comment-1669-info" class="comment-info"><span class="comment-age">(07 Jan '11, 05:33)</span> SYN-bit ♦♦</div></div><span id="1672"></span><div id="comment-1672" class="comment"><div id="post-1672-score" class="comment-score"></div><div class="comment-text"><p>SYNbit, I think you're right. The ports appeared to be configured as fixed 100 Mbps FD (not Gigabit) however, the same you've pointed out applies. Unfortunaly the counters are only five minute intervals so they're gone. On Monday we try to configure the main and span port as auto sensing, hoping that the real port (connection to provider) will come up as 100 Mbps FD and the span port as 1 Gbps FD (because the laptop is 1 Gbps). Let's see if Cisco supports this :-)</p></div><div id="comment-1672-info" class="comment-info"><span class="comment-age">(07 Jan '11, 09:24)</span> lutetia</div></div><span id="1676"></span><div id="comment-1676" class="comment"><div id="post-1676-score" class="comment-score"></div><div class="comment-text"><p>The drop counters don't use 5 min moving weighted average. So if you look the counters, you'll see the drops. This is why I presented a case like this in Sharkfest 2010. It is possible to infer a lot by looking at the traces. Looking at IP ID can help you gather some information etc. But to me, it looks like the span dropped it.</p></div><div id="comment-1676-info" class="comment-info"><span class="comment-age">(07 Jan '11, 13:29)</span> hansangb</div></div><span id="1683"></span><div id="comment-1683" class="comment"><div id="post-1683-score" class="comment-score"></div><div class="comment-text"><p>I agree with and second what hansangb is stating. Those drop counters will not reset or loop every 5 minutes. They may reset when the interface bounces though. It certainly looks like Wireshark does not have a complete view. This is one drawback of aggregating 2 direction traffic into a span port that does not have 2x the output capacity.</p></div><div id="comment-1683-info" class="comment-info"><span class="comment-age">(08 Jan '11, 08:48)</span> Paul Stewart</div></div></div><div id="comment-tools-1667" class="comment-tools"></div><div class="clear"></div><div id="comment-1667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1693"></span>

<div id="answer-container-1693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1693-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Clear the 3750 interface counters and then do a</p><p>"show interface counter errors"</p><p>to check for drops on the span target port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '11, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/d5aa09edfeeb0600f74a72e63806f227?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erics&#39;s gravatar image" /><p>erics<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erics has no accepted answers">0%</span></p></div></div><div id="comments-container-1693" class="comments-container"></div><div id="comment-tools-1693" class="comment-tools"></div><div class="clear"></div><div id="comment-1693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

