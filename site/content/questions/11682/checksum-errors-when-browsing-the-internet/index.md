+++
type = "question"
title = "checksum errors when browsing the internet"
description = '''Any ideas on what is causing all these header checksum errors...  A few times a day users intermittently lose network connections to the exchange server or the internet. Upon opening IE I start to see checksum errors like the following and they stop when closing IE... Header checksum: 0x0000 [incorr...'''
date = "2012-06-05T13:08:00Z"
lastmod = "2012-06-05T13:27:00Z"
weight = 11682
keywords = [ "checksum", "error" ]
aliases = [ "/questions/11682" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [checksum errors when browsing the internet](/questions/11682/checksum-errors-when-browsing-the-internet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11682-score" class="post-score" title="current number of votes">0</div><span id="post-11682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Any ideas on what is causing all these header checksum errors... A few times a day users intermittently lose network connections to the exchange server or the internet. Upon opening IE I start to see checksum errors like the following and they stop when closing IE...</p><p>Header checksum: 0x0000 [incorrect, should be 0x54ad (maybe caused by "IP checksum offload"?)]</p><p>This is a sample of the packet traffic that get the checksum error:</p><pre><code>20  4.223408    192.168.0.102   192.168.0.6 DNS 76  Standard query A search.yahoo.com
87  17.876965   192.168.0.102   192.168.0.6 DNS 73  Standard query A www.yahoo.com
91  17.892743   192.168.0.102   209.191.122.70  TCP 66  50355 &gt; http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1
93  17.893526   192.168.0.102   209.191.122.70  TCP 54  50355 &gt; http [ACK] Seq=1 Ack=1 Win=65700 Len=0
126 20.883091   192.168.0.102   209.191.122.70  TCP 54  50356 &gt; http [ACK] Seq=1 Ack=1 Win=65700 Len=0
127 20.883608   192.168.0.102   209.191.122.70  HTTP    297 GET / HTTP/1.1 
2811    41.858393   192.168.0.102   184.51.200.194  TCP 54  50455 &gt; http [RST, ACK] Seq=407 Ack=1 Win=0 Len=0
2812    41.858718   192.168.0.102   184.51.200.40   TCP 54  50452 &gt; http [RST, ACK] Seq=427 Ack=1 Win=0 Len=0
3426    49.442890   192.168.0.102   216.115.96.174  TCP 54  50422 &gt; http [RST, ACK] Seq=1 Ack=1 Win=0 Len=0
3427    49.550803   192.168.0.102   216.115.110.118 TCP 54  50388 &gt; http [RST, ACK] Seq=1 Ack=1 Win=0 Len=0</code></pre><p>Thanks, Dave</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '12, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/879889df151257c706b39db87402aa85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave&#39;s gravatar image" /><p><span>Dave</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jun '12, 13:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-11682" class="comments-container"></div><div id="comment-tools-11682" class="comment-tools"></div><div class="clear"></div><div id="comment-11682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11684"></span>

<div id="answer-container-11684" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11684-score" class="post-score" title="current number of votes">1</div><span id="post-11684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As the error message suggests, IP checksum offload is enabled. This means that the computer’s TCP/IP stack does not calculate the checksum. Instead, it passes the packet to the NIC and the NIC driver calculates the checksum and adds it to the packet before the packet is transmitted on the wire. Wireshark sees the packet before the checksum has been added. When the packet is transmitted on the wire, the checksum is correct.</p><p>One clue that checksum offload is involved is that the packets with the errors don’t get retransmitted. If the checksum really was wrong, either the packets would be retransmitted, or the communication would fail.</p><p>This can be considered a cosmetic error. You can ignore it, or you can make it go away by turning off checksum offloading in the NIC properties, or disabling IP checksum validation in Wireshark’s properties.</p><p>To see the actual transmitted packet with the correct checksum, capture the traffic from a third PC that is not involved in the communication using a hub or a port mirroring switch, instead of capturing on one of the end points.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '12, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jun '12, 16:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-11684" class="comments-container"></div><div id="comment-tools-11684" class="comment-tools"></div><div class="clear"></div><div id="comment-11684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11685"></span>

<div id="answer-container-11685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11685-score" class="post-score" title="current number of votes">1</div><span id="post-11685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The clue is in the error message: [maybe caused by "IP checksum offload"?)].</p><p>Your NIC (or NIC driver) is calculating IP checksums so the stack doesn't bother, and at the point that the capture mechanism gets hold of the packet the checksum is garbage.</p><p>You should see that the errors are only reported for outgoing packets from your machine, incoming packets will have the correct checksum.</p><p>You can remove the errors by checking the "Support packet-capture from IP TSO-enabled hardware" option in the IP dissectors preferences.</p><p>If there were actual errors in the checksums it's extremely unlikely that you would see the packets when capturing on a regular NIC as the packets would be discarded.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '12, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-11685" class="comments-container"></div><div id="comment-tools-11685" class="comment-tools"></div><div class="clear"></div><div id="comment-11685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

