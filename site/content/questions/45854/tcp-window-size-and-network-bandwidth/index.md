+++
type = "question"
title = "TCP Window Size and Network Bandwidth"
description = '''I have added 2 more captures (better) as examples. Each capture transfers the same file from the same source (Unix server). The client side is either a Windows 7 laptop or a MacBook Pro. https://www.dropbox.com/s/216fehk3p75ws45/MacBookSCPv2.pcapng?dl=0 https://www.dropbox.com/s/boxkdcmsmrsyb1l/Wind...'''
date = "2015-09-15T07:29:00Z"
lastmod = "2015-09-17T14:22:00Z"
weight = 45854
keywords = [ "tcpwindowsize" ]
aliases = [ "/questions/45854" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Window Size and Network Bandwidth](/questions/45854/tcp-window-size-and-network-bandwidth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45854-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have added 2 more captures (better) as examples. Each capture transfers the same file from the same source (Unix server). The client side is either a Windows 7 laptop or a MacBook Pro.<br />
<a href="https://www.dropbox.com/s/216fehk3p75ws45/MacBookSCPv2.pcapng?dl=0">https://www.dropbox.com/s/216fehk3p75ws45/MacBookSCPv2.pcapng?dl=0</a></p><p><a href="https://www.dropbox.com/s/boxkdcmsmrsyb1l/Windows7winSCPv2.pcapng?dl=0">https://www.dropbox.com/s/boxkdcmsmrsyb1l/Windows7winSCPv2.pcapng?dl=0</a></p><p>The captures illustrate the trouble that I am having; understanding windows size. The . The Win7 window size (65535) does seem to match the amount of data received (Bytes in flight - 2496). The MacBook capture seems more appropriate.</p><p>original post.</p><p>I am learning TCP window size and the impact window size has on data transfer and bandwidth. I have captured traffic between my field office server (over WAN) to a HQ backup server. I have noticed that some offices do not consume all available bandwidth. I captured traffic to investigate. I selected a series of 4 packets to analysis. First packet (of the series) - HQ server to field office server – this packet is acknowledging the previous set of data and (I assume) is setting the stage for the next set of data (using window size). Window size value = 1129 Window size scaling factor is 128 Calculated window size is 144,512</p><p>Next 3 packets – field office server to HQ server (the packet represent the data this being backed up). For these packets, I don’t believe window size is relevant. Instead the bytes in flight are important. Each of the 3 packets has a length of 1380. The bytes in flight increments by 1380 for each packet (1380, 2760 and 4140). Next packet is from HQ server to field office server. This packet acknowledges the previous set. The cycle begins again.</p><p>Should the field server send more data between acknowledgements? Instead of 3 packets, I was thinking more like 13 packets (1380x13=17,940bytes * 8 bits = 143,520 which is pretty close to 144,512). Am I missing something?</p><p>traffic capture file at</p><p><a href="https://www.dropbox.com/s/nw524rpzr2vh7ve/BackupCapture.pcap?dl=0">https://www.dropbox.com/s/nw524rpzr2vh7ve/BackupCapture.pcap?dl=0</a></p></div><div id="question-tags" class="tags-container tags">tcpwindowsize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '15, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/a2d282447b07a1cc698ecb68ac13f252?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RicM&#39;s gravatar image" /><p>RicM<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RicM has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Sep '15, 12:10</p></div></div><div id="comments-container-45854" class="comments-container"><span id="45859"></span><div id="comment-45859" class="comment"><div id="post-45859-score" class="comment-score"></div><div class="comment-text"><p>This kind of discussion is hard without a capture file - can you post it on Cloudshark (and sanitize it with TraceWrangler if required first)?</p></div><div id="comment-45859-info" class="comment-info"><span class="comment-age">(15 Sep '15, 12:50)</span> Jasper ♦♦</div></div><span id="45876"></span><div id="comment-45876" class="comment"><div id="post-45876-score" class="comment-score"></div><div class="comment-text"><p>Added capture information. I did not see how to attach a file.</p></div><div id="comment-45876-info" class="comment-info"><span class="comment-age">(16 Sep '15, 06:07)</span> RicM</div></div><span id="45879"></span><div id="comment-45879" class="comment"><div id="post-45879-score" class="comment-score"></div><div class="comment-text"><p>It's unlikely anyone is going to wade through all that text. There is no way to attach a file on this site, so instead post your capture file some place publicly accessible (www.cloudshark.org recommended, but other places like Dropbox or Google Drive will work as well) and edit your question to include a link to the capture file so we can download it. I recommend including more than just six packets.</p></div><div id="comment-45879-info" class="comment-info"><span class="comment-age">(16 Sep '15, 07:03)</span> Jim Aragon</div></div></div><div id="comment-tools-45854" class="comment-tools"></div><div class="clear"></div><div id="comment-45854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45934"></span>

<div id="answer-container-45934" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45934-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's not two data packets per ACK, it's one ACK for every two data packets. Those are not the same thing. There is no reason to expect or try to force more packets between ACKs, because the sending system isn't waiting on the ACKs. It doesn't send two packets and then wait for an ACK before sending two more. The sending system <em>transmits continuously</em>, and the receiving system <em>responds continuously</em> with acknowledgements as the data packets are received. In this case, Delayed ACK is in use, so the receiving system sends one ACK for every two data packets, instead of one ACK for each data packet.</p><p>Looking at the Windows capture file: It's encrypted, so we don't know what commands/requests and responses are going back and forth. We can see that by packet 205 the two systems seem to have negotiated whatever requests/responses are involved, and then a continuous data transfer gets underway. From that point on, the sender sends a continuous stream of 1,248-byte segments, which is the largest segment it is allowed to send based on the receiver's Maximum Segment Size of 1,260 bytes with Timestamps in the TCP options field.</p><p>From packet 205 to the end, packet 40,669, there is only one place where the delta time between data packets exceeds 1 ms. The delta times between all the rest of the data packets are less than 0.5 milliseconds.</p><p>From packet 205 to the end, that's 40,464 packets (both directions) in 9.788 seconds. It takes more than 19 seconds to get to packet 205, but from that point on, I'd say things are moving along very nicely.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '15, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-45934" class="comments-container"></div><div id="comment-tools-45934" class="comment-tools"></div><div class="clear"></div><div id="comment-45934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45899"></span>

<div id="answer-container-45899" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45899-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The receive windowsize is not the only dominating factor in TCP flow clontrol. There is also the <a href="https://en.wikipedia.org/wiki/Congestion_window">congestion window</a> that plays a role here. The trace was taken at the receiver so what you would normally see in an inbound streaming traffic is an ACK acki-ing 'every other' packet. The RTT is around 7 ms. In your trace the sender starts sending using a 1 MSS window, then increments to 2 MSS and 3 MSS so this looks like we are either pretty early in the connection or we suffered a packet loss or timeout on the connection causing cwnd to drop.</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '15, 22:38</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-45899" class="comments-container"><span id="45931"></span><div id="comment-45931" class="comment"><div id="post-45931-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the information and feedback. Couple of follow ups.</p><p>Is there any way to force more packets between ACK's? Thinking back over the previous months/years of traffic captures, it has been rare that I have seen more than 2 packets per ACK. It is almost like there is a regedit setting on my laptop that limits data exchanges to 2 packets per ACK.</p><p>Is there a formula that calculates bytes/packets per ACK? I found the following formula, but it seems different than what you are describing.</p><p>Bandwidth-in-bits-per-second * Round-trip-latency-in-seconds = TCP window size in bits / 8 = TCP window size in bytes</p></div><div id="comment-45931-info" class="comment-info"><span class="comment-age">(17 Sep '15, 13:09)</span> RicM</div></div></div><div id="comment-tools-45899" class="comment-tools"></div><div class="clear"></div><div id="comment-45899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

