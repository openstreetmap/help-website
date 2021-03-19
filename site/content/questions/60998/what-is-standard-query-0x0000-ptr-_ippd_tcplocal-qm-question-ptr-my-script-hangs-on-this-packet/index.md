+++
type = "question"
title = "What is &quot;Standard query  0x0000 PTR, _ippd._tcp.local, &quot;QM&quot; question PTR&quot; ? My script hangs on this packet ."
description = '''I have implemented socket client to communicate with my device from pc. The program successfully establishes the communication with device and starts to send/recieve packets but then it hangs. Here the Wireshark log where it has been hanged  And here it the Frame 191 whereit hangs  Frame 191: 87 byt...'''
date = "2017-04-24T02:22:00Z"
lastmod = "2017-04-24T04:10:00Z"
weight = 60998
keywords = [ "tcp", "socket", "stream", "wireshark" ]
aliases = [ "/questions/60998" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is "Standard query 0x0000 PTR, \_ippd.\_tcp.local, "QM" question PTR" ? My script hangs on this packet .](/questions/60998/what-is-standard-query-0x0000-ptr-_ippd_tcplocal-qm-question-ptr-my-script-hangs-on-this-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60998-score" class="post-score" title="current number of votes">0</div><span id="post-60998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have implemented socket client to communicate with my device from pc. The program successfully establishes the communication with device and starts to send/recieve packets but then it hangs. Here the Wireshark log where it has been hanged <img src="https://osqa-ask.wireshark.org/upfiles/ws5.png" alt="alt text" /></p><pre><code>And here it the Frame 191 whereit hangs

Frame 191: 87 bytes on wire (696 bits), 87 bytes captured (696 bits) on interface 0
    Interface id: 0 (wlx30b5c2125754)
    Encapsulation type: Ethernet (1)
    Arrival Time: Apr 24, 2017 05:14:09.911227896 +04
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1492996449.911227896 seconds
    [Time delta from previous captured frame: 0.524355526 seconds]
    [Time delta from previous displayed frame: 0.524355526 seconds]
    [Time since reference or first frame: 3.809895894 seconds]
    Frame Number: 191
    Frame Length: 87 bytes (696 bits)
    Capture Length: 87 bytes (696 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:udp:mdns]
    [Coloring Rule Name: UDP]
    [Coloring Rule String: udp]
Ethernet II, Src: Tp-LinkT_12:57:54 (30:b5:c2:12:57:54), Dst: IPv4mcast_fb (01:00:5e:00:00:fb)
    Destination: IPv4mcast_fb (01:00:5e:00:00:fb)
    Source: Tp-LinkT_12:57:54 (30:b5:c2:12:57:54)
    Type: IPv4 (0x0800)
Internet Protocol Version 4, Src: 172.16.87.84, Dst: 224.0.0.251
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
    Total Length: 73
    Identification: 0xf52d (62765)
    Flags: 0x02 (Don&#39;t Fragment)
        0... .... = Reserved bit: Not set
        .1.. .... = Don&#39;t fragment: Set
        ..0. .... = More fragments: Not set
    Fragment offset: 0
    Time to live: 255
    Protocol: UDP (17)
    Header checksum: 0xa215 [correct]
    [Header checksum status: Good]
    [Calculated Checksum: 0xa215]
    Source: 172.16.87.84
    Destination: 224.0.0.251
    [Source GeoIP: Unknown]
    [Destination GeoIP: Unknown]
User Datagram Protocol, Src Port: 5353, Dst Port: 5353
Multicast Domain Name System (query)
    Transaction ID: 0x0000
    Flags: 0x0000 Standard query
        0... .... .... .... = Response: Message is a query
        .000 0... .... .... = Opcode: Standard query (0)
        .... ..0. .... .... = Truncated: Message is not truncated
        .... ...0 .... .... = Recursion desired: Don&#39;t do query recursively
        .... .... .0.. .... = Z: reserved (0)
        .... .... ...0 .... = Non-authenticated data: Unacceptable
    Questions: 2
    Answer RRs: 0
    Authority RRs: 0
    Additional RRs: 0
    Queries
        _ipps._tcp.local: type PTR, class IN, &quot;QM&quot; question
            Name: _ipps._tcp.local
            [Name Length: 16]
            [Label Count: 3]
            Type: PTR (domain name PoinTeR) (12)
            .000 0000 0000 0001 = Class: IN (0x0001)
            0... .... .... .... = &quot;QU&quot; question: False
        _ipp._tcp.local: type PTR, class IN, &quot;QM&quot; question
            Name: _ipp._tcp.local
            [Name Length: 15]
            [Label Count: 3]
            Type: PTR (domain name PoinTeR) (12)
            .000 0000 0000 0001 = Class: IN (0x0001)
            0... .... .... .... = &quot;QU&quot; question: False

    192 3.816102710    fe80::2dad:1d24:560e:dfff ff02::fb              MDNS     107    Standard query 0x0000 PTR _ipps._tcp.local, &quot;QM&quot; question PTR _ipp._tcp.local, &quot;QM&quot; question</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '17, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/4cd73fb7c739ce6825247b45d3298096?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vardan9&#39;s gravatar image" /><p><span>Vardan9</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vardan9 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Apr '17, 02:27</strong> </span></p></div></div><div id="comments-container-60998" class="comments-container"></div><div id="comment-tools-60998" class="comment-tools"></div><div class="clear"></div><div id="comment-60998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61002"></span>

<div id="answer-container-61002" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61002-score" class="post-score" title="current number of votes">1</div><span id="post-61002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a <a href="https://en.wikipedia.org/wiki/Multicast_DNS">mDNS</a> query of a device using <a href="https://en.wikipedia.org/wiki/Zero-configuration_networking">Zeroconf</a>/Bonjour trying to find a printer service on the local network.</p><p>As your haven't given any information about your client application it's hard to say if the mDNS packets affects your application.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '17, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-61002" class="comments-container"></div><div id="comment-tools-61002" class="comment-tools"></div><div class="clear"></div><div id="comment-61002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

