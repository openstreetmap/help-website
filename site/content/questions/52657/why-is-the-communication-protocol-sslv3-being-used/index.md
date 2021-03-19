+++
type = "question"
title = "Why is the communication protocol SSLv3 being used?"
description = '''This is the first time I have had to delve down to the depths of network traces, so please excuse my ignorance. We have a working interface between one of our systems and an external company. The other day it stopped working and after a bit of investigation we discovered that they had turned off sup...'''
date = "2016-05-16T21:50:00Z"
lastmod = "2016-05-18T06:46:00Z"
weight = 52657
keywords = [ "tls", "ssl" ]
aliases = [ "/questions/52657" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why is the communication protocol SSLv3 being used?](/questions/52657/why-is-the-communication-protocol-sslv3-being-used)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52657-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is the first time I have had to delve down to the depths of network traces, so please excuse my ignorance. We have a working interface between one of our systems and an external company. The other day it stopped working and after a bit of investigation we discovered that they had turned off support for SSLv3. This seems to be a wise thing to do. However it broke the communications so we had to get them to turn it back on. We are using SAP on our end. All the research I have done indicates that we should support TLS. So it seemed strange that SSL v3 was being used after all. I ran a wireshark trace to hopefully tell me what was going on. Below is the extract. But I don’t know how to interpret it. It says the Handshake protocol is TLSv1, but then there is a mention of Version SSL 3.0. Does that mean it is using SSL 3.0 . If that is the case, how do I found out why isn’t it using TLS?</p><pre><code>Frame 4: 114 bytes on wire (912 bits), 114 bytes captured (912 bits) on interface 0
Ethernet II, Src: Vmware_9e:4a:78 (00:50:56:9e:4a:78), Dst: All-HSRP-routers_01 (00:00:0c:07:ac:01)
Internet Protocol Version 4, Src: 10.6.243.200, Dst: 203.27.124.106
Transmission Control Protocol, Src Port: 61460 (61460), Dst Port: 443 (443), Seq: 1, Ack: 1, Len: 60
Secure Sockets Layer
    TLSv1 Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: SSL 3.0 (0x0300)
        Length: 55
        Handshake Protocol: Client Hello
            Handshake Type: Client Hello (1)
            Length: 51
            Version: TLS 1.0 (0x0301)
            Random
            Session ID Length: 0
            Cipher Suites Length: 12
            Cipher Suites (6 suites)
                Cipher Suite: TLS_RSA_WITH_AES_128_CBC_SHA (0x002f)
                Cipher Suite: TLS_RSA_WITH_AES_256_CBC_SHA (0x0035)
                Cipher Suite: TLS_RSA_WITH_RC4_128_SHA (0x0005)
                Cipher Suite: TLS_RSA_WITH_RC4_128_MD5 (0x0004)
                Cipher Suite: TLS_RSA_WITH_3DES_EDE_CBC_SHA (0x000a)
                Cipher Suite: TLS_EMPTY_RENEGOTIATION_INFO_SCSV (0x00ff)
            Compression Methods Length: 1
            Compression Methods (1 method)</code></pre>regards Tony Lewis</div><div id="question-tags" class="tags-container tags">tls ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '16, 21:50</strong></p><img src="https://secure.gravatar.com/avatar/18e37f8924f0ab3c3316b89fa7b2f89c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awlwiles&#39;s gravatar image" /><p>awlwiles<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awlwiles has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '16, 01:23</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-52657" class="comments-container"><span id="52660"></span><div id="comment-52660" class="comment"><div id="post-52660-score" class="comment-score"></div><div class="comment-text"><p>A text dump doesn't help, nor a single packet.</p><p>Please post a capture file (not plain text) somewhere of the full connection negotiation, so an attempt can be made to understand the negotiations that go on.</p></div><div id="comment-52660-info" class="comment-info"><span class="comment-age">(17 May '16, 01:26)</span> Jaap ♦</div></div><span id="52754"></span><div id="comment-52754" class="comment"><div id="post-52754-score" class="comment-score"></div><div class="comment-text"><p>Thank you all for your input so far. I may not be permitted to post a full trace file. However I think the tips people have provided will enable us to resolve the issue. If and when we do I will post the fix here. I am going to get them to re-active the change that disabled SSLv3 so I can gather more details. regards Tony Lewis</p></div><div id="comment-52754-info" class="comment-info"><span class="comment-age">(18 May '16, 22:58)</span> awlwiles</div></div></div><div id="comment-tools-52657" class="comment-tools"></div><div class="clear"></div><div id="comment-52657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52665"></span>

<div id="answer-container-52665" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52665-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A generic answer maybe:</p><ul><li><p>SSL was the original name, TLS took over at some point, and the numbering was both restarted and changed. So the last SSL (3.0) has evolved into TLS v1.0. So counter-intuitively, TLS v1.2 is newer (more advanced) than SSL 3.0.</p></li><li><p>the dissectors follow the evolution of the protocols, but as many protocol fields are identical for SSL and TLS, you can see "Version: SSL 3.0 (0x0300)" in a TLSv1 packet because the dissector for SSL1.0 through to TLSv1.2 is (most likely, I'm not a core developer) the very same code. The packet whose text dissection you've posted seems to still be TLSv1.0, however in later phase of the client/server negotiation, the connection may have become a pure SSL 3.0.</p></li><li><p>as time goes, older protocols become obsolete, which is best seen in the security area where new vulnerabilities are discovered, so use of older versions of this SSL/TLS family (all SSL versions and TLSv1.0 included) is discouraged as they are not considered safe any more.</p></li></ul><p>So re-enabling of TLSv1.0 (or even SSL3.0) at the external company side should be considered only a <em>workaround</em>. The <em>solution</em> should be to implement (activate?) support of TLS1.2 at your end.</p><p>Analysis of the whole capture from the negotiation phase can tell you what versions of TLS the external company's server currently offers, and where the negotiation actually ends (SSL 3.0 or TLSv1.0) while the workaround is in place.</p><p>The only answer to the "why" which Wireshark can give you is "because this side of the conversation has asked for that, and the other side has agreed". But the answer to "why this side has asked for that" is something Wireshark cannot tell you. To get this answer, you have to talk to the administrator and/or developer of that side.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '16, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '16, 05:12</p></div></div><div id="comments-container-52665" class="comments-container"></div><div id="comment-tools-52665" class="comment-tools"></div><div class="clear"></div><div id="comment-52665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52722"></span>

<div id="answer-container-52722" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52722-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The two versions you see are for different purposes. SSL 3.0 and TLS 1.0 up to 1.2 have a record layer containing a version (SSL 3.0 in your case) which roughtly advertises the minimum supported version. The version included in the Client Hello message (TLS 1.0 in your case) is the highest version supported by the client.</p><p>According to your capture the client indeed supports TLS 1.0. Its set of supported cipher suites is however not that strong. Your external company might require more secure ciphers. See <a href="https://wiki.mozilla.org/Security/Server_Side_TLS">https://wiki.mozilla.org/Security/Server_Side_TLS</a> for what is considered acceptable.</p><p>Misbehaved servers will immediately reset the connection if they do not understand/accept the Client Hello. Good implementations will however send an "Alert" containing the reason why the connection fails. Possible reasons include <code>handshake_failure</code> and <code>insufficient_security</code>. Their meanings can be found in <a href="https://tools.ietf.org/html/rfc5246#section-7.2.2">RFC 5246 (TLS 1.2) - 7.2.2. Error Alerts</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '16, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-52722" class="comments-container"></div><div id="comment-tools-52722" class="comment-tools"></div><div class="clear"></div><div id="comment-52722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

