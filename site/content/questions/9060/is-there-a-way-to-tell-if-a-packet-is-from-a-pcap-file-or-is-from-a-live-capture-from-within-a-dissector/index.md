+++
type = "question"
title = "Is there a way to tell if a packet is from a pcap file, or is from a live capture from within a dissector?"
description = '''Within a dissector, is it possible to know if the tvbuff_t is populated from a file or from a live capture?'''
date = "2012-02-16T06:42:00Z"
lastmod = "2012-02-16T06:51:00Z"
weight = 9060
keywords = [ "tvbuff_t", "capture", "dissector", "development" ]
aliases = [ "/questions/9060" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a way to tell if a packet is from a pcap file, or is from a live capture from within a dissector?](/questions/9060/is-there-a-way-to-tell-if-a-packet-is-from-a-pcap-file-or-is-from-a-live-capture-from-within-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9060-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Within a dissector, is it possible to know if the <code>tvbuff_t</code> is populated from a file or from a live capture?</p></div><div id="question-tags" class="tags-container tags">tvbuff_t capture dissector development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '12, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/9da2e9fc67b04d5827f0413c73612df3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wintermut3&#39;s gravatar image" /><p>wintermut3<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wintermut3 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '12, 07:09</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9060" class="comments-container"><span id="9063"></span><div id="comment-9063" class="comment"><div id="post-9063-score" class="comment-score">1</div><div class="comment-text"><p>Why do you need to know? The protocol understood by your dissector shouldn't care how the bits get to it --whether it be from a pcap file, a live capture, the fuzz-tester, or somebody's fancy random number generator usb dongle that they've hooked up to Wireshark. The source of data (within Wireshark) should have no impact on how it is decoded.<br />
When the data reaches your dissector, it is totally frozen, and could have come from anywhere.</p></div><div id="comment-9063-info" class="comment-info"><span class="comment-age">(16 Feb '12, 07:07)</span> multipleinte...</div></div><span id="9064"></span><div id="comment-9064" class="comment"><div id="post-9064-score" class="comment-score"></div><div class="comment-text"><p>a requirement--I am having to detect and flag PTP V2 sequence ids that or out of order of packets (based on capture time that are of the same message_id. since the order the dissector receives the packets seems to vary (especially in the case of a pcap file) I know this is outside of the scope and intent of a dissector, but I need to either find a way to do it, or explain to them why this can't be done. I need to know the origin so I can decide to track and sort the order--something I don't think I need to do, or want to do in the case of a stream--the stream should be in the right order, yes?</p></div><div id="comment-9064-info" class="comment-info"><span class="comment-age">(16 Feb '12, 07:21)</span> wintermut3</div></div></div><div id="comment-tools-9060" class="comment-tools"></div><div class="clear"></div><div id="comment-9060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9061"></span>

<div id="answer-container-9061" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9061-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the dissector point of view there is no difference, so no, it does not know.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '12, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></p></div></div><div id="comments-container-9061" class="comments-container"><span id="9062"></span><div id="comment-9062" class="comment"><div id="post-9062-score" class="comment-score"></div><div class="comment-text"><p>That is what I thought, so if I needed to know that, I would have to set a flag somewhere outside of the dissector? is that reliable? or even possible?</p></div><div id="comment-9062-info" class="comment-info"><span class="comment-age">(16 Feb '12, 06:57)</span> wintermut3</div></div><span id="9070"></span><div id="comment-9070" class="comment"><div id="post-9070-score" class="comment-score">1</div><div class="comment-text"><p>I kinda doubt you can do it at all, since Wireshark does not capture frames. Instead, it runs an additional executable called "dumpcap" that writes the incoming frames to file, which is then loaded and decoded "on the fly" by Wireshark. So basically Wireshark <em>always</em> reads from pcap, never from the NIC.</p></div><div id="comment-9070-info" class="comment-info"><span class="comment-age">(16 Feb '12, 09:42)</span> Jasper ♦♦</div></div><span id="9079"></span><div id="comment-9079" class="comment"><div id="post-9079-score" class="comment-score"></div><div class="comment-text"><p>Ah, that makes sense, so those "on the fly" frames very well may not be sent to the dissector in any standard order?... which is the behavior I have seen from directly reading a pcap file as well--understandable behavior by Wireshark as a dissector is not meant anything other than decoding--now if I can I can just get "Them" to understand that...</p></div><div id="comment-9079-info" class="comment-info"><span class="comment-age">(16 Feb '12, 20:01)</span> wintermut3</div></div><span id="9086"></span><div id="comment-9086" class="comment"><div id="post-9086-score" class="comment-score"></div><div class="comment-text"><p>The order in which packets appear in a file captured by <em>any</em> program using libpcap/WinPcap, whether it's dumpcap (whether run by the user or by Wireshark or TShark) or tcpdump or..., is the order in which they're delivered to libpcap/WinPcap by the OS. This is not guaranteed to be the order in which they arrive on the machine; the OS might deliver them out of order.</p><p>Precision Time Protocol packets are sent over UDP, which makes no guarantee of delivery at all, much less any guarantee of in-order delivery.</p></div><div id="comment-9086-info" class="comment-info"><span class="comment-age">(17 Feb '12, 02:13)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-9061" class="comment-tools"></div><div class="clear"></div><div id="comment-9061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

