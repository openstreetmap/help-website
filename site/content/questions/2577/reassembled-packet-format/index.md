+++
type = "question"
title = "Reassembled Packet Format"
description = '''The proto I&#x27;m decoding can be over UDP or TCP, and multiple msgs can be in a given UDP/TCP packet.  I&#x27;m able to detect when my msg overflows into the next packet, and I can successfully manipulate the pinfo.desegment_len and pinfo.desegment_offset vars to have the decoding of the following packet st...'''
date = "2011-02-27T13:00:00Z"
lastmod = "2011-03-01T05:14:00Z"
weight = 2577
keywords = [ "reassembly", "lua" ]
aliases = [ "/questions/2577" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reassembled Packet Format](/questions/2577/reassembled-packet-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2577-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The proto I'm decoding can be over UDP or TCP, and multiple msgs can be in a given UDP/TCP packet.<br />
</p><p>I'm able to detect when my msg overflows into the next packet, and I can successfully manipulate the pinfo.desegment_len and pinfo.desegment_offset vars to have the decoding of the following packet start in the correct place. However, the dissector for the last msg (the fragmented one at the end of the packet) doesn't get called since I return out when I don't have enough bytes for a complete msg. Is it possible to 'bring' the remaining bytes from the next packet in and continue? Or should the beginning of the next packet try to reference the previous packet and start from there? I can see the decoded bytes are correctly appended in the reassembled TCP segments tree of the second packet. I feel like I am super close, but can't seal the deal. :(</p><p>As a side question, how does one generally determine the desegment_offset? I have a hard-coded value of 66 set to account for the ip/tcp header info in the frame. However, that wouldn't work so well if this was a UDP packet. Is there a method to get the beginning of 'user data'?<br />
</p><p>I'm doing this in Lua.</p></div><div id="question-tags" class="tags-container tags">reassembly lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '11, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/61dd0a62d62ba6e987ac1f93ad269ebe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TalleyHo&#39;s gravatar image" /><p>TalleyHo<br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TalleyHo has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-2577" class="comments-container"><span id="2578"></span><div id="comment-2578" class="comment"><div id="post-2578-score" class="comment-score"></div><div class="comment-text"><p>For UDP:</p><p>Can a message for your protocol cross a UDP packet boundary, or is all of a message contained within one UDP packet?</p><p>For TCP:</p><p>What determines the message boundaries in your protocol? For example, do messages have a message length field in the beginning of the packet?</p></div><div id="comment-2578-info" class="comment-info"><span class="comment-age">(27 Feb '11, 23:14)</span> Guy Harris ♦♦</div></div><span id="2582"></span><div id="comment-2582" class="comment"><div id="post-2582-score" class="comment-score"></div><div class="comment-text"><p>Guy, The message length is determined by the 2nd/3rd bytes of the message. So I have [id][len][data][checksum] ...</p><p>In the TCP trace that spans I have...</p><p>[id][len][data][checksum] [id][len][data][checksum] ... [id][len][da ...packet break... ta][checksum]</p><p>In the decode tree, all of the complete msgs are present in the first packet. The split packet is not decoded. It's like I need a higher layer dissector to accumulate the packet.</p><p>I've been told its possible that UDP can span packets, although I've yet to see it. All our msgs are relatively short, multiple msgs/packet are likely.</p></div><div id="comment-2582-info" class="comment-info"><span class="comment-age">(28 Feb '11, 06:26)</span> TalleyHo</div></div></div><div id="comment-tools-2577" class="comment-tools"></div><div class="clear"></div><div id="comment-2577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2602"></span>

<div id="answer-container-2602" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2602-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Given that the messages in your protocol have a length field early in the message, the best way to handle your protocol over TCP is to have its dissector call tcp_dissect_pdus(); let tcp_dissect_pdus() manipulate desegment_len and desegment_offset for you. See the doc/README.developer file (or, if you're using Windows, docREADME.developer :-)) for details on using tcp_dissect_pdus(). tcp_dissect_pdus() also handles the case of multiple messages per TCP segment for you, so you don't have to do that, either.</p><p>I suspect your protocol does not support messages that cross UDP packet boundaries, as UDP, unlike TCP, makes no guarantee of in-order delivery of packets, so you would need to have your own fragment sequence numbers (the "id" field is per-message, not per-fragment, so it won't suffice). When dissecting your messages over UDP, the dissector would have to handle the "multiple messages per UDP datagram" case itself.</p><p>For this, you would probably want a routine to dissect a single message, pass that as the "dissect a PDU" routine to tcp_dissect_pdus() in the dissector for your-protocol-over-TCP, and call it in the loop in the dissector for your-protocol-over-UDP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '11, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2602" class="comments-container"><span id="2605"></span><div id="comment-2605" class="comment"><div id="post-2605-score" class="comment-score"></div><div class="comment-text"><p>Inside the data is a msgId header, so I can verify order of delivery. I've not seen any reference to the tcp_dissect_pdus() functions in the Lua API? Are those also available from Lua? It was my impression that was only from C. For the cost of easy portability, I can live w/ a few boundary issues like this one. But your answer makes sense to what I was thinking. I guess reading it a second time (also from the Readme) it sunk in further.</p></div><div id="comment-2605-info" class="comment-info"><span class="comment-age">(01 Mar '11, 06:04)</span> TalleyHo</div></div><span id="2622"></span><div id="comment-2622" class="comment"><div id="post-2622-score" class="comment-score"></div><div class="comment-text"><p>You can verify order of delivery of messages, but not of parts of messages. If a message is split across UDP packet boundaries into parts that aren't separate messages, you won't even be able to recognize anything other than the first part as being a part of a message, much less verify order of delivery. (I'd give an example, but that'd take more than the limit on the number of characters in a comment; if you want to discuss that further, ask about it on the wireshark-dev mailing list.)</p></div><div id="comment-2622-info" class="comment-info"><span class="comment-age">(01 Mar '11, 14:21)</span> Guy Harris ♦♦</div></div><span id="2623"></span><div id="comment-2623" class="comment"><div id="post-2623-score" class="comment-score"></div><div class="comment-text"><p>I don't see any reference to tcp_dissect_pdus() in the source files in the epan/wslua directory, so it's probably not available from Lua. File a bug to request that. To do what you want to do, you would, for now, be best advised to duplicate in your Lua dissector all the stuff that tcp_dissect_pdus() does.</p></div><div id="comment-2623-info" class="comment-info"><span class="comment-age">(01 Mar '11, 14:24)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-2602" class="comment-tools"></div><div class="clear"></div><div id="comment-2602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

