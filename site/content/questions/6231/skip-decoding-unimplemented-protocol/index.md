+++
type = "question"
title = "Skip decoding unimplemented protocol?"
description = '''Hi, Is there a way to skip a certain number of bytes in the packet while  decoding protocols in a packet using Wireshark? In other words, if  Wireshark doesn&#x27;t support a particular protocol (at the moment), is it  possible to &#x27;skip&#x27; that protocol but be able to decode the next? As an example conside...'''
date = "2011-09-09T08:18:00Z"
lastmod = "2011-11-06T07:49:00Z"
weight = 6231
keywords = [ "decode_as" ]
aliases = [ "/questions/6231" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Skip decoding unimplemented protocol?](/questions/6231/skip-decoding-unimplemented-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6231-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is there a way to skip a certain number of bytes in the packet while decoding protocols in a packet using Wireshark? In other words, if Wireshark doesn't support a particular protocol (at the moment), is it possible to 'skip' that protocol but be able to decode the next?</p><p>As an example consider a VxLAN encapsulated packet. As per the IETF draft, a VxLAN packet contains the following headers in the given order -</p><p>Outer Ethernet Header (including an optional VLAN tag)<br />
Outer IP Header<br />
Outer UDP Header<br />
VxLAN Header<br />
Inner Ethernet Header (including an optional VLAN tag)<br />
Original Ethernet Payload (excluding the original Ethernet FCS)<br />
FCS for Outer Ethernet Frame</p><p>The VxLAN header is a fixed 8 byte header - what I'd like is for wireshark to skip the 8 bytes (since VxLAN was just announced and Wireshark doesn't support it yet) but continue to decode the Inner Ethernet Header and beyond.</p><p>Basically, give a parameter to "Decode As" to skip a certain number of bytes?</p><p><em>For some reason my post to the wireshark-users mailing list is being discarded although I'm a member of the list - therefore am asking here</em></p></div><div id="question-tags" class="tags-container tags">decode_as</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '11, 08:18</strong></p><img src="https://secure.gravatar.com/avatar/5a45b6d9137f7631da29560ece6f02ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pstavirs&#39;s gravatar image" /><p>pstavirs<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pstavirs has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-6231" class="comments-container"></div><div id="comment-tools-6231" class="comment-tools"></div><div class="clear"></div><div id="comment-6231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6235"></span>

<div id="answer-container-6235" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6235-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may be able to get around this programming your unsupported protocol in Lua.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '11, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-6235" class="comments-container"></div><div id="comment-tools-6235" class="comment-tools"></div><div class="clear"></div><div id="comment-6235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7253"></span>

<div id="answer-container-7253" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7253-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Following Jaap's pointer, I finally got some time to play around with Lua. The results of this tinkering is a VxLAN dissector in Lua - see <a href="http://www.lovemytool.com/blog/2011/11/analyzing-vxlan-packets-using-wireshark-by-srivats-p.html" title="VxLAN Dissector In Lua">http://www.lovemytool.com/blog/2011/11/analyzing-vxlan-packets-using-wireshark-by-srivats-p.html</a> for the code and accompanying explanation of the code.</p><p>Thanks Jaap!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '11, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/5a45b6d9137f7631da29560ece6f02ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pstavirs&#39;s gravatar image" /><p>pstavirs<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pstavirs has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-7253" class="comments-container"><span id="7283"></span><div id="comment-7283" class="comment"><div id="post-7283-score" class="comment-score"></div><div class="comment-text"><p>It's not so difficult to do in C either, a VxLAN dissector Committed revision 39760.</p></div><div id="comment-7283-info" class="comment-info"><span class="comment-age">(08 Nov '11, 09:41)</span> Anders ♦</div></div></div><div id="comment-tools-7253" class="comment-tools"></div><div class="clear"></div><div id="comment-7253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

