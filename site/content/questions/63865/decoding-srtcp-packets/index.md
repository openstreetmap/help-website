+++
type = "question"
title = "Decoding SRTCP Packets"
description = '''Hello, I am trying to decode SRTCP packets. I have the private key and specified it at Edit -&amp;gt; Preferences -&amp;gt; Protocols -&amp;gt; SSL. My SIP and RTP packets are decoding fine, but my RTCP packets are not. According to the Wiki page for RTCP (https://wiki.wireshark.org/RTCP) at the very bottom of ...'''
date = "2017-10-13T06:41:00Z"
lastmod = "2017-10-13T08:56:00Z"
weight = 63865
keywords = [ "srtcp", "rtcp", "decryption", "ssl" ]
aliases = [ "/questions/63865" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding SRTCP Packets](/questions/63865/decoding-srtcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63865-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to decode SRTCP packets. I have the private key and specified it at Edit -&gt; Preferences -&gt; Protocols -&gt; SSL. My SIP and RTP packets are decoding fine, but my RTCP packets are not. According to the Wiki page for RTCP (<a href="https://wiki.wireshark.org/RTCP)">https://wiki.wireshark.org/RTCP)</a> at the very bottom of the discussion, it is written, "SRT(C)P handling was recently added to both dissectors. (JaapKeuter)" so I am believing that Wireshark has the ability to SSL decode these packets.</p><p>My settings at Edit -&gt; Preferences -&gt; Protocols -&gt; SSL -&gt; RSA Keys List has the correct IP address, rtcp for protocol, and points to the private key. For port, I've tried our SIP/TLS port (we run on a non-standard port), 0, 32513 (the port on which SRTCP packets on this specific capture appear), but no matter what, they Sender Report isn't decrypted to where I can see it. Here's what I get:</p><p><code>Frame 20: 104 bytes on wire (832 bits), 104 bytes captured (832 bits) on interface 0 Ethernet II, Src: Jetcell_bb:15:1b (00:d0:2b:bb:15:1b), Dst: SuperMic_04:29:a4 (00:25:90:04:29:a4) Internet Protocol Version 4, Src: 1.2.3.4, Dst: 1.2.4.4 User Datagram Protocol, Src Port: 12147, Dst Port: 32513 Real-time Transport Control Protocol (Receiver Report)     [Stream setup by SDP (frame 6)]     10.. .... = Version: RFC 1889 Version (2)     ..0. .... = Padding: False     ...0 0000 = Reception report count: 0     Packet type: Receiver Report (201)     Length: 1 (8 bytes)     Sender SSRC: 0x4f468afd (1330023165)     Encrypted RTCP Payload - not dissected         [Expert Info (Warning/Undecoded): Encrypted RTCP Payload - not dissected]             [Encrypted RTCP Payload - not dissected]             [Severity level: Warning]             [Group: Undecoded]     1... .... .... .... .... .... .... .... = SRTCP E flag: True     .000 0000 0000 0000 0000 0000 0000 0000 = SRTCP Index: 0 (0x00000000)     SRTCP Auth Tag: 8210f9afd49d19feda38</code></p><p>Does anyone have decryption of SRTCP packets working? Ideas or advice for making this work?</p><p>Thanks,</p><p>Dave</p></div><div id="question-tags" class="tags-container tags">srtcp rtcp decryption ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '17, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/9dd4f945c9f4fa18fb38ab5b170ebc2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidSovereen&#39;s gravatar image" /><p>DavidSovereen<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidSovereen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Oct '17, 06:49</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-63865" class="comments-container"></div><div id="comment-tools-63865" class="comment-tools"></div><div class="clear"></div><div id="comment-63865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63867"></span>

<div id="answer-container-63867" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63867-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are aware the TLS and SRTP have little to do with each other, right?</p><p>In short they have nothing to to do with each other, while the long answer is that the signalling used for key exchange for the SRTP session may be accessible if the corresponding SDP exchange is accessible through the use of TLS decryption.</p><p>When this is not clear, consider the following. SIP is used for session control and SDP for the media session. When Secure RTP is involved, media key exchange has to take place, which can be done through SDP. This is only sensible if the key exchange itself is protected, eg. by (D)TLS. So having the option to decrypt SIP/TLS, and therefore SDP, gives you access to the media encryption keys. That is how this binds together.</p><p>This also tells you that it is a matter of using the media encryption keys to decrypt the SRTP and SRTCP packets. Well, Wireshark doesn't do that (yet). What is does do is being aware that the RTP and RTCP packets are encrypted and thus dissect the fields in these packets with that in fact in mind. They therefore also do not show decrypted data, since it is not capable of doing that right now.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '17, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63867" class="comments-container"><span id="63871"></span><div id="comment-63871" class="comment"><div id="post-63871-score" class="comment-score"></div><div class="comment-text"><p>We've been running SIP/RTP and are just starting our transition into SIP/TLS and SRTP. I hadn't looked at all into where and how the media encryption keys for RTP were transmitted, but its helpful for you to point this out; your explanation makes perfect sense.</p><p>I assumed that SRTP was visible, but now see that it is not. We have a monitoring system for our VoIP network and it decrypts the SIP/TLS traffic with use of the private key. It immediately began generating trouble reports from (S)RTCP packets, and it became apparent that it could not decrypt them.</p><p>Is decrypting SRTP and SRTCP packets on a roadmap for Wireshark? Is there a roadmap? If its all volunteer contributions, is there a method for donating or paying a bounty to get new types of analysis, like SRTP/SRTCP decryption done?</p><p>Thanks,</p><p>Dave</p></div><div id="comment-63871-info" class="comment-info"><span class="comment-age">(13 Oct '17, 12:21)</span> DavidSovereen</div></div><span id="63891"></span><div id="comment-63891" class="comment"><div id="post-63891-score" class="comment-score"></div><div class="comment-text"><p>It would surprise me if the monitoring system would be able to decrypt SIP/TLS but then expects RTP/RTCP to be unencrypted.</p><p>As for a roadmap, no there isn't one, other than a rough release schedule. It's all (except the work that Gerald does) volunteers, doing there bit, catching their itch. This particular subject has been itching some of use already, but I've seen nothing come to fruition as of yet.</p><p>You could contact the community at the <a href="https://www.wireshark.org/lists/">wireshark-dev mailing list</a> to get in touch with a competent developer.</p></div><div id="comment-63891-info" class="comment-info"><span class="comment-age">(14 Oct '17, 02:06)</span> Jaap ♦</div></div></div><div id="comment-tools-63867" class="comment-tools"></div><div class="clear"></div><div id="comment-63867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

