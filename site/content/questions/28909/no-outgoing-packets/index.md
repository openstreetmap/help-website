+++
type = "question"
title = "No outgoing packets"
description = '''Hello, I&#x27;m currently facing issue when tryin to capture network communications from Win 7 X64 stations. When I start a capture from a client, in the capture I most of the time I don&#x27;t see packets sent by the client. Strangely it&#x27;s quite random. Sometines I see packets from the client at the begining...'''
date = "2014-01-15T06:40:00Z"
lastmod = "2014-01-15T07:03:00Z"
weight = 28909
keywords = [ "symantec", "offload", "outgoing", "outbound", "chimney" ]
aliases = [ "/questions/28909" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No outgoing packets](/questions/28909/no-outgoing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28909-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm currently facing issue when tryin to capture network communications from Win 7 X64 stations. <strong>When I start a capture from a client, in the capture I most of the time I don't see packets sent by the client.</strong></p><p>Strangely it's quite random. Sometines I see packets from the client at the begining of the communication but after a short while I see only packets from server.</p><p>Do you have any idea causing this issue. This is blocking my network analyse so I need to solve it.</p><p>Is this related to offload / chimney behavior?</p><p>Thanks for your help</p></div><div id="question-tags" class="tags-container tags">symantec offload outgoing outbound chimney</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '14, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/25fcd4b6692b20e9189d8f0b52f1663d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="any-one&#39;s gravatar image" /><p>any-one<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="any-one has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Feb '14, 05:55</p></div></div><div id="comments-container-28909" class="comments-container"><span id="28911"></span><div id="comment-28911" class="comment"><div id="post-28911-score" class="comment-score"></div><div class="comment-text"><p>Try searching the site for "outgoing packets". This comes up a lot and is usually AV or VPN software or TCP offloading.</p></div><div id="comment-28911-info" class="comment-info"><span class="comment-age">(15 Jan '14, 07:01)</span> grahamb ♦</div></div><span id="28924"></span><div id="comment-28924" class="comment"><div id="post-28924-score" class="comment-score"></div><div class="comment-text"><p>I already tried to deactivate TCP Offload without success :(</p><p>netsh int tcp set global chimney=disabled</p><p>I checked the NIC settings, there's no specifig setting about offload. So I don't really undertand the source of the issue</p></div><div id="comment-28924-info" class="comment-info"><span class="comment-age">(15 Jan '14, 09:11)</span> any-one</div></div></div><div id="comment-tools-28909" class="comment-tools"></div><div class="clear"></div><div id="comment-28909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28914"></span>

<div id="answer-container-28914" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28914-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Sometines I <strong>see packets</strong> from the client <strong>at the begining of the communication</strong> but after a short while I see only packets from server.</p></blockquote><p>That's usually a sign for TCP offloading into the NIC driver. You will see the 3-way handshake and then nothing, as the rest of the communication is handled by the NIC itself and that traffic is invisible to Wireshark (due to the way the capturing library inserts itself into the kernel).</p><p>BTW: Apparently you already knew that, as you chose the right tags (offload and chimney) ;-))</p><p>There are other reasons, like 'strange network drivers', security software, etc.</p><blockquote><p><a href="http://ask.wireshark.org/questions/17638/no-outgoing-packets">http://ask.wireshark.org/questions/17638/no-outgoing-packets</a><br />
<a href="http://ask.wireshark.org/questions/28762/outbound-packets-not-captured">http://ask.wireshark.org/questions/28762/outbound-packets-not-captured</a><br />
</p></blockquote><p>See also other, similar, questions with the tags 'outgoing' or 'outbound'</p><blockquote><p><a href="http://ask.wireshark.org/tags/outgoing/">http://ask.wireshark.org/tags/outgoing/</a><br />
<a href="http://ask.wireshark.org/tags/outbound/">http://ask.wireshark.org/tags/outbound/</a></p></blockquote><p>BTW: I just updated the tags of some of those questions, as this specific problem arised a few times lately.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '14, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jan '14, 07:17</p></div></div><div id="comments-container-28914" class="comments-container"><span id="28922"></span><div id="comment-28922" class="comment"><div id="post-28922-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply.</p><p>I'm facing this issue even when I try to PING a server. I see only echo reply packets. no echo request. even using Wireless network</p></div><div id="comment-28922-info" class="comment-info"><span class="comment-age">(15 Jan '14, 08:22)</span> any-one</div></div><span id="28923"></span><div id="comment-28923" class="comment"><div id="post-28923-score" class="comment-score"></div><div class="comment-text"><p>Did you look at the 'DNE problem' (actually 'DNE LightWeight Filter' as part of a VPN client installed on the system)?</p><blockquote><p><a href="http://ask.wireshark.org/questions/28762/outbound-packets-not-captured">http://ask.wireshark.org/questions/28762/outbound-packets-not-captured</a></p></blockquote></div><div id="comment-28923-info" class="comment-info"><span class="comment-age">(15 Jan '14, 08:32)</span> Kurt Knochner ♦</div></div><span id="28925"></span><div id="comment-28925" class="comment"><div id="post-28925-score" class="comment-score"></div><div class="comment-text"><p>I'm pretty sure there's no VPN client installed on stations. I can duble check.</p></div><div id="comment-28925-info" class="comment-info"><span class="comment-age">(15 Jan '14, 09:13)</span> any-one</div></div><span id="28927"></span><div id="comment-28927" class="comment"><div id="post-28927-score" class="comment-score"></div><div class="comment-text"><p>Any other security software, like Endpoint protection, AV and the like?</p></div><div id="comment-28927-info" class="comment-info"><span class="comment-age">(15 Jan '14, 09:54)</span> Kurt Knochner ♦</div></div><span id="28950"></span><div id="comment-28950" class="comment"><div id="post-28950-score" class="comment-score"></div><div class="comment-text"><p>Symantec Endpoint Protection is installed on our clients. I'll request the right to disable it. I'll let you know.</p></div><div id="comment-28950-info" class="comment-info"><span class="comment-age">(16 Jan '14, 00:35)</span> any-one</div></div><span id="28951"></span><div id="comment-28951" class="comment not_top_scorer"><div id="post-28951-score" class="comment-score"></div><div class="comment-text"><p>O.K. that one is known to cause such an effect.</p></div><div id="comment-28951-info" class="comment-info"><span class="comment-age">(16 Jan '14, 00:47)</span> Kurt Knochner ♦</div></div><span id="29625"></span><div id="comment-29625" class="comment not_top_scorer"><div id="post-29625-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>I can confirm. I am now able to disable Symantec Endpoint Protect (SEP)and now I can see all packets in Wireshark !</p></div><div id="comment-29625-info" class="comment-info"><span class="comment-age">(10 Feb '14, 05:53)</span> any-one</div></div><span id="29630"></span><div id="comment-29630" class="comment not_top_scorer"><div id="post-29630-score" class="comment-score"></div><div class="comment-text"><p>Good!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-29630-info" class="comment-info"><span class="comment-age">(10 Feb '14, 06:32)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28914" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-28914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

