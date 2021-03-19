+++
type = "question"
title = "Google Object Storage RST, ACK"
description = '''We are trying to use Google Object storage and have a firewall that blocks hosts that sends &quot;Unhandled External Packets&quot;. So below it seems that our client software tears down the connection on No. 24 so our firewall closes the connection completely and then Google responds with a RST on No. 25. Sin...'''
date = "2014-11-23T20:56:00Z"
lastmod = "2014-11-24T09:28:00Z"
weight = 38089
keywords = [ "rst", "ack" ]
aliases = [ "/questions/38089" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Google Object Storage RST, ACK](/questions/38089/google-object-storage-rst-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38089-score" class="post-score" title="current number of votes">0</div><span id="post-38089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are trying to use Google Object storage and have a firewall that blocks hosts that sends "Unhandled External Packets". So below it seems that our client software tears down the connection on No. 24 so our firewall closes the connection completely and then Google responds with a RST on No. 25. Since the connection is already closed our firewall bans this IP. So I guess my question is... Is Google to blame?</p><pre><code>No.     Time        Source                Destination           Protocol Length Info
  1 0.000000    123.123.123.123         74.125.25.84          TCP      74     47379→443 [SYN] Seq=0 Win=14600 Len=0 MSS=1400 SACK_PERM=1 TSval=159142561 TSecr=0 WS=128
  2 0.038908    74.125.25.84          123.123.123.123         TCP      74     443→47379 [SYN, ACK] Seq=0 Ack=1 Win=42540 Len=0 MSS=1400 SACK_PERM=1 TSval=983168135 TSecr=159142561 WS=128
  3 0.041143    123.123.123.123         74.125.25.84          TCP      66     47379→443 [ACK] Seq=1 Ack=1 Win=14720 Len=0 TSval=159142603 TSecr=983168135
  4 0.056158    123.123.123.123         74.125.25.84          TLSv1    286    Client Hello
  5 0.095017    74.125.25.84          123.123.123.123         TCP      66     443→47379 [ACK] Seq=1 Ack=221 Win=43648 Len=0 TSval=983168191 TSecr=159142618
  6 0.096134    74.125.25.84          123.123.123.123         TLSv1    1454   Server Hello
  7 0.096187    74.125.25.84          123.123.123.123         TCP      1454   [TCP segment of a reassembled PDU]
  8 0.096213    74.125.25.84          123.123.123.123         TLSv1    819    Certificate
  9 0.098232    123.123.123.123         74.125.25.84          TCP      66     47379→443 [ACK] Seq=221 Ack=1389 Win=17408 Len=0 TSval=159142660 TSecr=983168192
 10 0.098478    123.123.123.123         74.125.25.84          TCP      66     47379→443 [ACK] Seq=221 Ack=2777 Win=20224 Len=0 TSval=159142660 TSecr=983168192
 11 0.098687    123.123.123.123         74.125.25.84          TCP      66     47379→443 [ACK] Seq=221 Ack=3530 Win=23040 Len=0 TSval=159142660 TSecr=983168192
 12 0.103253    123.123.123.123         74.125.25.84          TLSv1    200    Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message
 13 0.142249    74.125.25.84          123.123.123.123         TLSv1    125    Change Cipher Spec, Encrypted Handshake Message
 14 0.144370    123.123.123.123         74.125.25.84          TLSv1    316    Application Data, Application Data
 15 0.223258    74.125.25.84          123.123.123.123         TCP      66     443→47379 [ACK] Seq=3589 Ack=605 Win=45824 Len=0 TSval=983168319 TSecr=159142706
 16 0.225626    123.123.123.123         74.125.25.84          TLSv1    1164   Application Data, Application Data
 17 0.264448    74.125.25.84          123.123.123.123         TCP      66     443→47379 [ACK] Seq=3589 Ack=1703 Win=48000 Len=0 TSval=983168360 TSecr=159142787
 18 0.277894    74.125.25.84          123.123.123.123         TLSv1    743    Application Data
 19 0.278987    74.125.25.84          123.123.123.123         TLSv1    103    Application Data
 20 0.279175    74.125.25.84          123.123.123.123         TLSv1    295    Application Data
 21 0.279227    74.125.25.84          123.123.123.123         TCP      66     443→47379 [FIN, ACK] Seq=4532 Ack=1703 Win=48000 Len=0 TSval=983168375 TSecr=159142787
 22 0.281132    123.123.123.123         74.125.25.84          TCP      66     47379→443 [ACK] Seq=1703 Ack=4303 Win=25728 Len=0 TSval=159142842 TSecr=983168374
 23 0.281138    123.123.123.123         74.125.25.84          TLSv1    103    Encrypted Alert
 24 0.282572    123.123.123.123         74.125.25.84          TCP      66     47379→443 [RST, ACK] Seq=1740 Ack=4533 Win=28544 Len=0 TSval=159142844 TSecr=983168375
 25 0.320000    74.125.25.84          123.123.123.123         TCP      54     443→47379 [RST] Seq=4303 Win=0 Len=0</code></pre><p>Details of No 21-25</p><pre><code>    No.     Time        Source                Destination           Protocol Length Info
     21 0.279227    74.125.25.84          12.12.123.123         TCP      66     443?47379 [FIN, ACK] Seq=4532 Ack=1703 Win=48000 Len=0 TSval=983168375 TSecr=159142787

Frame 21: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: IETF-VRRP-VRID_02 (00:00:5e:00:01:02), Dst: Watchgua_11:f1:41 (01:91:71:11:f1:41)
Internet Protocol Version 4, Src: 74.125.25.84 (74.125.25.84), Dst: 12.12.123.123 (12.12.123.123)
Transmission Control Protocol, Src Port: 443 (443), Dst Port: 47379 (47379), Seq: 4532, Ack: 1703, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     22 0.281132    12.12.123.123         74.125.25.84          TCP      66     47379?443 [ACK] Seq=1703 Ack=4303 Win=25728 Len=0 TSval=159142842 TSecr=983168374

Frame 22: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Watchgua_11:f1:41 (01:91:71:11:f1:41), Dst: IETF-VRRP-VRID_02 (00:00:5e:00:01:02)
Internet Protocol Version 4, Src: 12.12.123.123 (12.12.123.123), Dst: 74.125.25.84 (74.125.25.84)
Transmission Control Protocol, Src Port: 47379 (47379), Dst Port: 443 (443), Seq: 1703, Ack: 4303, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     23 0.281138    12.12.123.123         74.125.25.84          TLSv1    103    Encrypted Alert

Frame 23: 103 bytes on wire (824 bits), 103 bytes captured (824 bits)
Ethernet II, Src: Watchgua_11:f1:41 (01:91:71:11:f1:41), Dst: IETF-VRRP-VRID_02 (00:00:5e:00:01:02)
Internet Protocol Version 4, Src: 12.12.123.123 (12.12.123.123), Dst: 74.125.25.84 (74.125.25.84)
Transmission Control Protocol, Src Port: 47379 (47379), Dst Port: 443 (443), Seq: 1703, Ack: 4303, Len: 37
Secure Sockets Layer

No.     Time        Source                Destination           Protocol Length Info
     24 0.282572    12.12.123.123         74.125.25.84          TCP      66     47379?443 [RST, ACK] Seq=1740 Ack=4533 Win=28544 Len=0 TSval=159142844 TSecr=983168375

Frame 24: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Watchgua_11:f1:41 (01:91:71:11:f1:41), Dst: IETF-VRRP-VRID_02 (00:00:5e:00:01:02)
Internet Protocol Version 4, Src: 12.12.123.123 (12.12.123.123), Dst: 74.125.25.84 (74.125.25.84)
Transmission Control Protocol, Src Port: 47379 (47379), Dst Port: 443 (443), Seq: 1740, Ack: 4533, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     25 0.320000    74.125.25.84          12.12.123.123         TCP      54     443?47379 [RST] Seq=4303 Win=0 Len=0

Frame 25: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: IETF-VRRP-VRID_02 (00:00:5e:00:01:02), Dst: Watchgua_11:f1:41 (01:91:71:11:f1:41)
Internet Protocol Version 4, Src: 74.125.25.84 (74.125.25.84), Dst: 12.12.123.123 (12.12.123.123)
Transmission Control Protocol, Src Port: 443 (443), Dst Port: 47379 (47379), Seq: 4303, Len: 0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '14, 20:56</strong></p><img src="https://secure.gravatar.com/avatar/bc1ebf9df0d9b3a0e12ea6407203156a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ooga%20booga&#39;s gravatar image" /><p><span>ooga booga</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ooga booga has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Nov '14, 00:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-38089" class="comments-container"></div><div id="comment-tools-38089" class="comment-tools"></div><div class="clear"></div><div id="comment-38089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38109"></span>

<div id="answer-container-38109" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38109-score" class="post-score" title="current number of votes">0</div><span id="post-38109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The time between the last two packets is 4ms (they are 12ms away according to ping). So I am guessing since Google didn't receive a FIN to do an orderly connection close it sent an RST to abort the connection, however the client program had already done an abortive connection release and my firewall saw this first, took down the connection and then 4ms later Google's RST arrived..</p><p>So what you need to happen is my client software needs to be modified to close properly using FIN rather than RST?</p><p>So this is all a big guess.. thoughts?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '14, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/bc1ebf9df0d9b3a0e12ea6407203156a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ooga%20booga&#39;s gravatar image" /><p><span>ooga booga</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ooga booga has no accepted answers">0%</span></p></div></div><div id="comments-container-38109" class="comments-container"></div><div id="comment-tools-38109" class="comment-tools"></div><div class="clear"></div><div id="comment-38109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

