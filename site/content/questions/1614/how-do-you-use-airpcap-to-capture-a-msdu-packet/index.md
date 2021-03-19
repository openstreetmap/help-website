+++
type = "question"
title = "how do you use AirPcap to capture A-MSDU packet?"
description = '''Hello everyone! I want to capture A-MSDU. I use AirPcap, but I don&#x27;t khown how will A-MSDU appear? I read some document that show A-MSDU in UDP packets. So how do i have to crate it so that i have A-MSDU quickly and exactly. Thank everyone for your help!!!'''
date = "2011-01-04T01:22:00Z"
lastmod = "2011-01-05T10:17:00Z"
weight = 1614
keywords = [ "capture" ]
aliases = [ "/questions/1614" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how do you use AirPcap to capture A-MSDU packet?](/questions/1614/how-do-you-use-airpcap-to-capture-a-msdu-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1614-score" class="post-score" title="current number of votes">0</div><span id="post-1614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone! I want to capture A-MSDU. I use AirPcap, but I don't khown how will A-MSDU appear? I read some document that show A-MSDU in UDP packets. So how do i have to crate it so that i have A-MSDU quickly and exactly. Thank everyone for your help!!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '11, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/4f406866b1740fdc247ba628d2515395?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haquyen&#39;s gravatar image" /><p><span>haquyen</span><br />
<span class="score" title="1 reputation points">1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haquyen has no accepted answers">0%</span></p></div></div><div id="comments-container-1614" class="comments-container"></div><div id="comment-tools-1614" class="comment-tools"></div><div class="clear"></div><div id="comment-1614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1635"></span>

<div id="answer-container-1635" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1635-score" class="post-score" title="current number of votes">1</div><span id="post-1635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi haquen, here is a sample decode of packet captured with an AirPcap Nx adapter. Scroll half way down for the 'IEEE 802.11 Aggregate MSDU' section.</p><p>Martin Lewald</p><pre><code>Frame 8: 171 bytes on wire (1368 bits), 171 bytes captured (1368 bits)
**PPI version 0, 48 bytes**
Version: 0
Flags: 0x00
Header length: 48
DLT: 105
802.11-Common
802.11n MAC
**IEEE 802.11 QoS Data, Flags: .......TC**
Type/Subtype: QoS Data (0x28)
Frame Control: 0x0188 (Normal)
Duration: 44
BSS Id: Buffalo_6f:03:c7 (00:16:01:6f:03:c7)
Source address: Buffalo_73:02:51 (00:16:01:73:02:51)
Destination address: Buffalo_6f:03:c7 (00:16:01:6f:03:c7)
Fragment number: 0
Sequence number: 812
Frame check sequence: 0x2c0a88fb [correct]
    [Good: True]
    [Bad: False]
QoS Control
**IEEE 802.11 Aggregate MSDU**
A-MSDU Subframe #1
    Destination address: 3com_27:f9:b2 (00:01:02:27:f9:b2)
    Source address: Buffalo_73:02:51 (00:16:01:73:02:51)
    MSDU length: 0x004F
    Logical-Link Control
        DSAP: SNAP (0xaa)
        IG Bit: Individual
        SSAP: SNAP (0xaa)
        CR Bit: Command
        Control field: U, func=UI (0x03)
        Organization Code: Encapsulated Ethernet (0x000000)
        Type: IP (0x0800)
    Internet Protocol, Src: 192.168.1.131 (192.168.1.131), Dst: 208.120.229.215 (208.120.229.215)
        Version: 4
        Header length: 20 bytes
        Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00)
        Total Length: 71
        Identification: 0x86cd (34509)
        Flags: 0x02 (Don&#39;t Fragment)
        Fragment offset: 0
        Time to live: 128
        Protocol: TCP (6)
        Header checksum: 0xfb67 [correct]
        Source: 192.168.1.131 (192.168.1.131)
        Destination: 208.120.229.215 (208.120.229.215)
    Transmission Control Protocol, Src Port: iec-104 (2404), Dst Port: 28249 (28249), Seq: 1, Ack: 1, Len: 19
        Source port: iec-104 (2404)
        Destination port: 28249 (28249)
        [Stream index: 0]
        Sequence number: 1    (relative sequence number)
        [Next sequence number: 20    (relative sequence number)]
        Acknowledgement number: 1    (relative ack number)
        Header length: 32 bytes
        Flags: 0x18 (PSH, ACK)
            000. .... .... = Reserved: Not set
            ...0 .... .... = Nonce: Not set
            .... 0... .... = Congestion Window Reduced (CWR): Not set
            .... .0.. .... = ECN-Echo: Not set
            .... ..0. .... = Urgent: Not set
            .... ...1 .... = Acknowledgement: Set
            .... .... 1... = Push: Set
            .... .... .0.. = Reset: Not set
            .... .... ..0. = Syn: Not set
            .... .... ...0 = Fin: Not set
        Window size: 32732
        Checksum: 0xc1fb [validation disabled]
            [Good Checksum: False]
            [Bad Checksum: False]
        Options: (12 bytes)
            NOP
            NOP
            Timestamps: TSval 1266352, TSecr 410613
        [SEQ/ACK analysis]
            [Number of bytes in flight: 19]
        [PDU Size: 19]
    IEC 60870-5-104-Apci: &lt;ERR 19 bytes&gt;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '11, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/669134f99381da9902f84ea4c2b81967?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martin%20Lewald&#39;s gravatar image" /><p><span>Martin Lewald</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martin Lewald has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jan '11, 10:18</strong> </span></p></div></div><div id="comments-container-1635" class="comments-container"></div><div id="comment-tools-1635" class="comment-tools"></div><div class="clear"></div><div id="comment-1635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

