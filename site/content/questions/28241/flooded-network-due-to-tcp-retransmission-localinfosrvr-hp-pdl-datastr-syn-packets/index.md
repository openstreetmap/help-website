+++
type = "question"
title = "Flooded network due to [TCP Retransmission] localinfosrvr &gt; hp-pdl-datastr [SYN] packets"
description = '''Hi all: I have a LAN (~100 PC&#x27;s, 10 servers, 6 Enterasys B3G124-48) that is having 3/4 blackouts a day; blackout meaning all switches ports blinking at the same time, big latency, and hughe packet loss, with no other solution rather than turning switches and routers off, wait, turn them on, and OK. ...'''
date = "2013-12-18T02:10:00Z"
lastmod = "2013-12-18T03:57:00Z"
weight = 28241
keywords = [ "retransmission", "network", "tcp", "blackout" ]
aliases = [ "/questions/28241" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Flooded network due to \[TCP Retransmission\] localinfosrvr &gt; hp-pdl-datastr \[SYN\] packets](/questions/28241/flooded-network-due-to-tcp-retransmission-localinfosrvr-hp-pdl-datastr-syn-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28241-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all:</p><p>I have a LAN (~100 PC's, 10 servers, 6 Enterasys B3G124-48) that is having 3/4 blackouts a day; blackout meaning all switches ports blinking at the same time, big latency, and hughe packet loss, with no other solution rather than turning switches and routers off, wait, turn them on, and OK.</p><p>My first approach (quite newbie to this), is to "turn on" Wireshark when the blackout happens: what I can see at that particular moment is 99.9% of packets like this:</p><p><strong>192.168.4.250 192.168.4.191 TCP 62 [TCP Retransmission] localinfosrvr &gt; hp-pdl-datastr [SYN] Win = 65535 Len=0</strong></p><p>Sometimes these are the IP's involved, and sometimes there are others; already updated Enterasys firmware to latest versión, changed Network cards, updated drivers, updated A.Virus, updated the Windows/Linux end PC's, changed ports in the switches, changed some network cables, etc. I am quite desperated....</p><p>This LAN is conected to the Internet and to other networks through optical fiber provided by the Spanish "big Telecom company". After Googling this, I can't see a clear direction about where to fight this. Could anyone please give a hint?.</p><p>Thank you in advance, sorry for my por english, and maybe for the lame question.....</p><p>P.</p></div><div id="question-tags" class="tags-container tags">retransmission network tcp blackout</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '13, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/8512e9911a31317e3192a22d023071f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pdrinio&#39;s gravatar image" /><p>pdrinio<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pdrinio has no accepted answers">0%</span></p></div></div><div id="comments-container-28241" class="comments-container"></div><div id="comment-tools-28241" class="comment-tools"></div><div class="clear"></div><div id="comment-28241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28248"></span>

<div id="answer-container-28248" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28248-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>what I can see at that particular moment is 99.9% of packets like this:<br />
192.168.4.250 192.168.4.191 TCP 62 [TCP Retransmission] localinfosrvr &gt; hp-pdl-datastr [SYN] Win = 65535 Len=0</p></blockquote><p>Looks like Wireshark sees the <strong>same</strong> frame again and again.</p><blockquote><p>Could anyone please give a hint?.</p></blockquote><p>As per your description, it sounds like a Layer 2 loop to me (someone created a ring by patching the wrong switch ports together). Did you check that? Do you run (rapid) spanning tree on your switches? If you don't know how to enable that, please ask your local Enterasys guru.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '13, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-28248" class="comments-container"></div><div id="comment-tools-28248" class="comment-tools"></div><div class="clear"></div><div id="comment-28248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

