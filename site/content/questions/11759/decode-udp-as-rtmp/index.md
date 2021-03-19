+++
type = "question"
title = "Decode UDP as RTMP"
description = '''Hi, I have a network dump with a RTMP stream but it&#x27;s transported over UDP rather then TCP,  so Wireshark seems not to be able to decode the RTMP stream. I&#x27;ve tried also to decode the packages manual,  but there is no option for RTMP when selecting a UDP packet. I&#x27;m using the current stable version ...'''
date = "2012-06-08T04:20:00Z"
lastmod = "2012-06-08T05:37:00Z"
weight = 11759
keywords = [ "decode_as", "udp", "rtmp" ]
aliases = [ "/questions/11759" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode UDP as RTMP](/questions/11759/decode-udp-as-rtmp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11759-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a network dump with a RTMP stream but it's transported over UDP rather then TCP, so Wireshark seems not to be able to decode the RTMP stream. I've tried also to decode the packages manual, but there is no option for RTMP when selecting a UDP packet.</p><p>I'm using the current stable version 1.6.8 and I tried the 1.8.0rc1 as well.</p><p>Is there any possibility to decode an RTMP stream transported over UDP with Wireshark?</p><p><strong>UDPATE:</strong></p><p>Maybe it's more like Secure Real-Time Media Flow Protocol (RTMFP).</p><p>Sorry, I can't post a capture but here is a screenshot from the connection setup I think: <img src="https://osqa-ask.wireshark.org/upfiles/wirehark-udp-rtmp_1.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">decode_as udp rtmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '12, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/7addbe79a0df4fa1521ef86fe4a41b42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rick28&#39;s gravatar image" /><p>rick28<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rick28 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jun '12, 10:34</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11759" class="comments-container"></div><div id="comment-tools-11759" class="comment-tools"></div><div class="clear"></div><div id="comment-11759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11764"></span>

<div id="answer-container-11764" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11764-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you talk about the Adobe protocol (Real Time Messaging Protocol - RTMP), that is only defined for TCP. The Wireshark RTMPT dissector (packet-rtmpt.c) can only dissect RTMP over TCP or over HTTP.</p><p>If you have RTMP encapsulated in UDP, that would be kind of strange, as nobody should be doing that. If you want to dissect RTMP over UDP, you'll have to enhance the RTMPT dissector, or write your own dissector in Lua: <code>http://www.wireshark.org/docs/wsug_html_chunked/wsluarm.html</code><br />
</p><p>How comes RTMP is encapsulated in UDP? Can you post a sample capture?</p><p><strong>UPDATE</strong>:</p><blockquote><p>Maybe it's more like Secure Real-Time Media Flow Protocol (RTMFP).</p></blockquote><p>That sounds reasonable, at least the port matches.</p><p>Unfortunately there is no RTMFP dissector available in wireshark.</p><p>Furthermore, there seems to be no public RTMFP spec available, so writing a fully compliant dissector might be difficult. The protocol supports encryption, which might pose another problem.</p><blockquote><p><code>http://p2p-sip.blogspot.de/2011/12/understanding-rtmfp-handshake.html</code></p></blockquote><p>However, there is an open source project called OpenRTMFP</p><blockquote><p><code>https://github.com/OpenRTMFP</code></p></blockquote><p>Based on that code, it might be possible to develop a dissector (encryption would still be a problem).<br />
</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '12, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jun '12, 10:58</p></div></div><div id="comments-container-11764" class="comments-container"></div><div id="comment-tools-11764" class="comment-tools"></div><div class="clear"></div><div id="comment-11764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

