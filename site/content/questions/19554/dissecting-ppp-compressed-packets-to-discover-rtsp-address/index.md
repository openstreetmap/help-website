+++
type = "question"
title = "dissecting PPP compressed packets to discover rtsp address"
description = '''Hi there I&#x27;m trying to find the rtsp URL for a video using Wireshark. I am only able to connect to the site and play the video using a VPN. I start Wireshark sniffing on wlan0 and when I stop the capture and sort the captured packets by protocol, I don&#x27;t see any that are listed RTSP. However, there ...'''
date = "2013-03-16T03:17:00Z"
lastmod = "2013-03-25T15:18:00Z"
weight = 19554
keywords = [ "ppp", "vpn", "compressed" ]
aliases = [ "/questions/19554" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [dissecting PPP compressed packets to discover rtsp address](/questions/19554/dissecting-ppp-compressed-packets-to-discover-rtsp-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19554-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there I'm trying to find the rtsp URL for a video using Wireshark. I am only able to connect to the site and play the video using a VPN. I start Wireshark sniffing on wlan0 and when I stop the capture and sort the captured packets by protocol, I don't see any that are listed RTSP. However, there are a whole heap of PPP compressed datagrams. If I were able to decompress these PPP packets, would the data inside them contain the RTSP URL? Furthermore, is there any way to decompress these packets using Wireshark? Thanks.</p></div><div id="question-tags" class="tags-container tags">ppp vpn compressed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '13, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/1c268a5e86ca2bb5431ea5f7d0ef413e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daloonik&#39;s gravatar image" /><p>daloonik<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daloonik has no accepted answers">0%</span></p></div></div><div id="comments-container-19554" class="comments-container"></div><div id="comment-tools-19554" class="comment-tools"></div><div class="clear"></div><div id="comment-19554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19565"></span>

<div id="answer-container-19565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19565-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>If I were able to decompress these PPP packets, would the data inside them contain the RTSP URL?</p></blockquote><p>Yes, if they contain the RTSP traffic, otherwise, no.</p><blockquote><p>is there any way to decompress these packets using Wireshark?</p></blockquote><p>What form of compression are they using?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '13, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19565" class="comments-container"><span id="19571"></span><div id="comment-19571" class="comment"><div id="post-19571-score" class="comment-score"></div><div class="comment-text"><p>I'm using www.freecanadavpn.com, so I'm guessing they're compressed using GRE?</p></div><div id="comment-19571-info" class="comment-info"><span class="comment-age">(16 Mar '13, 14:52)</span> daloonik</div></div><span id="19577"></span><div id="comment-19577" class="comment"><div id="post-19577-score" class="comment-score"></div><div class="comment-text"><p>GRE is a tunneling mechanisms, not a compression mechanism. FreeCanadaVPN speak of PPTP, and <a href="http://technet.microsoft.com/en-us/library/cc958045.aspx">this Microsoft page on PPTP</a> says PPTP uses "a modified version of Generic Routing Encapsulation (GRE) to encapsulate PPP frames as tunneled data" and that "PPTP inherits encryption or compression, or both, of PPP payloads from PPP."</p><p>PPP has the Compression Control Protocol, as specified by <a href="http://tools.ietf.org/html/rfc1962">RFC 1962</a>, which allows many different compression algorithms to be negotiated.</p></div><div id="comment-19577-info" class="comment-info"><span class="comment-age">(16 Mar '13, 16:43)</span> Guy Harris ♦♦</div></div><span id="19578"></span><div id="comment-19578" class="comment"><div id="post-19578-score" class="comment-score"></div><div class="comment-text"><p>So are you seeing any Compression Control Protocol packets when the session starts up, to show what form of compression is being negotiated? The form of compression being negotiated might, or might not, be one that Wireshark knows how to decompress.</p></div><div id="comment-19578-info" class="comment-info"><span class="comment-age">(16 Mar '13, 16:44)</span> Guy Harris ♦♦</div></div><span id="19823"></span><div id="comment-19823" class="comment"><div id="post-19823-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response. Based on what I can see below, I'd say Microsoft PPC. Is this correct?</p><pre><code>Internet Protocol Version 4, Src: 192.168.xx.xxx (192.168.xx.xxx), Dst: 184.107.xxx.xxx (184.107.xxx.xxx)
Generic Routing Encapsulation (PPP)
Point-to-Point Protocol
    Protocol: Compression Control Protocol (0x80fd)
PPP Compression Control Protocol
    Code: Configuration Request (0x01)
    Identifier: 0x02
    Length: 10
    Options: (6 bytes)
        Microsoft PPC: Supported Bits: 0x01000040</code></pre></div><div id="comment-19823-info" class="comment-info"><span class="comment-age">(25 Mar '13, 13:09)</span> daloonik</div></div></div><div id="comment-tools-19565" class="comment-tools"></div><div class="clear"></div><div id="comment-19565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19824"></span>

<div id="answer-container-19824" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19824-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Based on what I can see below, I'd say Microsoft PPC. Is this correct?</p></blockquote><p>According to <a href="http://tools.ietf.org/html/rfc2118">RFC 2118</a>, the low-order bit of "Supported Bits" is set if compression is being requested, but that bit isn't set. According to <a href="http://tools.ietf.org/html/rfc3078">RFC 3078</a>, the two bits that <em>are</em> set in "Supported Bits" request 128-bit encryption and stateless mode.</p><p>So I think the answer to your question is "no"; confusingly, the packets aren't compressed, but they <em>are</em> encrypted. Decrypting will probably require not only code but also the initial session key (or information sufficient to derive it).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '13, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19824" class="comments-container"></div><div id="comment-tools-19824" class="comment-tools"></div><div class="clear"></div><div id="comment-19824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

