+++
type = "question"
title = "MTU size on Windows machine caused retransmissions and eventual hang."
description = ''' FIREWALL   (Shorewall, &amp;lt;----------&amp;gt;192.168.0.21 [Linux]  DSL Modem---&amp;gt;eth0&amp;lt;===&amp;gt; dnsmasq) &amp;lt;==&amp;gt;eth1&amp;lt;===&amp;gt; 16-PORT &amp;lt;----------&amp;gt;192.168.0.22 [Win7]  192.168.0.1 HUB &amp;lt;----------&amp;gt;192.168.0.xx [Linux]  [Debian] &amp;lt;==&amp;gt;wlan0 -----------------------&amp;gt; misc.    From...'''
date = "2014-02-09T12:05:00Z"
lastmod = "2014-02-10T22:14:00Z"
weight = 29582
keywords = [ "url", "win7", "hangs", "browser" ]
aliases = [ "/questions/29582" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [MTU size on Windows machine caused retransmissions and eventual hang.](/questions/29582/mtu-size-on-windows-machine-caused-retransmissions-and-eventual-hang)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29582-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>                          FIREWALL 
                        (Shorewall,                      &lt;----------&gt;192.168.0.21 [Linux]
  DSL Modem---&gt;eth0&lt;===&gt; dnsmasq)  &lt;==&gt;eth1&lt;===&gt; 16-PORT &lt;----------&gt;192.168.0.22 [Win7]
                       192.168.0.1                HUB    &lt;----------&gt;192.168.0.xx [Linux]
                         [Debian]  &lt;==&gt;wlan0 -----------------------&gt; misc.</code></pre><code></code><p><code></code> From the configuration above, and the Wireshark output below, please tell me what's going on with the Win7 box at 192..22.</p><p>The Linux boxes work fine with SSH, SCP and the web. Oddly, no problem on the Win7 box with GMAIL. Other websites are slow (if they even load) on Win7 ONLY. If you enter a URL manually for Firefox on Win7, it will load a page fine.<br />
</p><pre><code>1   0   &#39;==internet==&#39;  192.168.0.22            TCP62   62  https &gt; 52701 [SYN, ACK] Seq=0 Ack=1 Win=8190 Len=0 MSS=1460 WS=64
2   0.000373    192.168.0.22    &#39;=internet=&#39;    TCP60   60  52701 &gt; https [ACK] Seq=1 Ack=1 Win=16425 Len=0
3   0.000997    192.168.0.22    &#39;=internet=&#39;    TLSv1   266 Client Hello
4   0.069747    &#39;==internet==&#39;  192.168.0.22    TCP54       [TCP Window Update] https &gt; 52701 [ACK] Seq=1 Ack=1 Win=8128 Len=0
5   0.072857    &#39;==internet==&#39;  192.168.0.22    TCP54       http https &gt; 52701 [ACK] Seq=1 Ack=213 Win=6912 Len=0
6   0.074068    &#39;==internet==&#39;  192.168.0.22    TLSv1   187 Server Hello, Change Cipher Spec, Encrypted Handshake Message
7   0.075121    192.168.0.22    &#39;=internet=&#39;    TLSv1   101 Change Cipher Spec, Encrypted Handshake Message
8   0.075999    192.168.0.22    &#39;=internet=&#39;    TLSv1   1441  Application Data
9   0.15997 &#39;==internet==&#39;  192.168.0.22        TCP54       http https &gt; 52701 [ACK] Seq=134 Ack=1647 Win=9728 Len=0
10  0.250439    &#39;==internet==&#39;   192.168.0.22   TLSv1   363 [TCP Previous segment not captured] Ignored Unknown Record
11  0.251382    192.168.0.22    &#39;=internet=&#39;    TCP60       [TCP Dup ACK 8#1] 52701 &gt; https [ACK] Seq=1647 Ack=134 Win=16391 Len=0
12  0.274499    &#39;==internet==&#39;   192.168.0.22   TLSv1   1103    [TCP Previous segment not captured] Ignored Unknown Record
13  0.275628    192.168.0.22    &#39;=internet=&#39;    TCP60       [TCP Dup ACK 8#2] 52701 &gt; https [ACK] Seq=1647 Ack=134 Win=16391 Len=0
 . . .
29  0.390888    192.168.0.22    &#39;=internet=&#39;    TCP60       [TCP Dup ACK 8#10] 52701 &gt; https [ACK] Seq=1647 Ack=134 Win=16391 Len=0
30  0.399005    &#39;==internet==&#39;   192.168.0.22   TLSv1   1103    [TCP Retransmission] Ignored Unknown Record</code></pre></div><div id="question-tags" class="tags-container tags">url win7 hangs browser</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '14, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/d77229ae8593144da6d67d910697141b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kirby&#39;s gravatar image" /><p>kirby<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kirby has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Feb '14, 14:12</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29582" class="comments-container"><span id="29585"></span><div id="comment-29585" class="comment"><div id="post-29585-score" class="comment-score"></div><div class="comment-text"><p>Your question title mentiones http but the trace shows https. Based on the timing values (0.4 seconds) I don't see a general problem. So, what exactly is your problem/question?</p></div><div id="comment-29585-info" class="comment-info"><span class="comment-age">(09 Feb '14, 12:33)</span> Kurt Knochner ♦</div></div><span id="29719"></span><div id="comment-29719" class="comment"><div id="post-29719-score" class="comment-score"></div><div class="comment-text"><p>@kirby</p><p>No need to modify the question title to add [Solved], accepting the answer informs other users that the question has been answered.</p></div><div id="comment-29719-info" class="comment-info"><span class="comment-age">(11 Feb '14, 14:13)</span> grahamb ♦</div></div></div><div id="comment-tools-29582" class="comment-tools"></div><div class="clear"></div><div id="comment-29582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29659"></span>

<div id="answer-container-29659" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29659-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that the client never ACKs higher than 134. Note that the largest tcp,len of inbound packets is 1443.<br />
</p><p>Looking at the - missing - packets in <a href="https://www.dropbox.com/s/xfiis5rb5n7eoho/shark-kd.pcapng.gz">shark-kd.pcapng</a> it's clear that none of the full sized 1460 MSS segments make it to the client and the server never reduces the MTU size (which it normally would if PMTUD would work). So the server is retransmitting the 1460 segments to no avail. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_162.png" alt="alt text" /></p><p>This is an example where PMTU discovery is not working correctly and the MSS is not adjusted to the real end to end available MTU size.</p><p>My suggestion would be to reduce the MTU size on your Win7 interface to 1484 to avoid this problem</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 22:14</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 11 Feb '14, 10:49</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-29659" class="comments-container"><span id="29710"></span><div id="comment-29710" class="comment"><div id="post-29710-score" class="comment-score"></div><div class="comment-text"><p>Thanks mrEEde! Win7's MTU was the problem.</p></div><div id="comment-29710-info" class="comment-info"><span class="comment-age">(11 Feb '14, 10:34)</span> kirby</div></div><span id="29711"></span><div id="comment-29711" class="comment"><div id="post-29711-score" class="comment-score"></div><div class="comment-text"><p>It the question is answered, please "accept" the answer so it can be closed, thanks!</p></div><div id="comment-29711-info" class="comment-info"><span class="comment-age">(11 Feb '14, 10:44)</span> mrEEde</div></div><span id="29712"></span><div id="comment-29712" class="comment"><div id="post-29712-score" class="comment-score"></div><div class="comment-text"><p>I don't see an "accept" button.</p><p>BTW MS has a page on PMTU: <span></span></p></div><div id="comment-29712-info" class="comment-info"><span class="comment-age">(11 Feb '14, 11:02)</span> kirby</div></div></div><div id="comment-tools-29659" class="comment-tools"></div><div class="clear"></div><div id="comment-29659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

