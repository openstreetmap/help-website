+++
type = "question"
title = "wireshark unable to decode sua/gsm_map traffic"
description = '''Hi, I am using wire shark version 1.6 and i am sending SUA traffic. It decodes up to SCCP layer and unable to decode tcap/map layer(it is displaying as raw data). Please see the below output  Stream Control Transmission Protocol, Src Port: 14002 (14002), Dst Port: sua (14001)  Source port: 14002  De...'''
date = "2011-07-08T07:28:00Z"
lastmod = "2011-07-10T09:01:00Z"
weight = 4953
keywords = [ "sua" ]
aliases = [ "/questions/4953" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark unable to decode sua/gsm\_map traffic](/questions/4953/wireshark-unable-to-decode-suagsm_map-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4953-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using wire shark version 1.6 and i am sending SUA traffic. It decodes up to SCCP layer and unable to decode tcap/map layer(it is displaying as raw data). Please see the below output</p><pre><code>Stream Control Transmission Protocol, Src Port: 14002 (14002), Dst Port: sua (14001)
    Source port: 14002
    Destination port: 14001
    Verification tag: 0x000048c4
    Checksum: 0x2a1e43db (not verified)
    DATA chunk(unordered, complete segment, TSN: 341282439, SID: 11, SSN: 0, PPID: 4, payload length: 196 bytes)
        Chunk type: DATA (0)
            0... .... = Bit: Stop processing of the packet
            .0.. .... = Bit: Do not report
        Chunk flags: 0x07
            .... ...1 = E-Bit: Last segment
            .... ..1. = B-Bit: First segment
            .... .1.. = U-Bit: Unordered delivery
        .... 0... = I-Bit: Possibly delay SACK
        Chunk length: 212
        TSN: 341282439
        Stream Identifier: 0x000b
        Stream sequence number: 0
        Payload protocol identifier: SUA (4)
SS7 SCCP-User Adaptation Layer
    Version: Release 1 (1)
    Reserved: 00
    Message Class: Connectionless messages (7)
    Message Type: Connectionless Data Transfer (CLDT) (1)
    Message Length: 196
    Data (SS7 message of 72 bytes)
        Parameter Tag: Data (0x010b)
        Parameter Length: 76
        Data: 62464804000000016b1e281c060700118605010101a01160...
    Routing context (1 context)
        Parameter Tag: Routing context (0x0006)
        Parameter Length: 8
        Routing context: 1
    Protocol class (0)
        Parameter Tag: Protocol class (0x0115)
        Parameter Length: 8
        Reserved: 000000
        Protocol Class
            0... .... = Return On Error Bit: No Special Options
            .000 0000 = Protocol Class: 0
    Source address
        Parameter Tag: Source address (0x0102)
        Parameter Length: 44
        Routing Indicator: Route on Global Title (1)
        Address Indicator
            0000 0000 0000 0... = Reserved Bits: 0
            .... .... .... .1.. = Include GT: True
            .... .... .... ..1. = Include PC: True
            .... .... .... ...1 = Include SSN: True
        **Subsystem number (150)**
            Parameter Tag: Subsystem number (0x8003)
            Parameter Length: 8
            Reserved: 000000
            Subsystem Number: 150
        Point code (7164)
            Parameter Tag: Point code (0x8002)
            Parameter Length: 8
            Point Code: 7164
        Global title
            Parameter Tag: Global title (0x8001)
            Parameter Length: 18
            Reserved: 000000
            GTI: 0x04
            Number of Digits: 12
            Translation Type: 0x00
            Numbering Plan: ISDN/Telephony Numbering Plan (Rec. E.161 and E.164) (0x01)
            Nature of Address: International Number (0x04)
            Address information (digits): 553496629991
            Padding: 0000
    Destination address
        Parameter Tag: Destination address (0x0103)
        Parameter Length: 44
        Routing Indicator: Route on Global Title (1)
        Address Indicator
            0000 0000 0000 0... = Reserved Bits: 0
            .... .... .... .1.. = Include GT: True
            .... .... .... ..1. = Include PC: True
            .... .... .... ...1 = Include SSN: True
        **Subsystem number (0)**
            Parameter Tag: Subsystem number (0x8003)
            Parameter Length: 8
            Reserved: 000000
            **Subsystem Number: 0**
        Point code (7112)
            Parameter Tag: Point code (0x8002)
            Parameter Length: 8
            Point Code: 7112
        Global title
            Parameter Tag: Global title (0x8001)
            Parameter Length: 20
            Reserved: 000000
            GTI: 0x04
            Number of Digits: 15
            Translation Type: 0x00
            Numbering Plan: ISDN/Mobile Numbering Plan (Rec. E.214) (0x07)
            Nature of Address: International Number (0x04)
            Address information (digits): 550320300029365
    Sequence control (138)
        Parameter Tag: Sequence control (0x0116)
        Parameter Length: 8
        Sequence Control: 138
Data (72 bytes)

0000  62 46 48 04 00 00 00 01 6b 1e 28 1c 06 07 00 11   bFH.....k.(.....
0010  86 05 01 01 01 a0 11 60 0f 80 02 07 80 a1 09 06   .......`........
0020  07 04 00 00 01 00 0e 03 6c 1e a1 1c 02 04 00 00   ........l.......
0030  00 01 02 01 38 30 11 80 08 27 34 02 03 00 92 63   ....80...&#39;4....c
0040  05 02 01 01 05 00 81 00                           ........
    **Data: 62464804000000016b1e281c060700118605010101a01160...**
    [Length: 72]</code></pre><p>Is it because of ssn number being used as '0'?</p><p>Could some one please help me on this?</p><p>Thanks, Ravi</p></div><div id="question-tags" class="tags-container tags">sua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '11, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/f51f8e81268463b13b2e234031ede5c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rakolla&#39;s gravatar image" /><p>rakolla<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rakolla has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jan '12, 12:24</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-4953" class="comments-container"><span id="8379"></span><div id="comment-8379" class="comment"><div id="post-8379-score" class="comment-score"></div><div class="comment-text"><p>I tried with 0 for my traces but nothing changed, I am able to see as before. Could you please share your results, moreover whats the value configured for SUA, I mean the RFC. Thanks</p></div><div id="comment-8379-info" class="comment-info"><span class="comment-age">(13 Jan '12, 11:51)</span> gsmguy</div></div></div><div id="comment-tools-4953" class="comment-tools"></div><div class="clear"></div><div id="comment-4953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4971"></span>

<div id="answer-container-4971" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4971-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it because of ssn number being used as '0'? Yes You need to set the ssn preference of gsm_map to 0 in this case. Regards Anders</p></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '11, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '11, 16:59</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4971" class="comments-container"><span id="4974"></span><div id="comment-4974" class="comment"><div id="post-4974-score" class="comment-score"></div><div class="comment-text"><p>it worked! Thanks Anders</p></div><div id="comment-4974-info" class="comment-info"><span class="comment-age">(11 Jul '11, 00:28)</span> rakolla</div></div></div><div id="comment-tools-4971" class="comment-tools"></div><div class="clear"></div><div id="comment-4971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

