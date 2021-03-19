+++
type = "question"
title = "a lot of retransmits, but no drops or significant delays"
description = '''We are troubleshooting connectivity issues across a layer two connection between sites across a provider. Users experience application hangs and timeouts when passing across this specific link.  Packet captures do NOT show packet DROPS, but show RE-TRANSMITS. It is the strangest thing.  Complete det...'''
date = "2012-04-16T14:19:00Z"
lastmod = "2012-04-19T11:52:00Z"
weight = 10200
keywords = [ "ack", "retransmission" ]
aliases = [ "/questions/10200" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [a lot of retransmits, but no drops or significant delays](/questions/10200/a-lot-of-retransmits-but-no-drops-or-significant-delays)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10200-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are troubleshooting connectivity issues across a layer two connection between sites across a provider. Users experience application hangs and timeouts when passing across this specific link.</p><p>Packet captures do NOT show packet DROPS, but show RE-TRANSMITS. It is the strangest thing.</p><p>Complete details <a href="http://www.networking-forum.com/viewtopic.php?f=33&amp;t=30281">here</a>, I would have put the pcaps here, but i couldn't figure out how to attach.</p><p>Any assistance in explaining this behavior is appreciated.</p><p>Thanks, Tarek</p></div><div id="question-tags" class="tags-container tags">ack retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '12, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/6c866bbe972fd157c8e160c9e16c5e31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tarjall&#39;s gravatar image" /><p>tarjall<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tarjall has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Apr '12, 17:47</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-10200" class="comments-container"></div><div id="comment-tools-10200" class="comment-tools"></div><div class="clear"></div><div id="comment-10200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10203"></span>

<div id="answer-container-10203" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10203-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had only a few minutes to look at your trace, but what happens in your trace is something not so uncommon (I looked at the server trace).</p><p>Frame 72 is a real retransmission (not a duplicate, since the IP Identification changes), so question is, why does the server retransmit when there is no loss. The answer is: a timer on the server ran out, because there was no acknowledge coming back in time. When you look at the timings you'll see that the client usually acknowledges incoming packets within a few milliseconds, but frame 71 isn't acknowledged before the server becomes impatient and retransmits.</p><p>This happens again, on a larger scale, in between frames 88 and 93. Frame 90 even contains some sort of a complaint by the client that it got data twice: if you look at the TCP options you'll see a SACK range that is within the full acknowledged range (6061-6273, which is included in the ACK on 6273). That way the client tries to tell the server that it got a needless retransmission.</p><p>I have no idea why the client has troubles acknowledging data in time; this is something the trace doesn't tell. It just looks like the network is working fine, but somehow client and server stacks seem to ignore each others packets sometimes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '12, 17:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Apr '12, 04:45</p></div></div><div id="comments-container-10203" class="comments-container"></div><div id="comment-tools-10203" class="comment-tools"></div><div class="clear"></div><div id="comment-10203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10297"></span>

<div id="answer-container-10297" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10297-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Retransmissions, missing acknowledgements and other problems without explicit dropped packets can be a symptom of a mismatched duplex setting on a link somewhere in the transmission path. As long as Wireshark itself is listening on a properly configured full duplex or half-duplex link, you might not see dropped or corrupted packets.</p><p>If the server packet is being blocked this would not explain the client complaining about getting a packet twice. That could happen if it was the initial ACK from the client that is sometimes being blocked before it reaches Wireshark. That is possible if the client-to-server path is being blocked by another packet en route from the server to the client.</p><p>The cause would be that the client side thinks the link is full duplex while the server side thinks it is half-duplex. That problem link would be somewhere between Wireshark and the client.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-10297" class="comments-container"><span id="10411"></span><div id="comment-10411" class="comment"><div id="post-10411-score" class="comment-score"></div><div class="comment-text"><p>I've made some progress on this but still need help. Apparently specific packets are being modified after leaving one end of this connection, and before arriving at the other end.</p><p>If you look at packet 88 on the outlookclient cap (receiving end), look at the bottom of the hex view and you see 08 bf e0, look at the same packet on the 3750 capture (sender side of packet) and its all zeros.</p><p>Has anyone ever seen behavior similar to this or know what might cause this, the packets are going across a provider that is doing QnQ and MPLS, but no inspection.</p></div><div id="comment-10411-info" class="comment-info"><span class="comment-age">(23 Apr '12, 14:25)</span> tarjall</div></div><span id="10420"></span><div id="comment-10420" class="comment"><div id="post-10420-score" class="comment-score"></div><div class="comment-text"><p>I don't think the packet got modified on its way. Yes, the bytes ARE different, BUT you captured the data at the client side ON the client. And that means that Wireshark (or whatever capturing software you used) grabbed the packet before the NIC finalized it for the wire. You'll notice that also most of your outgoing TCP checksums are incorrect at the client as well - that is a sign for someone having captured on a system that is part of the communication.</p><p>To be able to see what really happens you'll have to capture with additional PCs, not ON the PCs/Servers that are part of the problem.</p></div><div id="comment-10420-info" class="comment-info"><span class="comment-age">(24 Apr '12, 05:28)</span> Jasper ♦♦</div></div></div><div id="comment-tools-10297" class="comment-tools"></div><div class="clear"></div><div id="comment-10297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

