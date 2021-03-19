+++
type = "question"
title = "How to dissect TCP stream which emits multiple packets"
description = '''I&#x27;am writing dissector for protocol over TCP stream which can emit more than one packet per real TCP frame. For example lets assume that we have ethernet tunnel over TCP stream, and one TCP frame of length 15000 bytes (assume the capture with TSO on) can contain five or ten embedded ethernet packets...'''
date = "2014-02-13T07:41:00Z"
lastmod = "2014-02-13T15:11:00Z"
weight = 29831
keywords = [ "dissector", "packet-display" ]
aliases = [ "/questions/29831" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to dissect TCP stream which emits multiple packets](/questions/29831/how-to-dissect-tcp-stream-which-emits-multiple-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29831-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'am writing dissector for protocol over TCP stream which can emit more than one packet per real TCP frame. For example lets assume that we have ethernet tunnel over TCP stream, and one TCP frame of length 15000 bytes (assume the capture with TSO on) can contain five or ten embedded ethernet packets. So I can successfully dissect this stream, can write info about each packet to frame tree. But it is not possible to indicate such packet in frame list. And another case when I try to sub dissect emitted packets by ethernet dissector the system goes crazy and breaks TCP reassemble functionality.</p><p>What is a proper way to write such dissector? How can I indicate new frames to frame list? How not to break TCP reassemble functionality when subdissecting nested packets?</p><p>The best approach I have found is to dump the emitted packets to another pcap file on dissection and then load it to wireshark. But this is a hard way.</p></div><div id="question-tags" class="tags-container tags">dissector packet-display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '14, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/3a70b658be4c87ccf1e2699150f580ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RuAnShi&#39;s gravatar image" /><p>RuAnShi<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RuAnShi has no accepted answers">0%</span></p></div></div><div id="comments-container-29831" class="comments-container"></div><div id="comment-tools-29831" class="comment-tools"></div><div class="clear"></div><div id="comment-29831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29849"></span>

<div id="answer-container-29849" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29849-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But it is not possible to indicate such packet in frame list.</p></blockquote><p>That's not supported. At some point in the future we might support having multiple ways of viewing the list of packets, with an option to have the list show all packets at a given layer, so that, while the frame list will always be a list of "frames" as defined by the lowest layer protocol in the capture, you could see, instead, a list of reassembled IP datagrams (with one entry per IP datagram, and with the fragments not shown as individual frames) or a list of XXX-over-TCP packets (with one entry per XXX packet, even if there are multiple XXX packets in one frame or one TCP segment or if an XXX packet requires multiple frames or TCP segments), but that's not available now.</p><blockquote><p>What is a proper way to write such dissector?</p></blockquote><p>How do you determine where an Ethernet packet begins or ends in the TCP byte stream? Do you have a length field before each Ethernet packet? If so, you could use <code>tcp_dissect_pdus()</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '14, 15:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-29849" class="comments-container"><span id="29860"></span><div id="comment-29860" class="comment"><div id="post-29860-score" class="comment-score"></div><div class="comment-text"><blockquote><p>That's not supported. At some point in the future ....</p></blockquote><p>Personally I have waiting for such feature from 1.4 release, when I start to write plugins for wireshark. It is good to see lots of improvements and refactoring in source tree. Hope this great functionality will be implemented at nearest future.</p><blockquote><p>How do you determine where an Ethernet packet begins or ends in the TCP byte stream?</p></blockquote><p>Lets assume there is a length mark. I have not using tcp_dissect_pdus() because it's to old, my dissector is based on "new" stream dissection architecture. Where I can indicate desegment_offset and desegment_len and ask for more data when needed. This totally avoid to be dependent on underlying dissector.</p><p>Related to TCP reassemble bug. It is now clear for me that if I subdissect emmited frames through eth dissector, which than call TCP dissector again. Than after returning from subdissection the packet_info struct totally reflect underlying TCP substream, not the original TCP frame stream, and there is a roots of broken reassemble functionality. I'am not know a proper way how to fix this.</p></div><div id="comment-29860-info" class="comment-info"><span class="comment-age">(14 Feb '14, 01:23)</span> RuAnShi</div></div><span id="29861"></span><div id="comment-29861" class="comment"><div id="post-29861-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I have not using tcp_dissect_pdus() because it's to old, my dissector is based on "new" stream dissection architecture. Where I can indicate desegment_offset and desegment_len and ask for more data when needed.</p></blockquote><p>You have it exactly backwards. The old architecture required every dissector to manage <code>desegment_offset</code> and <code>desegment_len</code> itself. Several dissectors, for protocols with headers that included a length, had duplicate code to do the same thing; that code was extracted into <code>tcp_dissect_pdus()</code> and generalized to have the length of the part containing the length field, and a routine to extract the length from that part, be arguments to <code>tcp_dissect_pdus()</code>.</p></div><div id="comment-29861-info" class="comment-info"><span class="comment-age">(14 Feb '14, 01:31)</span> Guy Harris ♦♦</div></div><span id="29864"></span><div id="comment-29864" class="comment"><div id="post-29864-score" class="comment-score"></div><div class="comment-text"><p>May be this is true for protocols running only atop of TCP, but in general way I wish my dissector to be running at any data stream. So, according to README.dissector 2.7 I should use 2.7.2 method, which allow me to dissect any data stream in general. Otherwise I need to write dissector for each underlying transport. According to desegment_offset and desegment_len, they only used when dissector detect that there more data required to be called once again with enlarged tvb. And of cause the dissector use new_create_dissector_handle with function which return amount of already processed data.</p></div><div id="comment-29864-info" class="comment-info"><span class="comment-age">(14 Feb '14, 03:50)</span> RuAnShi</div></div></div><div id="comment-tools-29849" class="comment-tools"></div><div class="clear"></div><div id="comment-29849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

