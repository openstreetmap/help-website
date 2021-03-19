+++
type = "question"
title = "Malformed 32 byte TLS/SSL packet"
description = '''I have the following packet when trying to examine an SSL session. This is a local capture but I have a capture from the target network as well. I see the same packet on both ends. Frame 16: 540 bytes on wire (4320 bits), 540 bytes captured (4320 bits) Internet Protocol Version 4, Src: 172.20.2.164 ...'''
date = "2012-06-19T09:34:00Z"
lastmod = "2012-06-20T06:05:00Z"
weight = 12062
keywords = [ "tls", "malformed" ]
aliases = [ "/questions/12062" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed 32 byte TLS/SSL packet](/questions/12062/malformed-32-byte-tlsssl-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12062-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following packet when trying to examine an SSL session. This is a local capture but I have a capture from the target network as well. I see the same packet on both ends.</p><pre><code>Frame 16: 540 bytes on wire (4320 bits), 540 bytes captured (4320 bits)
Internet Protocol Version 4, Src: 172.20.2.164 (172.20.2.164), Dst: 169.20.69.250 (169.20.69.250)
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
    Total Length: 526
    Flags: 0x02 (Don&#39;t Fragment)
    Header checksum: 0x790d [correct]
Transmission Control Protocol, Src Port: 57599 (57599), Dst Port: https (443), Seq: 2331060189, Ack: 18913651, Len: 474
Checksum: 0x56c7 [validation disabled]
Secure Sockets Layer
     TLSv1 Record Layer: Application Data Protocol: tcp
        Content Type: Application Data (23)
        Version: TLS 1.0 (0x0301)
        Length: 32
        Encrypted Application Data: 6a19a737cd1b4b0478dadd0a907f3b48fe6ba2b1c4a0bc6d...
    [Malformed Packet: TCP]
        Expert Info (Error/Malformed): Malformed Packet (Exception occurred)</code></pre><p>IP's have been changed but the issue is the TLS record length. This is the packet being transmitted and received and the server is able to decrypt and process it correctly. The packet is what I believe to be the "GET" request. I just don't understand why the TLS length is so short. This is not part of a fragment. I am using the WireShark 1.6.2. Is this a problem with WireShark or the traffic? This is not a one off packet, my session contains multiple "malformed" 32 length TLS records, always from my client to the server.</p></div><div id="question-tags" class="tags-container tags">tls malformed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '12, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/5cba7e1eb0723df16b550c2c72d751dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DigitalCowboy&#39;s gravatar image" /><p>DigitalCowboy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DigitalCowboy has no accepted answers">0%</span></p></div></div><div id="comments-container-12062" class="comments-container"><span id="12064"></span><div id="comment-12064" class="comment"><div id="post-12064-score" class="comment-score"></div><div class="comment-text"><p>I found that WireShark appears to be ignoring the followup SSL data, after that first 32 byte chunk (which decrypts to a G) there is another SSL record that is not being parsed correctly. Is this error fixed in later versions of WireShark?</p></div><div id="comment-12064-info" class="comment-info"><span class="comment-age">(19 Jun '12, 14:05)</span> DigitalCowboy</div></div></div><div id="comment-tools-12062" class="comment-tools"></div><div class="clear"></div><div id="comment-12062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12071"></span>

<div id="answer-container-12071" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12071-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is only one way to to be sure whether this issue has been fixed in a later release and that is to test it with a later release. But as I have not seen this kind of behavior with the SSL dissector, my guess is it is a bug triggered by your specific capture that might not have been fixed yet.</p><p>If the problem still exists with the latest 1.6.x release, please file a bug report on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and attach the capture file (you can mark it as private to make it only available to the core-developers).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '12, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-12071" class="comments-container"></div><div id="comment-tools-12071" class="comment-tools"></div><div class="clear"></div><div id="comment-12071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

