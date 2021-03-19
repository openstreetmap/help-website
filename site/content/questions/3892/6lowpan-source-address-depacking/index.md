+++
type = "question"
title = "6LoWPAN Source Address Depacking"
description = '''Hi! I am working with 6LoWPAN protocol, and I am dissecting some packets to understand it correctly. When I have started sniffing my own packets I set the address: fe80::0011:22ff:fe33:4455/64. When wireshark extract the information of this packets, the generated address is: 2002:db8::0011:22ff:fe33...'''
date = "2011-05-03T01:43:00Z"
lastmod = "2011-05-03T23:42:00Z"
weight = 3892
keywords = [ "6lowpan" ]
aliases = [ "/questions/3892" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [6LoWPAN Source Address Depacking](/questions/3892/6lowpan-source-address-depacking)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3892-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I am working with 6LoWPAN protocol, and I am dissecting some packets to understand it correctly. When I have started sniffing my own packets I set the address: <strong>fe80::0011:22ff:fe33:4455/64</strong>.</p><p>When wireshark extract the information of this packets, the generated address is: <strong>2002:db8::0011:22ff:fe33:4455</strong></p><p>Why not FE80::...? As I've read in the RFC...?</p><p>I am reading the internet-draft for 6lowpan comrpession of IPv6 datagrams of February 2011.</p><p>Thanks in Advance</p></div><div id="question-tags" class="tags-container tags">6lowpan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '11, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/838c19776a7048a5f0b5780a087e17e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cesar%20Bernardini&#39;s gravatar image" /><p>Cesar Bernar...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cesar Bernardini has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 May '11, 07:36</p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span></p></div></div><div id="comments-container-3892" class="comments-container"></div><div id="comment-tools-3892" class="comment-tools"></div><div class="clear"></div><div id="comment-3892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3906"></span>

<div id="answer-container-3906" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3906-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check your protocol preferences, for the expansion of address it needs to have a context.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '11, 23:42</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3906" class="comments-container"><span id="3920"></span><div id="comment-3920" class="comment"><div id="post-3920-score" class="comment-score"></div><div class="comment-text"><p>I don't fully understood your answer!</p><p>Where are the protocol preferences? Is there something I didnt read in the specification? Something from the operative system implementing the protocol? If this is in Linux and you know where it's the information, let me know :)</p><p>Thanks in advance. Cesar</p></div><div id="comment-3920-info" class="comment-info"><span class="comment-age">(04 May '11, 07:18)</span> Cesar Bernar...</div></div><span id="3922"></span><div id="comment-3922" class="comment"><div id="post-3922-score" class="comment-score">1</div><div class="comment-text"><p>Jaap is referring to Wireshark's 6LoWPAN protocol prefrences. You can change the preferences by right-clicking on "6LoWPAN" in the packet detail (middle pane) or by selecting Edit→Preferences→Protocols→6LoWPAN from the main menu.</p><p>(I've also converted your answer to a comment.)</p></div><div id="comment-3922-info" class="comment-info"><span class="comment-age">(04 May '11, 07:35)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-3906" class="comment-tools"></div><div class="clear"></div><div id="comment-3906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

