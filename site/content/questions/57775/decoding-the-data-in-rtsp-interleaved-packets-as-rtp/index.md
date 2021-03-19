+++
type = "question"
title = "decoding the data in RTSP interleaved packets as RTP"
description = '''I was wondering how to decode the data in RTSP interleaved packets as RTP, like when in case of rtp over udp, we can use the &#x27;decode as&#x27; feature on the UDP packet and select RTP and can see the RTP headers. I want to do something similar in RTSP interleaved case.'''
date = "2016-12-01T21:50:00Z"
lastmod = "2016-12-03T02:51:00Z"
weight = 57775
keywords = [ "interleave", "rtsp", "rtp" ]
aliases = [ "/questions/57775" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [decoding the data in RTSP interleaved packets as RTP](/questions/57775/decoding-the-data-in-rtsp-interleaved-packets-as-rtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57775-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was wondering how to decode the data in RTSP interleaved packets as RTP, like when in case of rtp over udp, we can use the 'decode as' feature on the UDP packet and select RTP and can see the RTP headers. I want to do something similar in RTSP interleaved case.</p></div><div id="question-tags" class="tags-container tags">interleave rtsp rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '16, 21:50</strong></p><img src="https://secure.gravatar.com/avatar/71bf6857a6516d2b1f5c19500d67742c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="streamfanatic&#39;s gravatar image" /><p>streamfanatic<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="streamfanatic has no accepted answers">0%</span></p></div></div><div id="comments-container-57775" class="comments-container"></div><div id="comment-tools-57775" class="comment-tools"></div><div class="clear"></div><div id="comment-57775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57813"></span>

<div id="answer-container-57813" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57813-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried Decode As RTSP? Interleaved data is a feature of RTSP (see <a href="https://tools.ietf.org/html/rfc2326#section-10.12">RFC 2326, Section 10.12</a>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '16, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-57813" class="comments-container"><span id="57851"></span><div id="comment-57851" class="comment"><div id="post-57851-score" class="comment-score"></div><div class="comment-text"><p>Let me try and explain what I mean, Generally in RTSP/RTP streaming the RTSP protocol controls the stream and is usually over TCP, and the actual stream data is sent over UDP on a different port after RTP packetization, so in wireshark one would see a seperate UDP and TCP stream. This UDP stream can then be decoded as RTP using the menu options, this allows wireshark to display the RTP header fields, this helps in analyzing it also we can extract the stream from the RTP packetized stream.</p><p>Now coming to RTSP interleave case, the RTP packets and the RTSP commmands both are sent over the same protocol on the same port, the RTP packets are preceeded by a small header and interleaved with the RTSP commands, what I am looking to get done is to somehow decode these interleaved RTP packets and see the RTP header values and extract the encoded stream.</p><p>I hope this gives some clarity, do let me know if there is a way to do this with wireshark.</p></div><div id="comment-57851-info" class="comment-info"><span class="comment-age">(05 Dec '16, 01:11)</span> streamfanatic</div></div><span id="57852"></span><div id="comment-57852" class="comment"><div id="post-57852-score" class="comment-score"></div><div class="comment-text"><p>This is handled by the RTSP dissector. When it sees a packet beginning with <code>$</code>, it assumes interleaved RTSP/RTP and it will invoke the appropriate subdissector (RTP/RTCP). If a stream is not recognized as RTSP, you can use the Decode As functionality as mentioned in my answer.</p><p>Have you tried this already? It is supposed to be supported by Wireshark.</p></div><div id="comment-57852-info" class="comment-info"><span class="comment-age">(05 Dec '16, 01:20)</span> Lekensteyn</div></div><span id="57853"></span><div id="comment-57853" class="comment"><div id="post-57853-score" class="comment-score"></div><div class="comment-text"><p>I can see the packets as RTSP interleaved in wireshark, but I am looking to find a way to decode the data that follows the header that starts with $, this data is RTP, but I am not sure how to see this as RTP or extract this packet using wireshark.</p></div><div id="comment-57853-info" class="comment-info"><span class="comment-age">(05 Dec '16, 01:38)</span> streamfanatic</div></div><span id="57854"></span><div id="comment-57854" class="comment"><div id="post-57854-score" class="comment-score"></div><div class="comment-text"><p>The following data is supposed to be decoded automatically as RTP. If not, do you have a capture file that demonstrates the issue?</p></div><div id="comment-57854-info" class="comment-info"><span class="comment-age">(05 Dec '16, 02:01)</span> Lekensteyn</div></div><span id="57859"></span><div id="comment-57859" class="comment"><div id="post-57859-score" class="comment-score"></div><div class="comment-text"><p>I have the file, but at work I am restricted, I wont be able to share the capture. The dissector doesnt seem to be working in this case. I am using Version 1.12.4 (v1.12.4-0-gb4861da from master-1.12) dont think the version is the issue though.</p></div><div id="comment-57859-info" class="comment-info"><span class="comment-age">(05 Dec '16, 03:45)</span> streamfanatic</div></div><span id="57860"></span><div id="comment-57860" class="comment not_top_scorer"><div id="post-57860-score" class="comment-score"></div><div class="comment-text"><p>13 0.100180000 10.1.29.34 10.1.29.26 TCP 605 Interleaved channel 0x00, 2007 bytes</p></div><div id="comment-57860-info" class="comment-info"><span class="comment-age">(05 Dec '16, 03:47)</span> streamfanatic</div></div><span id="57862"></span><div id="comment-57862" class="comment not_top_scorer"><div id="post-57862-score" class="comment-score"></div><div class="comment-text"><p>Please try with 2.0 or newer, there was a change (v1.99.8rc0-495-g093aef0) that allows further dissection of data as RTP.</p></div><div id="comment-57862-info" class="comment-info"><span class="comment-age">(05 Dec '16, 04:30)</span> Lekensteyn</div></div><span id="57893"></span><div id="comment-57893" class="comment not_top_scorer"><div id="post-57893-score" class="comment-score"></div><div class="comment-text"><p>tried with Version 2.0.5 (v2.0.5-0-ga3be9c6 from master-2.0) still the sub dissectors for rtp are'nt working.</p></div><div id="comment-57893-info" class="comment-info"><span class="comment-age">(06 Dec '16, 04:48)</span> streamfanatic</div></div><span id="57895"></span><div id="comment-57895" class="comment not_top_scorer"><div id="post-57895-score" class="comment-score"></div><div class="comment-text"><p>Consider filing a bug report at <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a> with a capture that demonstrates the issue, without more details it will be too much effort to find the issue.</p></div><div id="comment-57895-info" class="comment-info"><span class="comment-age">(06 Dec '16, 05:20)</span> Lekensteyn</div></div><span id="57896"></span><div id="comment-57896" class="comment not_top_scorer"><div id="post-57896-score" class="comment-score"></div><div class="comment-text"><p>Thanks Lekensteyn for your time. Appreciate it.</p></div><div id="comment-57896-info" class="comment-info"><span class="comment-age">(06 Dec '16, 05:34)</span> streamfanatic</div></div></div><div id="comment-tools-57813" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-57813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

