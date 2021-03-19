+++
type = "question"
title = "How to capture all control and mgmt packets?"
description = '''I&#x27;m capturing with tcpdump and also via the wireshark gui. The dropped packets is 0 but I can clearly see that some clear-to-send / request-to-send and link layer ACK packets are missing. any idea why? I tried to increase the buffer to 100MB to see if it would help but no success.'''
date = "2011-09-06T15:19:00Z"
lastmod = "2011-09-07T07:16:00Z"
weight = 6141
keywords = [ "capture", "tcpdump" ]
aliases = [ "/questions/6141" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture all control and mgmt packets?](/questions/6141/how-to-capture-all-control-and-mgmt-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6141-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm capturing with tcpdump and also via the wireshark gui. The dropped packets is 0 but I can clearly see that some clear-to-send / request-to-send and link layer ACK packets are missing. any idea why? I tried to increase the buffer to 100MB to see if it would help but no success.</p></div><div id="question-tags" class="tags-container tags">capture tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '11, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/5d64d21de6598960bf2db61f1ca705cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddayan&#39;s gravatar image" /><p>ddayan<br />
<span class="score" title="41 reputation points">41</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddayan has no accepted answers">0%</span></p></div></div><div id="comments-container-6141" class="comments-container"><span id="6149"></span><div id="comment-6149" class="comment"><div id="post-6149-score" class="comment-score"></div><div class="comment-text"><p>do you see any wireless packets (display filter "wlan") ?</p></div><div id="comment-6149-info" class="comment-info"><span class="comment-age">(06 Sep '11, 23:44)</span> Landi</div></div><span id="6170"></span><div id="comment-6170" class="comment"><div id="post-6170-score" class="comment-score"></div><div class="comment-text"><p>yea I can see most of the packets, but its clear that some are missing. for an example when I see a clear to send request made from my machine but I dont see a request to send packet. or when I can see that some packets dont have ACK packets but they are not retransmitted so I know the packet was acknowledged.</p></div><div id="comment-6170-info" class="comment-info"><span class="comment-age">(07 Sep '11, 03:51)</span> ddayan</div></div><span id="6177"></span><div id="comment-6177" class="comment"><div id="post-6177-score" class="comment-score"></div><div class="comment-text"><p>what is your capture setup then, do you capture your own machines traffic with a sniffer running on the very same machine (same NIC) or do you use another wireless card or even 2nd device to capture the traffic? Also, which tool do you use to capture and which specs (frequency, channel(s), 802.11a/b/g/n?)</p></div><div id="comment-6177-info" class="comment-info"><span class="comment-age">(07 Sep '11, 05:05)</span> Landi</div></div><span id="6179"></span><div id="comment-6179" class="comment"><div id="post-6179-score" class="comment-score"></div><div class="comment-text"><p>I'm capturing using the same NIC, its a Pentium 4 (1.4Ghz) laptop using atheros card and the ath5k driver, OS: backtrack 5 (Linux).</p><p>To capture 1) I make a monitor interface using airmon-ng 2) I start capturing using tcpdump(tcpdump -nvvXSs 1514 -i mon0 -w packet_dump) or wireshark<br />
3) I connect to an AP.</p><p>I didn't find how I can set the capture to a certain frequency/channel</p></div><div id="comment-6179-info" class="comment-info"><span class="comment-age">(07 Sep '11, 05:56)</span> ddayan</div></div></div><div id="comment-tools-6141" class="comment-tools"></div><div class="clear"></div><div id="comment-6141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6183"></span>

<div id="answer-container-6183" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6183-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Two things here:</p><ol><li>If you're going to capture your own traffic you should <em>not</em> use the same NIC, because in most cases you can either send <em>or</em> recieve frames with your wireless adapter which in most cases resolves in you not getting all of your own packets</li><li>You should also limit your channel(s) to the one's you are working on in order to prevent your wireless driver from hopping through some other channels and thereby missing packets. Put your NIC in monitor mode with airmon-ng start &lt;whatever&gt; and give it a channel number - see aircrack-ng docs for details and command flags.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '11, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span> </br></p></div></div><div id="comments-container-6183" class="comments-container"><span id="6208"></span><div id="comment-6208" class="comment"><div id="post-6208-score" class="comment-score"></div><div class="comment-text"><p>From my understanding if you listen from the same card the outgoing packets are delivered from the driver not by listening to the channel (i.e. the driver sends the packet and stores a copy locally). However I captured with another laptop and I can more acknowledgments now. Thanks!</p></div><div id="comment-6208-info" class="comment-info"><span class="comment-age">(08 Sep '11, 05:42)</span> ddayan</div></div><span id="6209"></span><div id="comment-6209" class="comment"><div id="post-6209-score" class="comment-score"></div><div class="comment-text"><p>True, I myself don't exactly know where the driver captures the packets on wireless NICs, but from what I've experienced while capturing wireless frames it was never a good idea to rely on the same machine sending and monitoring stuff - anyways, good that it seems to work know. Good luck</p></div><div id="comment-6209-info" class="comment-info"><span class="comment-age">(08 Sep '11, 06:49)</span> Landi</div></div></div><div id="comment-tools-6183" class="comment-tools"></div><div class="clear"></div><div id="comment-6183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

