+++
type = "question"
title = "CAPWAP Malformed packets"
description = '''Hi, Recently I found on my company network that CAPWAP protocol packets sent from different access points (registered in a Cisco Wireless Controller) to the address 255.255.255.255 were decoded like Malformed Packets. After &quot;googling it&quot; I found several forums where other engineers found that was du...'''
date = "2015-05-02T03:54:00Z"
lastmod = "2015-05-02T14:20:00Z"
weight = 42019
keywords = [ "capwap", "wlc", "malformedpacket" ]
aliases = [ "/questions/42019" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [CAPWAP Malformed packets](/questions/42019/capwap-malformed-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42019-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Recently I found on my company network that CAPWAP protocol packets sent from different access points (registered in a Cisco Wireless Controller) to the address 255.255.255.255 were decoded like Malformed Packets. After "googling it" I found several forums where other engineers found that was due to an (by default) unchecked option called "Cisco Wireless Controller Support" in the menu Edit/preferences/protocols/CAPWAP. It was true, when I enabled this options Wireshark didn't show the error "Malformed Packets" any more.</p><p>My question is: why are these packets considered malformed if this check is not enabled since they are necessary packets for the WLC access points functioning?</p><p>Some forums consider this like a bug but, from my point of view is not a bug because the option Cisco Wireless Controller Support decodes well packets. The point is that I don´t understand the necessity of this option, I´m assuming that has some sense the possibility of check/uncheck the option. If I´m right I would like to know why is implemented on this way.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">capwap wlc malformedpacket</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '15, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/1dcc4b16407e544312bbeb965544e7cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Francisco%20Torrecillas&#39;s gravatar image" /><p>Francisco To...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Francisco Torrecillas has no accepted answers">0%</span></p></div></div><div id="comments-container-42019" class="comments-container"></div><div id="comment-tools-42019" class="comment-tools"></div><div class="clear"></div><div id="comment-42019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42023"></span>

<div id="answer-container-42023" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42023-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Because in your case the packets conform to a Draft-8 version of the protocol what was to become CAPWAP. With equipment that is CAPWAP compliant these specific packets look different. Unfortunately it's not possible to know automagically which version of the CAPWAP protocol these packets adhere to ("Is it really Draft-8 compliant or is it an error?") so you have to decide, though a preference.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '15, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-42023" class="comments-container"><span id="42052"></span><div id="comment-42052" class="comment"><div id="post-42052-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your comments, Jaap. The problem was affecting only to CAPWAP Control Messages (Type: Primary Discovery Request). After reviewing RFC 5415 (CAPWAP Protocol Specification) I saw that this protocol status is still a proposed standard however, if, I'm not misunderstanding it, Cisco implementation is not being unconditionally compliant with the "proposed standard" and that´s why Wireshark adds the option "Cisco Wireless Controller Support". Considering the message type of these packets I think that should´t depend on protocol version implemented, a primary discovery request format should be always the same irrespective of the access controller type. As additional note, one of RFC 5415 authors (P. Calhoun) worked for Cisco when proposed standard was created.</p></div><div id="comment-42052-info" class="comment-info"><span class="comment-age">(04 May '15, 03:06)</span> Francisco To...</div></div><span id="42054"></span><div id="comment-42054" class="comment"><div id="post-42054-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-42054-info" class="comment-info"><span class="comment-age">(04 May '15, 04:54)</span> Jaap ♦</div></div><span id="42055"></span><div id="comment-42055" class="comment"><div id="post-42055-score" class="comment-score"></div><div class="comment-text"><p>Well, that's a welcome to the ugly world of standardization. When you develop a technology/protocol and work it into a standard two things can happen. Either you get incompatible changes with respect to the pre-standard equipment you put out in the market, or you get standards with numerous optional features. The latter opens the gate to all kinds of standard compliant but incompatible equipment. When that happens they start putting together so called profiles, to define proper selections of optional features to implement for a specific application. Try to figure that one out is a bit of a nightmare.</p></div><div id="comment-42055-info" class="comment-info"><span class="comment-age">(04 May '15, 04:59)</span> Jaap ♦</div></div></div><div id="comment-tools-42023" class="comment-tools"></div><div class="clear"></div><div id="comment-42023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

