+++
type = "question"
title = "Unknown SCTP Payload Protocol Id (SABP)"
description = '''Hi! I am using wire shark version 1.4.6 and when i send encoded SABP (Service Area Broadcast Protocol) packet (WRITE REPLACE message) over SCTP (Stream Control Transmission Protocol) the SCTP Payload protocol identifier is Unknown (31). However i found two links where SABP is defined as PPI=31 and i...'''
date = "2011-11-22T01:32:00Z"
lastmod = "2011-11-22T06:40:00Z"
weight = 7552
keywords = [ "3gpp", "sabp", "sctp" ]
aliases = [ "/questions/7552" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Unknown SCTP Payload Protocol Id (SABP)](/questions/7552/unknown-sctp-payload-protocol-id-sabp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7552-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I am using wire shark version 1.4.6 and when i send encoded SABP (Service Area Broadcast Protocol) packet (WRITE REPLACE message) over SCTP (Stream Control Transmission Protocol) the SCTP Payload protocol identifier is <strong>Unknown (31)</strong>.</p><p>However i found two links where SABP is defined as PPI=31 and it's used over SCTP.</p><ol><li><a href="http://wiki.wireshark.org/SABP/">http://wiki.wireshark.org/SABP</a></li><li><a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-sctp.c/">http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-sctp.c</a></li></ol><p>Could some one please help me on this or have a SCTP trace whith SABP message?</p><p>Thanks.</p><pre><code>Stream Control Transmission Protocol, Src Port: 3452 (3452), Dst Port: 3452 (3452)
Source port: 3452
Destination port: 3452
Verification tag: 0x1500d017
Checksum: 0x745fed2a (not verified)
DATA chunk(unordered, complete segment, TSN: 476389665, SID: 0, SSN: 0, PPID: 31, payload length: 49 bytes)
    Chunk type: DATA (0)
        0... .... = Bit: Stop processing of the packet
        .0.. .... = Bit: Do not report
    Chunk flags: 0x07
        .... ...1 = E-Bit: Last segment
        .... ..1. = B-Bit: First segment
        .... .1.. = U-Bit: Unordered delivery
        .... 0... = I-Bit: Possibly delay SACK
    Chunk length: 65
    TSN: 476389665
    Stream Identifier: 0x0000
    Stream sequence number: 0
    Payload protocol identifier: Unknown (31)
    Chunk padding: 000000
Data (49 bytes)
0000  00 00 00 2d 00 00 06 00 07 40 02 53 75 00 0f 40   [email protected]@
0010  09 00 00 03 e6 79 d1 3f f7 64 00 0d 40 02 0a 63   [email protected]
0020  00 09 40 02 18 d8 00 04 40 01 39 00 00 40 02 11   [email protected]@[email protected]
0030  c4                                                .
Data: 0000002d000006000740025375000f4009000003e679d13f...
[Length: 49]</code></pre></div><div id="question-tags" class="tags-container tags">3gpp sabp sctp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '11, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/b45f93fdfa837f36334066e28cd7334c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sifu&#39;s gravatar image" /><p>sifu<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sifu has no accepted answers">0%</span></p></div></div><div id="comments-container-7552" class="comments-container"></div><div id="comment-tools-7552" class="comment-tools"></div><div class="clear"></div><div id="comment-7552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7555"></span>

<div id="answer-container-7555" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7555-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Upgrade to a newer version (e.g., 1.6.x).</p><p>To see what is used for the 1.4.x series, you have to look at the <a href="http://anonsvn.wireshark.org/wireshark/trunk-1.4/epan/dissectors/packet-sctp.c">source code</a> for that (pretty old now) version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '11, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-7555" class="comments-container"><span id="7560"></span><div id="comment-7560" class="comment"><div id="post-7560-score" class="comment-score"></div><div class="comment-text"><p>Actually you need a development version a SABP dissector was recently added.</p></div><div id="comment-7560-info" class="comment-info"><span class="comment-age">(22 Nov '11, 09:39)</span> Anders ♦</div></div><span id="7562"></span><div id="comment-7562" class="comment"><div id="post-7562-score" class="comment-score"></div><div class="comment-text"><p>My bad :-) I was thinking of sbc-ap</p></div><div id="comment-7562-info" class="comment-info"><span class="comment-age">(22 Nov '11, 09:48)</span> Anders ♦</div></div><span id="7578"></span><div id="comment-7578" class="comment"><div id="post-7578-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I have just installed wireshark 1.6.4 on ubuntu 11.04 and it solves my problem. Actually Ubuntu Software Center and Synaptic only propose 1.4.6.</p></div><div id="comment-7578-info" class="comment-info"><span class="comment-age">(23 Nov '11, 01:05)</span> sifu</div></div></div><div id="comment-tools-7555" class="comment-tools"></div><div class="clear"></div><div id="comment-7555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

