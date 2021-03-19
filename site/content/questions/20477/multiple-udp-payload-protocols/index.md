+++
type = "question"
title = "Multiple UDP Payload Protocols"
description = '''I have a UDP payload dissector (1) I&#x27;ve developed that works just fine. Occasionally, there will be data that is not part of dissector 1 and is a different protocol that was attached to the same UDP payload. I&#x27;ve written another dissector for type 2. Is there a way for the 2nd dissector to automatic...'''
date = "2013-04-16T12:40:00Z"
lastmod = "2013-04-16T15:31:00Z"
weight = 20477
keywords = [ "udp", "protocol", "payload" ]
aliases = [ "/questions/20477" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple UDP Payload Protocols](/questions/20477/multiple-udp-payload-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20477-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a UDP payload dissector (1) I've developed that works just fine. Occasionally, there will be data that is not part of dissector 1 and is a different protocol that was attached to the same UDP payload.</p><p>I've written another dissector for type 2.</p><p>Is there a way for the 2nd dissector to automatically dissect the remaining bytes? Dissector 1 returns the number of bytes it actually used and I was hoping wireshark would try other protocols on the remaining bytes.</p><p>I could specifically call dissector 2 from 1, but I don't really want to do that. There could be many other protocols and they could be in different orders.</p><p>dissector_next doesn't really exist, but that's the functionality I'm looking for. I dissect the first protocol and hand off the remaining bytes to whatever protocol that may apply.</p><p>EDIT: Words.</p></div><div id="question-tags" class="tags-container tags">udp protocol payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '13, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/0fe43e124d583a2fd5d3847eb8ecdff4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dlovelace&#39;s gravatar image" /><p>dlovelace<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dlovelace has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Apr '13, 12:43</p></div></div><div id="comments-container-20477" class="comments-container"></div><div id="comment-tools-20477" class="comment-tools"></div><div class="clear"></div><div id="comment-20477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20483"></span>

<div id="answer-container-20483" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20483-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand you correctly, you have a protocol that is identified by wireshark by it's UDP port number (or through heuristics) and the first part of the UDP payload is always your protocol (protocol 1 in your question). After the dissector for protocol 1 has finished dissecting it's bytes, there is still bytes left in the UDP payload and nothing in the protocol 1 headers tell you which protocol the remaining bytes belong to. So:</p><blockquote><p>There could be many other protocols and they could be in different orders.</p></blockquote><p>And how would you recognize which bytes belong to which protocol? Is there a header with certain values for certain protocols? Or are there some heuristics that can determine which protocol is used for (part of) the remaining bytes?</p><p>If there is no value in either protocol 1 or the first part of the remaining bytes pointing to a distinct protocol, then you could build a heuristic protocol table and let all the possible protocol dissectors for the remaining bytes register to that table. Each dissector determines whether the next bytes are indeed valid bytes for the protocol. If not, it returns 0, if so, it returns the number of bytes it recognized and dissected. The protocol 1 dissector will have to loop through the remaining bytes this way until all remaining bytes have been dissecter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '13, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20483" class="comments-container"><span id="20491"></span><div id="comment-20491" class="comment"><div id="post-20491-score" class="comment-score"></div><div class="comment-text"><p>Protocol 1 is heuristic as is Protocol 2. Both of these protocols are ASTERIX-like and use a header byte/length. Protocol 1 decodes all the UDP payload bytes that are its type and finishes. There may or may not be leftover bytes. Occasionally there are 2 instances of Protocol 1 and then leftover bytes that are Protocol 2. It would be far easier if the spec said just 1 Protocol per packet, but alas, no.</p><p>If there are leftover bytes, I was curious if Protocol 1 can 'hand over' the extra bytes to Wireshark to see if any other protocol applies. The heuristic code in Protocol 2 would sense that it fits and decode the remaining bytes. I don't really want to write code in Protocol 1 to determine what the remaining bytes are and call those sub dissector manually. They are separate Protocols and I don't really want to combine them in any way. If there's an automatic way of doing it, that would be swell.</p><p>That probably explains it a bit better.</p></div><div id="comment-20491-info" class="comment-info"><span class="comment-age">(16 Apr '13, 16:09)</span> dlovelace</div></div><span id="20492"></span><div id="comment-20492" class="comment"><div id="post-20492-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Both of these protocols are ASTERIX-like</p></blockquote><p>Maybe the code of the asterix plugin can help you. See the links in my answer to the following question:</p><blockquote><p><code>http://ask.wireshark.org/questions/20109/problem-with-tcpip-decoding</code></p></blockquote></div><div id="comment-20492-info" class="comment-info"><span class="comment-age">(16 Apr '13, 16:14)</span> Kurt Knochner ♦</div></div><span id="20514"></span><div id="comment-20514" class="comment"><div id="post-20514-score" class="comment-score"></div><div class="comment-text"><p>I'll look at it further, but it is in french. Haha.</p><p>The one thing the Asterix dissector does itself is that it will handle all the Asterix protocols. Mine are technically different dissectors so I can't handle Protocol 2 in the Protocol 1 code.</p></div><div id="comment-20514-info" class="comment-info"><span class="comment-age">(17 Apr '13, 04:58)</span> dlovelace</div></div></div><div id="comment-tools-20483" class="comment-tools"></div><div class="clear"></div><div id="comment-20483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

