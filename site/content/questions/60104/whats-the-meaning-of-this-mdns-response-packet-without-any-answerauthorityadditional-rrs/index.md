+++
type = "question"
title = "what&#x27;s the meaning of this mDNS response packet without any answer/authority/additional RRs?"
description = '''As the title says, I got such a mDNS response from the link local ipv6 multicast address, my mDNS program complains about its empty response body and its truncated bit is not set, so what&#x27;s the purpose of this? Frame 27: 74 bytes on wire (592 bits), 74 bytes captured (592 bits) on interface 0 Ethern...'''
date = "2017-03-15T19:18:00Z"
lastmod = "2017-03-16T02:31:00Z"
weight = 60104
keywords = [ "mdns", "multicast", "ipv6" ]
aliases = [ "/questions/60104" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [what's the meaning of this mDNS response packet without any answer/authority/additional RRs?](/questions/60104/whats-the-meaning-of-this-mdns-response-packet-without-any-answerauthorityadditional-rrs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60104-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>As the title says, I got such a mDNS response from the link local ipv6 multicast address, my mDNS program complains about its empty response body and its truncated bit is not set, so what's the purpose of this?</p><pre><code>Frame 27: 74 bytes on wire (592 bits), 74 bytes captured (592 bits) on interface 0
Ethernet II, Src: Apple_98:31:19 (98:01:a7:98:31:19), Dst: IPv6mcast_fb (33:33:00:00:00:fb)
Internet Protocol Version 6, Src: fe80::70c9:a23a:12a2:4a45, Dst: ff02::fb
    0110 .... = Version: 6
    .... 0000 0000 .... .... .... .... .... = Traffic class: 0x00 (DSCP: CS0, ECN: Not-ECT)
    .... .... .... 0000 0000 0000 0000 0000 = Flow label: 0x00000
    Payload length: 20
    Next header: UDP (17)
    Hop limit: 1
    Source: fe80::70c9:a23a:12a2:4a45
    Destination: ff02::fb
    [Source GeoIP: Unknown]
    [Destination GeoIP: Unknown]
User Datagram Protocol, Src Port: 5353, Dst Port: 5353
    Source Port: 5353
    Destination Port: 5353
    Length: 20
    Checksum: 0xe389 [unverified]
    [Checksum Status: Unverified]
    [Stream index: 3]
Multicast Domain Name System (response)
    Transaction ID: 0x0000
    Flags: 0x8400 Standard query response, No error
        1... .... .... .... = Response: Message is a response
        .000 0... .... .... = Opcode: Standard query (0)
        .... .1.. .... .... = Authoritative: Server is an authority for domain
        .... ..0. .... .... = Truncated: Message is not truncated
        .... ...0 .... .... = Recursion desired: Don&#39;t do query recursively
        .... .... 0... .... = Recursion available: Server can&#39;t do recursive queries
        .... .... .0.. .... = Z: reserved (0)
        .... .... ..0. .... = Answer authenticated: Answer/authority portion was not authenticated by the server
        .... .... ...0 .... = Non-authenticated data: Unacceptable
        .... .... .... 0000 = Reply code: No error (0)
    Questions: 0
    Answer RRs: 0
    Authority RRs: 0
    Additional RRs: 0</code></pre></div><div id="question-tags" class="tags-container tags">mdns multicast ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '17, 19:18</strong></p><img src="https://secure.gravatar.com/avatar/75de90cd2dddc1467b3f3db8d49dfb30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfly&#39;s gravatar image" /><p>jfly<br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfly has no accepted answers">0%</span></p></div></div><div id="comments-container-60104" class="comments-container"></div><div id="comment-tools-60104" class="comment-tools"></div><div class="clear"></div><div id="comment-60104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60105"></span>

<div id="answer-container-60105" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60105-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>How about <a href="https://social.technet.microsoft.com/Forums/en-US/b334e797-ef80-4525-b74a-b4830420a14e/windows-10-spams-network-with-invalid-mdns-response-packets?forum=win10itpronetworking">this</a>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '17, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60105" class="comments-container"><span id="60140"></span><div id="comment-60140" class="comment"><div id="post-60140-score" class="comment-score"></div><div class="comment-text"><p>Indeed, I checked the source of these packets, they are all Windows 10 PC.</p></div><div id="comment-60140-info" class="comment-info"><span class="comment-age">(17 Mar '17, 02:29)</span> jfly</div></div></div><div id="comment-tools-60105" class="comment-tools"></div><div class="clear"></div><div id="comment-60105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

