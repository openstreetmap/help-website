+++
type = "question"
title = "3GPP PCAP over SUA (SS7 SCCP-User Adaptation Layer)"
description = '''Hi! I am using wire shark version 1.4.6 and i am trying to send encoded PCAP (Positioning Calculation Application Part) packet (POSITION INITIATION REQUEST message) over SUA (SS7 SCCP-User Adaptation Layer) between a Radio Network Controller (RNC) and the Stand-Alone SMLC (SAS) accordance with 3GPP ...'''
date = "2011-11-18T07:58:00Z"
lastmod = "2011-11-20T23:09:00Z"
weight = 7504
keywords = [ "3gpp", "sccp", "pcap", "sua" ]
aliases = [ "/questions/7504" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [3GPP PCAP over SUA (SS7 SCCP-User Adaptation Layer)](/questions/7504/3gpp-pcap-over-sua-ss7-sccp-user-adaptation-layer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7504-score" class="post-score" title="current number of votes">0</div><span id="post-7504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I am using wire shark version 1.4.6 and i am trying to send encoded PCAP (Positioning Calculation Application Part) packet (POSITION INITIATION REQUEST message) over SUA (SS7 SCCP-User Adaptation Layer) between a Radio Network Controller (RNC) and the Stand-Alone SMLC (SAS) accordance with 3GPP standart. But when i send it wireshark is unable to recognize the PCAP protocol and it displays: Protocol is SUA (RFC 3868) and info is CORE. However PCAP packet is correctly decoded.</p><p>Could some one please help me on this or have a SUA trace whith PCAP message?</p><p>Thanks.</p><pre><code>No.     Time        Source                Destination           Protocol Info
    323 46.555464   10.1.1.204            10.1.1.191            SUA (RFC 3868) CORE

Stream Control Transmission Protocol, Src Port: 40000 (40000), Dst Port: 20000 (20000)
    Source port: 40000
    Destination port: 20000
    Verification tag: 0x3f59bad4
    Checksum: 0x1f9809b6 (not verified)
    DATA chunk(unordered, complete segment, TSN: 1527587857, SID: 0, SSN: 0, PPID: 4, payload length: 168 bytes)
        Chunk type: DATA (0)
            0... .... = Bit: Stop processing of the packet
            .0.. .... = Bit: Do not report
        Chunk flags: 0x07
            .... ...1 = E-Bit: Last segment
            .... ..1. = B-Bit: First segment
            .... .1.. = U-Bit: Unordered delivery
            .... 0... = I-Bit: Possibly delay SACK
        Chunk length: 184
        TSN: 1527587857
        Stream Identifier: 0x0000
        Stream sequence number: 0
        Payload protocol identifier: SUA (4)
SS7 SCCP-User Adaptation Layer
    Version: Release 1 (1)
    Reserved: 00
    Message Class: Connection-Oriented messages (8)
    Message Type: Connection Request (CORE) (1)
    Message Length: 168
    Routing context (1 context)
        Parameter Tag: Routing context (0x0006)
        Parameter Length: 8
        Routing context: 1
    Protocol class (2)
        Parameter Tag: Protocol class (0x0115)
        Parameter Length: 8
        Reserved: 000000
        Protocol Class
            0... .... = Return On Error Bit: No Special Options
            .000 0010 = Protocol Class: 2
    Source reference number (1)
        Parameter Tag: Source reference number (0x0104)
        Parameter Length: 8
        Source Reference Number: 1
    Destination address
        Parameter Tag: Destination address (0x0103)
        Parameter Length: 24
        Routing Indicator: Route on SSN + IP Address (4)
        Address Indicator
            0000 0000 0000 0... = Reserved Bits: 0
            .... .... .... .0.. = Include GT: False
            .... .... .... ..0. = Include PC: False
            .... .... .... ...1 = Include SSN: True
        Subsystem number (249)
            Parameter Tag: Subsystem number (0x8003)
            Parameter Length: 8
            Reserved: 000000
            Subsystem Number: 249
        IPv4 address (10.1.1.191)
            Parameter Tag: IPv4 address (0x8004)
            Parameter Length: 8
            IP Version 4 address: 10.1.1.191 (10.1.1.191)
    Sequence control (1)
        Parameter Tag: Sequence control (0x0116)
        Parameter Length: 8
        Sequence Control: 1
    Source address
        Parameter Tag: Source address (0x0102)
        Parameter Length: 24
        Routing Indicator: Route on SSN + IP Address (4)
        Address Indicator
            0000 0000 0000 0... = Reserved Bits: 0
            .... .... .... .0.. = Include GT: False
            .... .... .... ..0. = Include PC: False
            .... .... .... ...1 = Include SSN: True
        Subsystem number (250)
            Parameter Tag: Subsystem number (0x8003)
            Parameter Length: 8
            Reserved: 000000
            Subsystem Number: 250
        IPv4 address (10.1.1.204)
            Parameter Tag: IPv4 address (0x8004)
            Parameter Length: 8
            IP Version 4 address: 10.1.1.204 (10.1.1.204)
    SS7 hop counter (15)
        Parameter Tag: SS7 hop counter (0x0101)
        Parameter Length: 8
        Reserved: 000000
        SS7 Hop Counter: 15
    Importance (5)
        Parameter Tag: Importance (0x0113)
        Parameter Length: 8
        Reserved: 000000
        Importance: 5
    Data (SS7 message of 58 bytes)
        Parameter Tag: Data (0x010b)
        Parameter Length: 62
        Data: 0001404035000003001c000260b6001d0002518000420022...
        Padding: 0000
Data (58 bytes)
    Data: 0001404035000003001c000260b6001d0002518000420022...
    [Length: 58]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-3gpp" rel="tag" title="see questions tagged &#39;3gpp&#39;">3gpp</span> <span class="post-tag tag-link-sccp" rel="tag" title="see questions tagged &#39;sccp&#39;">sccp</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-sua" rel="tag" title="see questions tagged &#39;sua&#39;">sua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '11, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/b45f93fdfa837f36334066e28cd7334c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sifu&#39;s gravatar image" /><p><span>sifu</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sifu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Nov '11, 10:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7504" class="comments-container"></div><div id="comment-tools-7504" class="comment-tools"></div><div class="clear"></div><div id="comment-7504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7509"></span>

<div id="answer-container-7509" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7509-score" class="post-score" title="current number of votes">0</div><span id="post-7509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sifu has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try setting the PCAP preference (Edit-&gt;Preferences-&gt;Protocols-&gt;PCAP) for the SSNs to 249 and/or 250.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '11, 11:39</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-7509" class="comments-container"><span id="7524"></span><div id="comment-7524" class="comment"><div id="post-7524-score" class="comment-score"></div><div class="comment-text"><p>Thank you i had not set the pcap preferences, now i see the correct pcap packet</p></div><div id="comment-7524-info" class="comment-info"><span class="comment-age">(20 Nov '11, 23:09)</span> <span class="comment-user userinfo">sifu</span></div></div></div><div id="comment-tools-7509" class="comment-tools"></div><div class="clear"></div><div id="comment-7509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

